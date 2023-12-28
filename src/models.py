from argparse import ArgumentParser
from enum import Enum
from pathlib import Path
from typing import Any, Optional

from pydantic import BaseModel, Field, validator
from typing_extensions import Self


class FunctionData:
    arguments: list[str]
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
    maya_argments: dict[str, str] = Field(alias="maya argments")
    all_definition: list[str] = Field(alias="__all__")

    class Config:
        populate_by_name = True

    @validator("new_types", pre=True)
    def create_new_type_list(cls, v: Any) -> dict[str, list[NewType]]:
        return {"items": [NewType(name=item[0], type=item[1]) for item in v]}


class Docs(BaseModel):
    jp: str
    en: str


class Translator(BaseModel):
    synopsis_word: str = Field(alias="synopsis word")
    synopsis_note_text: str = Field(alias="synopsis note text")
    flags_word: str = Field(alias="flags word")
    return_word: str = Field(alias="return word")
    return_none_word: str = Field(alias="return none word")
    example_word: str = Field(alias="example word")
    properties_word: str = Field(alias="properties word")
    property_mode: dict[str, str] | None = Field(alias="property mode")

    class Config:
        populate_by_name = True

    def get_property_mode(self, property: str) -> str:
        if isinstance(self.property_mode, None):
            return property
        return self.property_mode[property]


class Maya(BaseModel):
    version: int
    python: str
    help_url: Path = Field(alias="help url")
    imports: list[str]
    documents: dict[str, Docs]

    class Config:
        populate_by_name = True

    @validator("imports", pre=True)
    def create_imports_list(cls, v: Any) -> list[str]:
        return v or []

    @validator("help_url", pre=True)
    def create_help_url(cls, v: str) -> Path:
        return Path(v)

    @validator("documents", pre=True)
    def create_base_documents(cls, v: dict[str, dict[str, str]]) -> dict[str, Docs]:
        docs: dict[str, Docs] = {}
        for key, value in v.items():
            docs[str(key)] = Docs(**value)
        return docs


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
    version: Optional[str] = Field(alias="version", default=None)
    export_path: Optional[Path] = Field(alias="export_path", default=None)
    document_dir: Optional[Path] = Field(alias="document_dir", default=None)
    language: Optional[str] = Field(alias="language", default=None)

    class Config:
        populate_by_name = True

    @classmethod
    def parse_args(cls) -> Self:
        parser = ArgumentParser()
        for k in cls.model_json_schema()["properties"].keys():
            if k in ["export_path", "document_dir"]:
                parser.add_argument(f"-{k[0:1]}", f"--{k}", type=Path)
            else:
                parser.add_argument(f"-{k[0:1]}", f"--{k}")
        return cls.model_validate(parser.parse_args().__dict__)

    @validator("language", pre=True)
    def create_imports_list(cls, v: str) -> str:
        try:
            return v.lower()
        except AttributeError:
            return None
