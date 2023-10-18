import enum
from pathlib import Path
from typing import Literal

from pydantic import AnyHttpUrl, Field, FilePath

from .. import types
from .base import BaseModel, ConfigPath, DataPath, LogPath, RunPath, ServerCert


class Plugin(types.AutoStrEnum):
    activity = enum.auto()
    administration = enum.auto()
    dashboard = enum.auto()
    maintenance = enum.auto()
    monitoring = enum.auto()
    pgconf = enum.auto()
    statements = enum.auto()


class LogMethod(types.AutoStrEnum):
    stderr = enum.auto()
    syslog = enum.auto()
    file = enum.auto()


class Settings(BaseModel):
    """Settings for temBoard agent"""

    ui_url: AnyHttpUrl = Field(description="URL of the temBoard UI.")

    signing_key: FilePath = Field(
        description="Path to the public key for UI connection."
    )

    certificate: ServerCert = Field(
        description="TLS certificate files for the temboard-agent HTTP server."
    )

    execpath: FilePath = Field(
        default=Path("/usr/bin/temboard-agent"),
        description="Path to the temboard-agent executable.",
    )

    role: str = Field(
        default="temboardagent",
        description="Name of the PostgreSQL role for temBoard agent.",
    )

    configpath: ConfigPath = Field(
        default=ConfigPath("temboard-agent/temboard-agent-{name}.conf"),
        description="Path to the config file.",
    )

    pid_file: RunPath = Field(
        default=RunPath("temboard-agent/temboard-agent-{name}.pid"),
        description="Path to which temboard-agent process PID will be written.",
    )

    plugins: tuple[Plugin, ...] = Field(
        default=(
            Plugin.monitoring,
            Plugin.dashboard,
            Plugin.activity,
        ),
        description="Plugins to load.",
    )

    home: DataPath = Field(
        default=DataPath("temboard-agent/{name}"),
        description="Path to agent home directory containing files used to store temporary data",
    )

    logpath: LogPath = Field(
        default=LogPath("temboard"),
        description="Path where log files are stored.",
    )

    logmethod: LogMethod = Field(
        default=LogMethod.stderr, description="Method used to send the logs."
    )

    loglevel: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = Field(
        default="INFO", description="Log level."
    )
