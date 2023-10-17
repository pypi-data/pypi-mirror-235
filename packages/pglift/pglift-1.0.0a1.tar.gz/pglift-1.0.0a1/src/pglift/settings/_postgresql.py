import enum
from pathlib import Path
from typing import Any, Optional

from pydantic import DirectoryPath, Field, validator

from .. import types
from .base import BaseModel, DataPath, LogPath, RunPath


class PostgreSQLVersion(types.StrEnum):
    """PostgreSQL version

    >>> PostgreSQLVersion("12")
    <PostgreSQLVersion.v12: '12'>
    >>> PostgreSQLVersion(12)
    <PostgreSQLVersion.v12: '12'>
    """

    v16 = "16"
    v15 = "15"
    v14 = "14"
    v13 = "13"
    v12 = "12"

    @classmethod
    def _missing_(cls, value: object) -> Any:
        if isinstance(value, int):
            return cls(str(value))
        return super()._missing_(value)


class PostgreSQLVersionSettings(BaseModel):
    """Version-specific settings for PostgreSQL."""

    version: PostgreSQLVersion
    bindir: DirectoryPath


def _postgresql_bindir_version() -> tuple[str, str]:
    usrdir = Path("/usr")
    for version in PostgreSQLVersion:
        # Debian packages
        if (usrdir / "lib" / "postgresql" / version).exists():
            return str(usrdir / "lib" / "postgresql" / "{version}" / "bin"), version

        # RPM packages from the PGDG
        if (usrdir / f"pgsql-{version}").exists():
            return str(usrdir / "pgsql-{version}" / "bin"), version
    else:
        raise OSError("no PostgreSQL installation found")


def _postgresql_bindir() -> Optional[str]:
    try:
        return _postgresql_bindir_version()[0]
    except OSError:
        return None


class AuthLocalMethod(types.AutoStrEnum):
    """Local authentication method"""

    trust = enum.auto()
    reject = enum.auto()
    md5 = enum.auto()
    password = enum.auto()
    scram_sha_256 = "scram-sha-256"
    gss = enum.auto()
    sspi = enum.auto()
    ident = enum.auto()
    peer = enum.auto()
    pam = enum.auto()
    ldap = enum.auto()
    radius = enum.auto()


class AuthHostMethod(types.AutoStrEnum):
    """Host authentication method"""

    trust = enum.auto()
    reject = enum.auto()
    md5 = enum.auto()
    password = enum.auto()
    scram_sha_256 = "scram-sha-256"
    gss = enum.auto()
    sspi = enum.auto()
    ident = enum.auto()
    pam = enum.auto()
    ldap = enum.auto()
    radius = enum.auto()


class AuthHostSSLMethod(types.AutoStrEnum):
    """Host SSL authentication method"""

    trust = enum.auto()
    reject = enum.auto()
    md5 = enum.auto()
    password = enum.auto()
    scram_sha_256 = "scram-sha-256"
    gss = enum.auto()
    sspi = enum.auto()
    ident = enum.auto()
    pam = enum.auto()
    ldap = enum.auto()
    radius = enum.auto()
    cert = enum.auto()


class AuthSettings(BaseModel):
    """PostgreSQL authentication settings."""

    local: AuthLocalMethod = Field(
        default=AuthLocalMethod.trust,
        description="Default authentication method for local-socket connections.",
    )

    host: AuthHostMethod = Field(
        default=AuthHostMethod.trust,
        description="Default authentication method for local TCP/IP connections.",
    )

    hostssl: Optional[AuthHostSSLMethod] = Field(
        default=AuthHostSSLMethod.trust,
        description="Default authentication method for SSL-encrypted TCP/IP connections.",
    )

    passfile: Optional[Path] = Field(
        default=Path.home() / ".pgpass", description="Path to .pgpass file."
    )

    password_command: tuple[str, ...] = Field(
        default=(), description="An optional command to retrieve PGPASSWORD from"
    )


class InitdbSettings(BaseModel):
    """Settings for initdb step of a PostgreSQL instance."""

    locale: Optional[str] = Field(
        default="C", description="Instance locale as used by initdb."
    )

    encoding: Optional[str] = Field(
        default="UTF8", description="Instance encoding as used by initdb."
    )

    data_checksums: Optional[bool] = Field(
        default=None, description="Use checksums on data pages."
    )


class Role(BaseModel):
    name: str
    pgpass: bool = Field(
        default=False, description="Whether to store the password in .pgpass file."
    )


class SuRole(Role):
    """Super-user role."""

    name: str = "postgres"


class BackupRole(Role):
    """Backup role."""

    name: str = "backup"


