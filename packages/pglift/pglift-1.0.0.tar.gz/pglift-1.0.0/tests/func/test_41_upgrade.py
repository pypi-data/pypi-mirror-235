from __future__ import annotations

from pathlib import Path

from pglift import databases, postgresql
from pglift.ctx import Context
from pglift.models import system
from pglift.types import Status

from . import passfile_entries


def test_upgrade(
    ctx: Context, pg_version: str, upgraded_instance: system.Instance
) -> None:
    assert upgraded_instance.name == "upgraded"
    assert upgraded_instance.version == pg_version
    assert postgresql.status(upgraded_instance) == Status.not_running
    with postgresql.running(ctx, upgraded_instance):
        assert databases.exists(ctx, upgraded_instance, "postgres")


def test_upgrade_pgpass(
    ctx: Context,
    passfile: Path,
    upgraded_instance: system.Instance,
    surole_password: str | None,
    pgbackrest_password: str | None,
) -> None:
    backuprole = ctx.settings.postgresql.backuprole.name
    port = upgraded_instance.port
    assert f"*:{port}:*:postgres:{surole_password}" in passfile_entries(passfile)
    assert f"*:{port}:*:{backuprole}:{pgbackrest_password}" in passfile_entries(
        passfile, role=backuprole
    )
