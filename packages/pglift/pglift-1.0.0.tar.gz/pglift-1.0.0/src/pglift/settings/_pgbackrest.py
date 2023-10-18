from pathlib import Path
from typing import Literal, Optional, Union

from pydantic import Field, FilePath

from .base import BaseModel, ConfigPath, DataPath, LogPath, RunPath, ServerCert


class HostRepository(BaseModel):
    """Remote repository host for pgBackRest."""

    host: str = Field(description="Host name of the remote repository.")
    host_port: Optional[int] = Field(
        default=None,
        description="Port to connect to the remote repository.",
    )
    host_config: Optional[Path] = Field(
        default=None,
        description="pgBackRest configuration file path on the remote repository.",
    )


class TLSHostRepository(HostRepository):
    mode: Literal["host-tls"]
    cn: str = Field(description="Certificate Common Name of the remote repository.")
    certificate: ServerCert = Field(
        description="TLS certificate files for the pgBackRest server on site."
    )
    port: int = Field(default=8432, description="Port for the TLS server on site.")
    pid_file: RunPath = Field(
        default=RunPath("pgbackrest.pid"),
        description="Path to which pgbackrest server process PID will be written.",
    )


class SSHHostRepository(HostRepository):
    mode: Literal["host-ssh"]
    host_user: Optional[str] = Field(
        default=None,
        description="Name of the user that will be used for operations on the repository host.",
    )
    cmd_ssh: Optional[Path] = Field(
        default=None,
        description="SSH client command. Use a specific SSH client command when an alternate is desired or the ssh command is not in $PATH.",
    )


class Retention(BaseModel):
    """Retention settings."""

    archive: int = 2
    diff: int = 3
    full: int = 2


class PathRepository(BaseModel):
    """Remote repository (path) for pgBackRest."""

    mode: Literal["path"]
    path: DataPath = Field(
        description="Base directory path where backups and WAL archives are stored.",
    )
    retention: Retention = Field(default=Retention(), description="Retention options.")


class Settings(BaseModel):
    """Settings for pgBackRest."""

    execpath: FilePath = Field(
        default=Path("/usr/bin/pgbackrest"),
        description="Path to the pbBackRest executable.",
    )

    configpath: ConfigPath = Field(
        default=ConfigPath("pgbackrest"),
        description="Base path for pgBackRest configuration files.",
    )

    repository: Union[TLSHostRepository, SSHHostRepository, PathRepository] = Field(
        description="Repository definition, either as a (local) path-repository or as a host-repository.",
        discriminator="mode",
    )

    logpath: LogPath = Field(
        default=LogPath("pgbackrest"),
        description="Path where log files are stored.",
    )

    spoolpath: DataPath = Field(
        default=DataPath("pgbackrest/spool"),
        description="Spool path.",
    )

    lockpath: RunPath = Field(
        default=RunPath("pgbackrest/lock"),
        description="Path where lock files are stored.",
    )
