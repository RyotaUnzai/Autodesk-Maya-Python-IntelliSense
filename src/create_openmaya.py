import re
import shutil
from functools import cached_property
from pathlib import Path
from typing import Any

import autopep8
from bs4 import BeautifulSoup, NavigableString, Tag, element

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
        document_root: str | Path,
        # export_path: str | Path,
        option: IntelliSenseOptionModel,
    ) -> None:
        self.option = option
        if isinstance(document_root, str):
            document_root = Path(document_root)
        self.document_root = document_root
        # base = r"D:/development/github/Autodesk-Maya-Python-IntelliSense/mayaProductHelps/maya-2024-developer-help-enu/index.html#!/url=./cpp_ref/group___open_maya.html"

        # Path(document_root) / self.option.maya.documents / "CommandsPython"
        # self.export_path = Path(export_path)
        self.commands_data = {}

    @cached_property
    def openMayaPath(self) -> Path:
        return self.document_root / "cpp_ref/group___open_maya.html"

    @cached_property
    def openMayaAnimPath(self) -> Path:
        return self.document_root / "cpp_ref/group___open_maya_anim.html"

    @cached_property
    def openMayaFXPath(self) -> Path:
        return self.document_root / "cpp_ref/group___open_maya_f_x.html"

    @cached_property
    def openMayaRenderPath(self) -> Path:
        return self.document_root / "cpp_ref/group___open_maya_render.html"

    @cached_property
    def openMayaUIPath(self) -> Path:
        return self.document_root / "cpp_ref/group___open_maya_u_i.html"

    @cached_property
    def functionSetPath(self) -> Path:
        return self.document_root / "cpp_ref/group___m_fn.html"

    @cached_property
    def proxyPath(self) -> Path:
        return self.document_root / "cpp_ref/group___m_px.html"

    def __init_export_dir(self) -> None:
        self.export_path.mkdir(exist_ok=True)
        self.maya_dir

    @cached_property
    def maya_dir(self) -> Path:
        maya_dir = self.export_path / "maya"
        maya_dir.mkdir(exist_ok=True)
        return maya_dir

    def get_html_content(self, path: Path) -> str:
        with open(path, "r") as file:
            return file.read()

    def _get_modules_files(self, resultSet: element.ResultSet) -> list[Path]:
        files = []
        for result in resultSet:
            href = result.get("href")
            if href:
                modulefile = self.document_root / href.replace("#!/url=./", "")
                if "class" in modulefile.name:
                    files.append(modulefile)
        return files

    def __create_openMaya(self) -> None:
        root_html_content = self.get_html_content(self.openMayaPath)
        soup = BeautifulSoup(root_html_content, "html.parser")
        memberdecls = soup.find("div", class_="contents")
        links = memberdecls.find_all("a", class_="el")
        files = self._get_modules_files(links)

        for file in files:
            print(file)

    def run(self) -> None:
        self.__create_openMaya()


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
    omPYI = CreateOpenMayaPYI(document_root=r"D:/development/github/Autodesk-Maya-Python-IntelliSense/mayaProductHelps/maya-2024-developer-help-enu", option=IntelliSenseOptionModel(**data))
    omPYI.run()
