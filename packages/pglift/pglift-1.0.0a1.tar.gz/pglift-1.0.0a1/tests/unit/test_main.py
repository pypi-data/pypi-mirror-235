from __future__ import annotations

import re

import pglift


def test_execpath() -> None:
    assert re.match(r".*python\S* -m pglift$", pglift.execpath)