class Settings(BaseModel):
    """Settings for PostgreSQL."""

    bindir: Optional[str] = Field(
        default_factory=_postgresql_bindir,
        description="Default PostgreSQL bindir, templated by version.",
    )

    @validator("bindir")
    def __bindir_is_templated_(cls, value: Optional[str]) -> Optional[str]:
        if value is not None and "{version}" not in value:
            raise ValueError("missing '{version}' template placeholder")
        return value

    versions: tuple[PostgreSQLVersionSettings, ...] = Field(
        default=(), description="Available PostgreSQL versions."
    )

    @validator("versions", always=True)
    def __set_versions_(
        cls, value: tuple[PostgreSQLVersionSettings, ...], values: dict[str, Any]
    ) -> tuple[PostgreSQLVersionSettings, ...]:
        if (bindir := values.get("bindir")) is None and not value:
            raise ValueError(
                "either a value is required, or the 'bindir' setting is needed in order to enable 'versions' discovery"
            )
        pgversions = [v.version for v in value]
        versions = list(value)
        for version in PostgreSQLVersion:
            if version in pgversions:
                continue
            if bindir is not None:
                version_bindir = Path(bindir.format(version=version))
                if version_bindir.exists():
                    versions.append(
                        PostgreSQLVersionSettings(
                            version=version, bindir=version_bindir
                        )
                    )
        if not versions:
            raise ValueError(
                f"no value could be inferred from bindir template {bindir!r}"
            )
        versions.sort(key=lambda v: v.version)
        return tuple(versions)

    default_version: PostgreSQLVersion = Field(  # type: ignore[assignment]
        default=None,
        description=(
            "Default PostgreSQL version to use, if unspecified at instance creation or upgrade. "
            "If unset, defaults to the latest PostgreSQL version as declared in or inferred from 'versions' setting."
        ),
    )

    @validator("default_version", always=True)
    def __validate_default_version_(
        cls, value: Optional[PostgreSQLVersion], values: dict[str, Any]
    ) -> PostgreSQLVersion:
        if not (pgversions := {v.version for v in values.get("versions", ())}):
            raise ValueError("empty 'versions' field")
        if value is None:
            return max(pgversions)  # type: ignore[no-any-return]
        if value not in pgversions:
            raise ValueError(
                f"value must be amongst declared 'versions': {', '.join(pgversions)}"
            )
        return value

    initdb: InitdbSettings = Field(default_factory=InitdbSettings)

    auth: AuthSettings = Field(default_factory=AuthSettings)

    surole: SuRole = Field(default=SuRole(), description="Instance super-user role.")

    replrole: Optional[str] = Field(
        default=None, description="Instance replication role."
    )

    backuprole: BackupRole = Field(
        default=BackupRole(), description="Instance role used to backup."
    )

    datadir: DataPath = Field(
        default=DataPath("pgsql/{version}/{name}/data"),
        description="Path segment from instance base directory to PGDATA directory.",
    )

    waldir: DataPath = Field(
        default=DataPath("pgsql/{version}/{name}/wal"),
        description="Path segment from instance base directory to WAL directory.",
    )

    logpath: LogPath = Field(
        default=LogPath("postgresql"),
        description="Path where log files are stored.",
    )

    socket_directory: RunPath = Field(
        default=RunPath("postgresql"),
        description="Path to directory where postgres unix socket will be written.",
    )

    dumps_directory: DataPath = Field(
        default=DataPath("dumps/{version}-{name}"),
        description="Path to directory where database dumps are stored.",
    )

    dump_commands: tuple[tuple[str, ...], ...] = Field(
        default=(
            (
                "{bindir}/pg_dump",
                "-Fc",
                "-f",
                "{path}/{dbname}_{date}.dump",
                "-d",
                "{conninfo}",
            ),
        ),
        description="Commands used to dump a database",
    )

    restore_commands: tuple[tuple[str, ...], ...] = Field(
        default=(
            (
                "{bindir}/pg_restore",
                "-d",
                "{conninfo}",
                "{createoption}",
                "{path}/{dbname}_{date}.dump",
            ),
        ),
        description="Commands used to restore a database",
    )

    @validator("surole", "backuprole")
    def __validate_role_pgpass_and_passfile_(
        cls, value: Role, values: dict[str, Any]
    ) -> Role:
        passfile = values["auth"].passfile
        if passfile is None and value.pgpass:
            raise ValueError("cannot set 'pgpass' without 'auth.passfile'")
        return value

    @validator("dump_commands", "restore_commands")
    def __validate_dump_restore_commands_(
        cls, value: tuple[tuple[str, ...], ...]
    ) -> tuple[tuple[str, ...], ...]:
        """Validate 'dump_commands' and 'restore_commands' when defined
        without {bindir} substitution variable.
        """
        for i, cmd in enumerate(value, 1):
            program = cmd[0]
            if "{bindir}" not in program:
                p = Path(program)
                if not p.is_absolute():
                    raise ValueError(
                        f"program {program!r} from command #{i} is not an absolute path"
                    )
                if not p.exists():
                    raise ValueError(
                        f"program {program!r} from command #{i} does not exist"
                    )
        return value
