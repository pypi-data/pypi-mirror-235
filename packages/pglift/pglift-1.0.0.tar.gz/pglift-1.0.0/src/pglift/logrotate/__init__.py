from __future__ import annotations

import logging
from pathlib import Path

from pglift import util

from .. import hookimpl
from ..models.system import Instance, PostgreSQLInstance
from ..pm import PluginManager
from ..settings import Settings, _logrotate

logger = logging.getLogger(__name__)


def register_if(settings: Settings) -> bool:
    return settings.logrotate is not None


def get_settings(settings: Settings) -> _logrotate.Settings:
    assert settings.logrotate is not None
    return settings.logrotate


def config_path(settings: _logrotate.Settings) -> Path:
    return settings.configdir / "logrotate.conf"


@hookimpl
def site_configure_install(settings: Settings, pm: PluginManager) -> None:
    logger.info("creating logrotate config directory")
    s = get_settings(settings)
    s.configdir.mkdir(mode=0o750, exist_ok=True, parents=True)
    results = pm.hook.logrotate_config(settings=settings)
    with config_path(s).open("w") as f:
        logger.info("writing logrotate config")
        f.write("\n".join(results))


@hookimpl
def site_configure_uninstall(settings: Settings) -> None:
    logger.info("deleting logrotate config directory")
    s = get_settings(settings)
    util.rmtree(s.configdir)


@hookimpl
def site_configure_installed(settings: Settings) -> bool:
    s = get_settings(settings)
    if not (fpath := config_path(s)).exists():
        logger.error("logrotate configuration '%s' missing", fpath)
        return False
    return True


def instance_configpath(
    settings: _logrotate.Settings, instance: PostgreSQLInstance
) -> Path:
    return settings.configdir / f"{instance.qualname}.conf"


@hookimpl
def instance_dropped(instance: Instance) -> None:
    settings = get_settings(instance._settings)
    instance_configpath(settings, instance).unlink(missing_ok=True)
