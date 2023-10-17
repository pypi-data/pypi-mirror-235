import enum
import typing

import pydantic


class Edge(enum.Enum):
    LEFT = "left"
    RIGHT = "right"
    TOP = "top"
    BOTTOM = "bottom"


EDGES: typing.Dict[
    Edge,
    typing.Tuple[
        # rotation, axis, position lambda
        int,
        int,
        typing.Callable[[int, typing.Tuple[int, int]], typing.Tuple[int, int]],
    ],
] = {
    Edge.TOP: (180, 0, lambda border, size: (border, 0)),
    Edge.LEFT: (270, 1, lambda border, size: (0, border)),
    Edge.BOTTOM: (0, 0, lambda border, size: (border, size[1] + border)),
    Edge.RIGHT: (90, 1, lambda border, size: (size[0] + border, border)),
}


class VerticalAnchor(enum.Enum):
    TOP = "top"
    MIDDLE = "middle"
    BOTTOM = "bottom"


ANCHORS: typing.Dict[VerticalAnchor, typing.Tuple[str, float]] = {
    VerticalAnchor.TOP: ("a", 0),
    VerticalAnchor.MIDDLE: ("m", 0.5),
    VerticalAnchor.BOTTOM: ("d", 1.0),
}


class ImageBorderConfig(pydantic.BaseModel):
    border_percent: float = 2.5
    border_minimum_px: int = 32
    border_color: str = "black"

    text_font: str = "B612-Regular"
    text_height_percent: float = 45.0
    text_color: str = "white"
    text_edge: Edge = Edge.BOTTOM
    text_vertical_anchor: VerticalAnchor = VerticalAnchor.MIDDLE

    elements_l: typing.Dict[int, str] = {
        0: "ISO {ISO}",
        4: "f/{FNumber}",
        7: "{ShutterSpeed}",
        10: "{Toolbox35mmEquivalentFocalLength}",
    }
    elements_r: typing.Dict[int, str] = {
        0: "{Copyright}, {Artist}",
    }
    """
    Elements are shifted by computed border pixels * dictionary key amount.

    Formatting supports all variables output by `exiftool -json`.
    """

    output_format: str = "JPEG"
    output_quality: int = 95

    @pydantic.validator("output_format")
    def _validate_output_format(cls, value: str) -> str:
        value = value.upper()
        if value == "JPG":
            return "JPEG"
        return value
