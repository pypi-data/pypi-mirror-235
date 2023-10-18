from __future__ import annotations

from typing import Any

from .ctx import Context
from .pm import PluginManager
from .settings import Settings


def do(
    pm: PluginManager,
    settings: Settings,
    env: dict[str, Any] | None = None,
    header: str = "",
) -> None:
    if env is None:
        env = {}
    pm.hook.site_configure_install(settings=settings, pm=pm, header=header, env=env)


def undo(pm: PluginManager, settings: Settings, ctx: Context) -> None:
    pm.hook.site_configure_uninstall(settings=settings, pm=pm, ctx=ctx)


def check(pm: PluginManager, settings: Settings) -> bool:
    """Return True if the installation is complete."""
    return all(pm.hook.site_configure_installed(settings=settings, pm=pm))
