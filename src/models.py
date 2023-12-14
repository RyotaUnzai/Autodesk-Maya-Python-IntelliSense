import re
from enum import Enum
from pathlib import Path, WindowsPath
from typing import Any

import autopep8
from bs4 import BeautifulSoup
from pydantic import BaseModel, Field, validator
from typing_extensions import Final, Self


class FunctionData:
    arguments: list
    description: str
    url: str


class ArgumentData:
    longName: str
    shortName: str
    type: str
    docs: str
    properties: list[str]


class NewType(BaseModel):
    name: str
    type: str


class NewTypes(BaseModel):
    items: list[NewType]


class Common(BaseModel):
    ignore: list[str]
    new_types: NewTypes = Field(alias="new types")
    maya_argments: dict = Field(alias="maya argments")

    class Config:
        populate_by_name = True

    @validator("new_types", pre=True)
    def create_new_type_list(cls, v):
        return {"items": [NewType(name=item[0], type=item[1]) for item in v]}


class Maya(BaseModel):
    version: int
    python: str
    help_url: Path = Field(alias="help url")
    imports: list[str]

    class Config:
        populate_by_name = True

    @validator("imports", pre=True)
    def create_imports_list(cls, v):
        return v or []

    @validator("help_url", pre=True)
    def create_help_url(cls, v):
        return Path(v)


class IntelliSenseOptionModel(BaseModel):
    common: Common
    maya: Maya


class HTags(Enum):
    hSynopsis = "hSynopsis"
    hReturn = "hReturn"
    hKeywords = "hKeywords"
    hFlags = "hFlags"
    hExamples = "hExamples"
    hRelated = "hRelated"
    hNotes = "hNotes"
