from __future__ import annotations

import copy
import json
from pathlib import Path

import pydantic
import pytest
import yaml
from ansible.module_utils.common.arg_spec import ArgumentSpecValidator

from pglift import prometheus
from pglift.models import helpers, interface
from pglift.pm import PluginManager
from pglift.types import Manifest

all_plugins = PluginManager.all()


def test_argspec_from_instance_manifest(
    datadir: Path,
    write_changes: bool,
    composite_instance_model: type[interface.Instance],
) -> None:
    compare_argspec(composite_instance_model, write_changes, datadir)


def test_argspec_from_role_manifest(
    datadir: Path,
    write_changes: bool,
    composite_role_model: type[interface.Role],
) -> None:
    compare_argspec(composite_role_model, write_changes, datadir)


@pytest.mark.parametrize(
    "manifest_type",
    [
        prometheus.PostgresExporter,
        interface.Database,
    ],
)
def test_argspec_from_model_manifest(
    datadir: Path, write_changes: bool, manifest_type: type[Manifest]
) -> None:
    compare_argspec(manifest_type, write_changes, datadir)


def compare_argspec(
    manifest_type: type[Manifest],
    write_changes: bool,
    datadir: Path,
    *,
    name: str | None = None,
) -> None:
    actual = helpers.argspec_from_model(manifest_type)
    if name is None:
        name = manifest_type.__name__.lower()
    fpath = datadir / f"ansible-argspec-{name}.json"
    if write_changes:
        fpath.write_text(json.dumps(actual, indent=2, sort_keys=True) + "\n")
    expected = json.loads(fpath.read_text())
    assert actual == expected


@pytest.mark.parametrize(
    "objtype",
    [
        ("instance", interface.Instance, interface.InstanceApplyResult),
        ("role", interface.Role, interface.ApplyResult),
        ("database", interface.Database, interface.ApplyResult),
        ("postgresexporter", prometheus.models.PostgresExporter, interface.ApplyResult),
    ],
    ids=lambda v: v[0],
)
def test_doc_fragments(
    datadir: Path,
    objtype: tuple[str, type[pydantic.BaseModel], type[pydantic.BaseModel]],
    write_changes: bool,
) -> None:
    name, m, r = objtype
    if hasattr(m, "composite"):
        model = m.composite(all_plugins)
    else:
        model = m
    options = helpers.argspec_from_model(model)
    validator = ArgumentSpecValidator(copy.deepcopy(options))
    examples = (datadir / "ansible-examples" / f"{name}.yaml").read_text()
    for example in yaml.safe_load(examples):
        assert len(example) == 2 and "name" in example
        collection_name = (set(example) - {"name"}).pop()
        assert not validator.validate(example[collection_name]).error_messages
    data = {
        "options": options,
        "return values": helpers.argspec_from_model(r),
        "examples": examples,
    }
    fpath = datadir / "ansible-doc-fragments" / f"{name}.json"
    fpath.parent.mkdir(parents=True, exist_ok=True)
    if write_changes:
        fpath.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    expected = json.loads(fpath.read_text())
    assert data == expected
