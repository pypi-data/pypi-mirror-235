import os
import shutil
from pathlib import Path
from typing import Any, ClassVar

from pydantic import Field, root_validator, validator

from .. import util
from .base import BaseModel


def default_systemd_unit_path(uid: int) -> Path:
    """Return the default systemd unit path for 'uid'.

    >>> default_systemd_unit_path(0)
    PosixPath('/etc/systemd/system')
    >>> default_systemd_unit_path(42)  # doctest: +ELLIPSIS
    PosixPath('/.../.local/share/systemd/user')
    """
    if uid == 0:
        return Path("/etc/systemd/system")
    return util.xdg_data_home() / "systemd" / "user"


class Settings(BaseModel):
    """Systemd settings."""

    systemctl: ClassVar[Path]

    @root_validator
    def __systemctl_(cls, values: dict[str, Any]) -> dict[str, Any]:
        if not hasattr(cls, "systemctl"):
            systemctl = shutil.which("systemctl")
            if systemctl is None:
                raise ValueError("systemctl command not found")
            cls.systemctl = Path(systemctl)  # type: ignore[misc]
        return values

    unit_path: Path = Field(
        default=default_systemd_unit_path(os.getuid()),
        description="Base path where systemd units will be installed.",
    )

    user: bool = Field(
        default=True,
        description="Use the system manager of the calling user, by passing --user to systemctl calls.",
    )

    sudo: bool = Field(
        default=False,
        description="Run systemctl command with sudo; only applicable when 'user' is unset.",
    )

    @validator("sudo")
    def __validate_sudo_and_user_(cls, value: bool, values: dict[str, Any]) -> bool:
        if value and values.get("user"):
            raise ValueError("cannot be used with 'user' mode")
        return value
