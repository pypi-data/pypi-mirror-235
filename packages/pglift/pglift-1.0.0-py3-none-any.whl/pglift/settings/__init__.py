import grp
import json
import os
import pwd
import tempfile
from pathlib import Path
from typing import Any, Literal, Optional

import pydantic
import yaml
from pydantic import Field, root_validator, validator
from pydantic.env_settings import SettingsSourceCallable
from pydantic.fields import ModelField

from .. import __name__ as pkgname
from .. import exceptions, util
from . import (
    _cli,
    _logrotate,
    _patroni,
    _pgbackrest,
    _postgresql,
    _powa,
    _prometheus,
    _rsyslog,
    _systemd,
    _temboard,
)
from .base import prefix_values


def default_prefix(uid: int) -> Path:
    """Return the default path prefix for 'uid'.

    >>> default_prefix(0)
    PosixPath('/')
    >>> default_prefix(42)  # doctest: +ELLIPSIS
    PosixPath('/.../.local/share/pglift')
    """
    if uid == 0:
        return Path("/")
    return util.xdg_data_home() / pkgname


def default_run_prefix(uid: int) -> Path:
    """Return the default run path prefix for 'uid'."""
    if uid == 0:
        base = Path("/run")
    else:
        try:
            base = util.xdg_runtime_dir(uid)
        except exceptions.FileNotFoundError:
            base = Path(tempfile.gettempdir())

    return base / pkgname


def default_sysuser() -> tuple[str, str]:
    pwentry = pwd.getpwuid(os.getuid())
    grentry = grp.getgrgid(pwentry.pw_gid)
    return pwentry.pw_name, grentry.gr_name


def yaml_settings_source(settings: pydantic.BaseSettings) -> dict[str, Any]:
    """Load settings values 'settings.yaml' file if found in user or system
    config directory directory.
    """
    assert isinstance(settings, SiteSettings)
    path = settings.site_settings()
    if path is None:
        return {}
    settings = yaml.safe_load(path.read_text())
    if not isinstance(settings, dict):
        raise exceptions.SettingsError(
            f"failed to load site settings from {path}, expecting an object"
        )
    return settings


def json_config_settings_source(settings: pydantic.BaseSettings) -> dict[str, Any]:
    """Load settings values from 'SETTINGS' environment variable.

    If this variable has a value starting with @, it is interpreted as a path
    to a JSON file. Otherwise, a JSON serialization is expected.
    """
    env_settings = os.getenv("SETTINGS")
    if not env_settings:
        return {}
    if env_settings.startswith("@"):
        config = Path(env_settings[1:])
        encoding = settings.__config__.env_file_encoding
        # May raise FileNotFoundError, which is okay here.
        env_settings = config.read_text(encoding)
    try:
        return json.loads(env_settings)  # type: ignore[no-any-return]
    except json.decoder.JSONDecodeError as e:
        raise exceptions.SettingsError(str(e)) from e


def is_root() -> bool:
    return os.getuid() == 0


