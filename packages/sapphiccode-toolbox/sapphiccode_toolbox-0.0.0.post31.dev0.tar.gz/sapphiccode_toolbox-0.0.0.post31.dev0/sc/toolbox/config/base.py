import typing

import pydantic

from .image_border import ImageBorderConfig


class ImageConfig(pydantic.BaseModel):
    border: ImageBorderConfig = ImageBorderConfig()


class ToolboxConfigSpec(pydantic.BaseModel):
    image: ImageConfig = ImageConfig()


class ToolboxConfig(pydantic.BaseModel):
    apiVersion: typing.Literal["sapphicco.de/v1alpha1"]
    kind: typing.Literal["ToolboxConfig"]
    spec: ToolboxConfigSpec
