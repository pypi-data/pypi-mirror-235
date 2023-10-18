import socket
from typing import ClassVar, Optional

from pydantic import Extra, Field, FilePath, SecretStr, validator

from ... import types
from .common import RESTAPI


class ClusterMember(types.BaseModel, extra=Extra.allow, frozen=True):
    """An item of the list of members returned by Patroni API /cluster endpoint."""

    host: str
    name: str
    port: int
    role: str
    state: str


class ClientSSLOptions(types.BaseModel):
    cert: FilePath = Field(description="Client certificate.")
    key: FilePath = Field(description="Private key.")
    password: Optional[SecretStr] = Field(
        default=None, description="Password for the private key."
    )


class ClientAuth(types.BaseModel):
    ssl: Optional[ClientSSLOptions] = Field(
        default=None,
        description="Client certificate options.",
    )


class PostgreSQL(types.BaseModel):
    connect_host: Optional[str] = Field(
        default=None,
        description="Host or IP address through which PostgreSQL is externally accessible.",
    )
    replication: Optional[ClientAuth] = Field(
        default=None,
        description="Authentication options for client (libpq) connections to remote PostgreSQL by the replication user.",
    )
    rewind: Optional[ClientAuth] = Field(
        default=None,
        description="Authentication options for client (libpq) connections to remote PostgreSQL by the rewind user.",
    )


class Etcd(types.BaseModel):
    username: str = Field(
        description="Username for basic authentication to etcd.",
    )
    password: SecretStr = Field(
        description="Password for basic authentication to etcd."
    )


class ServiceManifest(types.ServiceManifest, service_name="patroni"):
    _cli_config: ClassVar[dict[str, types.CLIConfig]] = {
        "cluster_members": {"hide": True},
        "postgresql_connect_host": {"hide": True},
    }
    _ansible_config: ClassVar[dict[str, types.AnsibleConfig]] = {
        "cluster_members": {"hide": True},
    }

    # XXX Or simply use instance.qualname?
    cluster: str = Field(
        description="Name (scope) of the Patroni cluster.",
        readOnly=True,
    )
    node: str = Field(
        default_factory=socket.getfqdn,
        description="Name of the node (usually the host name).",
        readOnly=True,
    )
    restapi: RESTAPI = Field(
        default_factory=RESTAPI, description="REST API configuration"
    )

    postgresql: Optional[PostgreSQL] = Field(
        default=None,
        description="Configuration for PostgreSQL setup and remote connection.",
    )
    etcd: Optional[Etcd] = Field(
        default=None, description="Instance-specific options for etcd DCS backend."
    )
    cluster_members: list[ClusterMember] = Field(
        default=[],
        description="Members of the Patroni this instance is member of.",
        readOnly=True,
    )

    __validate_none_values_ = validator("node", "restapi", pre=True, allow_reuse=True)(
        types.default_if_none
    )