class Settings(pydantic.BaseSettings):
    """Settings for pglift."""

    class Config:
        frozen = True

    postgresql: _postgresql.Settings = Field(default_factory=_postgresql.Settings)
    patroni: Optional[_patroni.Settings] = None
    pgbackrest: Optional[_pgbackrest.Settings] = None
    powa: Optional[_powa.Settings] = None
    prometheus: Optional[_prometheus.Settings] = None
    temboard: Optional[_temboard.Settings] = None
    systemd: Optional[_systemd.Settings] = None
    logrotate: Optional[_logrotate.Settings] = None
    rsyslog: Optional[_rsyslog.Settings] = None
    cli: _cli.Settings = Field(default_factory=_cli.Settings)

    service_manager: Optional[Literal["systemd"]] = None
    scheduler: Optional[Literal["systemd"]] = None

    prefix: Path = Field(
        default=default_prefix(os.getuid()),
        description="Path prefix for configuration and data files.",
    )

    run_prefix: Path = Field(
        default=default_run_prefix(os.getuid()),
        description="Path prefix for runtime socket, lockfiles and PID files.",
    )

    sysuser: tuple[str, str] = Field(
        default_factory=default_sysuser,
        help=(
            "(username, groupname) of system user running PostgreSQL; "
            "mostly applicable when operating PostgreSQL with systemd in non-user mode"
        ),
    )

    @validator("prefix", "run_prefix")
    def __validate_prefix_(cls, value: Path) -> Path:
        """Make sure path settings are absolute."""
        if not value.is_absolute():
            raise ValueError("expecting an absolute path")
        return value

    @root_validator(skip_on_failure=True)
    def __prefix_paths(cls, values: dict[str, Any]) -> dict[str, Any]:
        """Prefix child settings fields with the global 'prefix'."""
        return prefix_values(
            values,
            {"prefix": values["prefix"], "run_prefix": values["run_prefix"]},
        )

    @root_validator(pre=True)
    def __set_service_manager_scheduler(cls, values: dict[str, Any]) -> dict[str, Any]:
        """Set 'service_manager' and 'scheduler' to 'systemd' by default if systemd is enabled."""
        if values.get("systemd") is not None:
            values.setdefault("service_manager", "systemd")
            values.setdefault("scheduler", "systemd")
        return values

    @validator("service_manager", "scheduler")
    def __validate_service_manager_scheduler_(
        cls, v: Optional[Literal["systemd"]], values: dict[str, Any]
    ) -> Optional[Literal["systemd"]]:
        """Make sure systemd is enabled globally when 'service_manager' or 'scheduler' are set."""
        if values.get("systemd") is None and v is not None:
            raise ValueError("cannot use systemd, if 'systemd' is not enabled globally")
        return v

    @root_validator(pre=True)
    def __validate_is_not_root(cls, values: dict[str, Any]) -> dict[str, Any]:
        """Make sure current user is not root.

        This is not supported by postgres (cannot call neither initdb nor pg_ctl as root).
        """
        if is_root():
            raise exceptions.UnsupportedError("pglift cannot be used as root")
        return values

    @validator("patroni")
    def __validate_patroni_passfile_(
        cls,
        value: Optional[_patroni.Settings],
        values: dict[str, Any],
        field: ModelField,
    ) -> Optional[_patroni.Settings]:
        try:
            postgresql_settings = values["postgresql"]
        except KeyError:  # Another validation probably failed.
            return value
        assert isinstance(postgresql_settings, _postgresql.Settings)
        if (
            value
            and postgresql_settings.auth.passfile
            and value.postgresql.passfile == postgresql_settings.auth.passfile
        ):
            raise ValueError(
                f"'{field.name}.postgresql.passfile' must be different from 'postgresql.auth.passfile'"
            )
        return value

    @validator("patroni")
    def __validate_patroni_requires_replrole_(
        cls, value: Optional[_patroni.Settings], values: dict[str, Any]
    ) -> Optional[_patroni.Settings]:
        try:
            postgresql_settings = values["postgresql"]
        except KeyError:  # Another validation probably failed.
            return value
        assert isinstance(postgresql_settings, _postgresql.Settings)
        if value and postgresql_settings.replrole is None:
            raise ValueError("'postgresql.replrole' must be provided to use 'patroni'")
        return value


class SiteSettings(Settings):
    """Settings loaded from site-sources.

    Load user or site settings from:
    - 'settings.yaml' if found in user or system configuration directory, and,
    - SETTINGS environment variable.
    """

    @staticmethod
    def site_settings() -> Optional[Path]:
        """Return content of 'settings.yaml' if found in site configuration
        directories.
        """
        for hdlr in (util.xdg_config, util.etc_config):
            if (fpath := hdlr("settings.yaml")) is not None:
                return fpath
        return None

    class Config:
        frozen = True

        @classmethod
        def customise_sources(
            cls,
            init_settings: SettingsSourceCallable,
            env_settings: SettingsSourceCallable,
            file_secret_settings: SettingsSourceCallable,
        ) -> tuple[SettingsSourceCallable, ...]:
            return (
                init_settings,
                env_settings,
                json_config_settings_source,
                yaml_settings_source,
            )
