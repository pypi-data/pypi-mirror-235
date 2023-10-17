import json
import os
import platform
import typing

import yaml

from .base import ToolboxConfig, ToolboxConfigSpec

EXTENSIONS = {"yaml", "yml", "json"}


def _get_config(
    extra_paths: typing.Optional[typing.List[str]] = None,
) -> ToolboxConfigSpec:
    """Tries to locate a usable toolbox config, otherwise returns defaults."""

    paths = []
    if extra_paths:
        paths.extend(extra_paths)

    # search ~/.config/sapphiccode/toolbox.<ext>
    home = os.path.expanduser("~")
    if home:
        for ext in EXTENSIONS:
            paths.append(os.path.join(home, ".config", "sapphiccode", f"toolbox.{ext}"))

    # search /etc/sapphiccode/toolbox.<ext>
    if platform.platform() in {"Linux", "Darwin"}:
        for ext in EXTENSIONS:
            paths.append(os.path.join("/etc", "sapphiccode", f"toolbox.{ext}"))

    # actually perform the search
    data = {"apiVersion": "sapphicco.de/v1alpha1", "kind": "ToolboxConfig", "spec": {}}
    for path in paths:
        if not os.path.exists(path):
            continue

        if path.endswith(".yaml") or path.endswith(".yml"):
            with open(path, "r") as f:
                data = yaml.safe_load(f)
                break

        if path.endswith(".json"):
            with open(path, "r") as f:
                data = json.load(f)
                break

    return ToolboxConfig.model_validate(data).spec
