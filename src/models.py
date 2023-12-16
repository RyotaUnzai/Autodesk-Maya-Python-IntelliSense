from argparse import ArgumentParser
from enum import Enum
from pathlib import Path

from pydantic import BaseModel, Field, validator
from typing_extensions import Self


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
    all_definition: list[str] = Field(alias="__all__")

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
    def create_imports_list(cls, v) -> list[str]:
        return v or []

    @validator("help_url", pre=True)
    def create_help_url(cls, v) -> Path:
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


class Arguments(BaseModel):
    version: int | None
    export_path: Path | None

    @classmethod
    def parse_args(cls) -> Self:
        parser = ArgumentParser()
        for k in cls.model_json_schema()["properties"].keys():
            if k == "export_path":
                parser.add_argument(f"-{k[0:1]}", f"--{k}", type=Path)
            else:
                parser.add_argument(f"-{k[0:1]}", f"--{k}")
        return cls.model_validate(parser.parse_args().__dict__)
