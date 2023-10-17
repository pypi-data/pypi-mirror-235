import json
import re
import subprocess
import typing


def exiftool(*args, capture: bool = False, **kwargs) -> str | int:
    """Invokes ExifTool."""

    args = ("exiftool", *args)

    if not capture:
        return subprocess.check_call(args, **kwargs)
    else:
        return subprocess.check_output(args, text=True, **kwargs)


def exiftool_json(path: str) -> typing.Dict[str, typing.Any]:
    json_raw = exiftool("-json", path, capture=True)
    assert isinstance(json_raw, str)

    data = json.loads(json_raw)[0]
    assert isinstance(data, dict)

    return data


def supplement_tags(data: typing.Dict[str, typing.Any]) -> typing.Dict[str, typing.Any]:
    """
    Supplements ExifTool tags for better consistency across camera vendors.

    - Toolbox35mmEquivalentFocalLength
    """

    # consistent 35mm equivalent focal length tag
    if equiv := data.get("FocalLength35efl"):
        if not isinstance(equiv, str):
            raise TypeError()
        if match := re.search(r"equivalent: (\d+\.\d mm)", equiv):
            data["Toolbox35mmEquivalentFocalLength"] = match.group(1)

    if equiv := data.get("FocalLengthIn35mmFormat"):
        data["Toolbox35mmEquivalentFocalLength"] = equiv

    return data
