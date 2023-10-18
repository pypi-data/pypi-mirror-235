from pathlib import Path
from typing import Any, Literal, Optional

from pydantic import DirectoryPath, Field, FilePath, validator
from pydantic.fields import ModelField

from .. import types
from .base import BaseModel, ConfigPath, LogPath, RunPath


class Etcd(BaseModel):
    """Settings for Etcd (for Patroni)."""

    v2: bool = Field(default=False, description="Configure Patroni to use etcd v2.")

    hosts: tuple[types.Address, ...] = Field(
        default=(types.Address("127.0.0.1:2379"),),
        description="List of etcd endpoint.",
    )

    protocol: Literal["http", "https"] = Field(
        default="http",
        description="http or https, if not specified http is used.",
    )

    cacert: Optional[FilePath] = Field(
        default=None,
        description="Certificate authority to validate the server certificate.",
    )

    cert: Optional[FilePath] = Field(
        default=None,
        description="Client certificate for authentication.",
    )

    key: Optional[FilePath] = Field(
        default=None,
        description="Private key corresponding to the client certificate.",
    )

    @validator("cacert", "cert")
    def __validate_cert_and_protocol_(
        cls, value: Optional[FilePath], values: dict[str, Any]
    ) -> Optional[FilePath]:
        """Make sure protocol https is used when setting certificates."""
        if value is not None and values["protocol"] == "http":
            raise ValueError("'https' protocol is required")
        return value


class WatchDog(BaseModel):
    """Settings for watchdog (for Patroni)."""

    mode: Literal["off", "automatic", "required"] = Field(
        default="off", description="watchdog mode."
    )

    device: Optional[Path] = Field(
        default=None,
        description="Path to watchdog.",
    )

    safety_margin: Optional[int] = Field(
        default=None,
        description=(
            "Number of seconds of safety margin between watchdog triggering"
            " and leader key expiration."
        ),
    )

    @validator("device")
    def __validate_device_(cls, value: Path) -> Path:
        if value and not value.exists():
            raise ValueError(f"path {value} does not exists")
        return value


class RESTAPI(BaseModel):
    """Settings for Patroni's REST API."""

    cafile: Optional[FilePath] = Field(
        default=None,
        description="Certificate authority (or bundle) to verify client certificates.",
    )

    certfile: Optional[FilePath] = Field(
        default=None,
        description="PEM-encoded server certificate to enable HTTPS.",
    )

    keyfile: Optional[FilePath] = Field(
        default=None,
        description="PEM-encoded private key corresponding to the server certificate.",
    )

    verify_client: Optional[Literal["optional", "required"]] = Field(
        default=None, description="Whether to check client certificates."
    )

    @validator("verify_client")
    def __validate_verify_client_and_certfile_(
        cls, value: Optional[Any], values: dict[str, Any]
    ) -> Optional[Any]:
        """Make sure that certfile is set when verify_client is."""
        if value is not None and values.get("certfile") is None:
            raise ValueError("requires 'certfile' to enable TLS")
        return value


class CTL(BaseModel):
    """Settings for Patroni's CTL."""

    certfile: FilePath = Field(
        description="PEM-encoded client certificate.",
    )

    keyfile: FilePath = Field(
        description="PEM-encoded private key corresponding to the client certificate.",
    )


class ServerSSLOptions(BaseModel):
    """Settings for server certificate verification."""

    mode: Optional[
        Literal[
            "disable",
            "allow",
            "prefer",
            "require",
            "verify-ca",
            "verify-full",
        ]
    ] = Field(
        default=None,
        description="Verification mode.",
    )
    crl: Optional[FilePath] = Field(
        default=None,
        description="Certificate Revocation List (CRL).",
    )
    crldir: Optional[DirectoryPath] = Field(
        default=None,
        description="Directory with CRL files.",
    )
    rootcert: Optional[FilePath] = Field(
        default=None,
        description="Root certificate(s).",
    )


class ConnectionOptions(BaseModel):
    ssl: Optional[ServerSSLOptions] = Field(
        default=None,
        description="Settings for server certificate verification when connecting to remote PostgreSQL instances.",
    )


class PostgreSQL(BaseModel):
    connection: Optional[ConnectionOptions] = Field(
        default=None,
        description="Client (libpq) connection options.",
    )
    passfile: ConfigPath = Field(
        default=ConfigPath("patroni/{name}.pgpass"),
        description="Path to .pgpass password file managed by Patroni.",
    )
    use_pg_rewind: bool = Field(
        default=False, description="Whether or not to use pg_rewind."
    )


class Settings(BaseModel):
    """Settings for Patroni."""

    execpath: FilePath = Field(
        default=Path("/usr/bin/patroni"),
        description="Path to patroni executable.",
    )

    configpath: ConfigPath = Field(
        default=ConfigPath("patroni/{name}.yaml"),
        description="Path to the config file.",
    )

    logpath: LogPath = Field(
        default=LogPath("patroni"),
        description="Path where directories are created (based on instance name) to store patroni log files.",
    )

    pid_file: RunPath = Field(
        default=RunPath("patroni/{name}.pid"),
        description="Path to which Patroni process PID will be written.",
    )

    loop_wait: int = Field(
        default=10, description="Number of seconds the loop will sleep."
    )

    etcd: Etcd = Field(default_factory=Etcd, description="Etcd settings.")

    watchdog: WatchDog = Field(
        default_factory=WatchDog, description="Watchdog settings."
    )

    ctl: Optional[CTL] = Field(default=None, description="CTL settings.")

    postgresql: PostgreSQL = Field(
        default_factory=PostgreSQL, description="PostgreSQL settings."
    )

    restapi: RESTAPI = Field(default_factory=RESTAPI, description="REST API settings.")

    @validator("restapi")
    def __validate_restapi_verify_client_(
        cls, value: RESTAPI, values: dict[str, Any], field: ModelField
    ) -> RESTAPI:
        """Make sure 'ctl' client certificates are provided when setting
        restapi.verify_client to required.
        """
        if value.verify_client == "required" and values.get("ctl") is None:
            raise ValueError(
                f"'ctl' must be provided when '{field.name}.verify_client' is set to 'required'"
            )
        return value
