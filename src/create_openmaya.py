import re
import shutil
from functools import cached_property
from pathlib import Path
from typing import Any

import autopep8
from bs4 import BeautifulSoup, NavigableString, Tag

from models import (
    ArgumentData,
    FunctionData,
    HTags,
    IntelliSenseOptionModel,
    OpenMayaAPI1,
)


class CreateOpenMayaPYI:
    """
    A class for generating Python Interface (PYI) files for Maya commands.

    This class parses Maya command documentation from HTML files, extracts relevant
    information, and generates PYI files which include type hints and docstrings for
    each Maya command based on the parsed data.
    """

    document_root: Path
    export_path: Path
    code_text: str
    code_texts: dict[str, dict[str, str]]
    html_content: str
    commands_data: dict[str, FunctionData]
    function_name: str
    argument_data: list[ArgumentData]
    current_letter: str | None = None
    om: OpenMayaAPI1

    def __init__(
        self,
        # document_root: str | Path,
        # export_path: str | Path,
        option: IntelliSenseOptionModel,
    ) -> None:
        self.option = option
        self.document_root = r"D:\development\github\Autodesk-Maya-Python-IntelliSense\mayaProductHelps\maya-2024-developer-help-enu"
        base = r"D:/development/github/Autodesk-Maya-Python-IntelliSense/mayaProductHelps/maya-2024-developer-help-enu/index.html#!/url=./cpp_ref/group___open_maya.html"

        # Path(document_root) / self.option.maya.documents / "CommandsPython"
        # self.export_path = Path(export_path)
        self.commands_data = {}

    def __init_export_dir(self) -> None:
        self.export_path.mkdir(exist_ok=True)
        self.maya_dir

    @cached_property
    def maya_dir(self) -> Path:
        maya_dir = self.export_path / "maya"
        maya_dir.mkdir(exist_ok=True)
        return maya_dir


def main() -> None:
    rootDir = Path(r"D:/development/github/Autodesk-Maya-Python-IntelliSense/mayaProductHelps/maya-2024-developer-help-enu")
    openMaya = "cpp_ref/group___open_maya.html"
    openMayaAnim = "cpp_ref/group___open_maya_anim.html"
    openMayaFX = "cpp_ref/group___open_maya_f_x.html"
    openMayaRender = "cpp_ref/group___open_maya_render.html"
    openMayaUI = "cpp_ref/group___open_maya_u_i.html"
    functionSet = "cpp_ref/group___m_fn.html"
    proxy = "cpp_ref/group___m_px.html"
    # macros = "cpp_ref/group___macros.html"

    file_path = Path(rootDir) / openMaya

    print(OpenMayaAPI1.OpenMaya.name)

    with open(file_path, "r") as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, "html.parser")

    memberdecls = soup.find("div", class_="contents")
    links = memberdecls.find_all("a", class_="el")
    # links = memberdecls.find_all("a", class_="href")

    modules = []
    hrefs = []
    for link in links:
        # module = link.text
        href = link.get("href")
        if href:
            hrefs.append(href)
            print(href)

        # if "<" in module:
        #     module = module.split(" ")[0]
        # if ":" in module:
        #     module = module.split(":")[0]

        # modules.append(module)
    # for module in modules:
    #     print(module)


if __name__ == "__main__":
    import yaml

    cwd = Path.cwd()
    create_pyi = cwd / "src" / "create_pyi.yml"
    version: str = "2024.2"
    language = "en"

    maya = cwd / "src" / f"maya{int(float(version))}.yml"
    with open(create_pyi, "r", encoding="utf-8") as file:
        data = yaml.safe_load(file)
        data["common"]["language"] = language
    with open(maya, "r", encoding="utf-8") as file:
        maya_data = yaml.safe_load(file)
        maya_data["language"] = language
        maya_data["versioning"] = version
    data["maya"] = maya_data
    main()
    option = IntelliSenseOptionModel(**data)
    print(option.maya.openmaya1.documents)
    print(option.maya.openmaya1.OpenMaya)  # cpp_ref\group___open_maya.html

    # TODO: 各ModuleのHTML情報を取得できるようになったところ
