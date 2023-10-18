from __future__ import annotations

from functools import partial
from typing import Any

import click

from .. import patroni
from ..cli.util import (
    Group,
    instance_identifier_option,
    pass_component_settings,
    pass_instance,
)
from ..models import system
from ..settings import _patroni
from . import impl

pass_patroni_settings = partial(pass_component_settings, patroni, "Patroni")


@click.group("patroni", cls=Group)
@instance_identifier_option
def cli(**kwargs: Any) -> None:
    """Handle Patroni service for an instance."""


@cli.command("logs")
@pass_patroni_settings
@pass_instance
def logs(instance: system.Instance, settings: _patroni.Settings) -> None:
    """Output Patroni logs."""
    for line in impl.logs(instance.qualname, settings):
        click.echo(line, nl=False)
