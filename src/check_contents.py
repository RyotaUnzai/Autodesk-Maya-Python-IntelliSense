import shutil
from pathlib import Path

import yaml

from models import Maya

cwd = Path.cwd()
rootDir = cwd / "Autodesk-Maya-Python-IntelliSense" / "mayaProductHelps"
contentRootDir = cwd / "Autodesk-Maya-Python-IntelliSense" / "contents"

sourceVersion = 2024.2
targetVersion = 2024.1
language = "jp"

content_dir = contentRootDir / f"{language}_{str(targetVersion)}"
content_dir.mkdir(exist_ok=True)


source_maya_yaml = cwd / "src" / f"maya{int(sourceVersion)}.yml"
target_maya_yaml = cwd / "src" / f"maya{int(sourceVersion)}.yml"


with open(source_maya_yaml, "r") as file:
    source_maya_data = yaml.safe_load(file)
    source_maya_data["language"] = language
    source_maya_data["versioning"] = str(sourceVersion)

SourceMaya = Maya(**source_maya_data)

with open(target_maya_yaml, "r") as file:
    target_mayaBase_data = yaml.safe_load(file)
    target_mayaBase_data["language"] = language
    target_mayaBase_data["versioning"] = str(targetVersion)

TargetMaya = Maya(**target_mayaBase_data)


sorce_doc_dir = rootDir / SourceMaya.documents / "CommandsPython"
target_doc_dir = rootDir / TargetMaya.documents / "CommandsPython"


SourceFiles = sorted([f.stem for f in sorce_doc_dir.glob("*") if f.suffix == ".html"])
TargetFiles = sorted([f.stem for f in target_doc_dir.glob("*") if f.suffix == ".html"])


def check(source: tuple[list[str], Path], target: tuple[list[str], Path], path: Path) -> None:

    for element in source[0]:
        existFile = target[1] / f"{element}.html"

        if not existFile.exists():
            sourcePath = source[1] / f"{element}.html"
            copyPath = path / f"{element}.content"
            shutil.copy(sourcePath.as_posix(), copyPath.as_posix())


check((SourceFiles, sorce_doc_dir), (TargetFiles, target_doc_dir), content_dir)
