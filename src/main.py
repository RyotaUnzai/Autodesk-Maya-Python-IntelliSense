from pathlib import Path

import yaml

from create_pyi import CreateMayaCommandPYI
from models import Arguments, IntelliSenseOptionModel

if __name__ == "__main__":
    args = Arguments.parse_args()

    cwd = Path.cwd()
    create_pyi = cwd / "src" / "create_pyi.yml"
    version: str = args.version or "2023.3"
    language = args.language or "en"
    export_dir = args.export_path or cwd / f"{language}_maya{version}"
    export_dir.mkdir(exist_ok=True)
    export_path = export_dir / "typings"
    export_path.mkdir(exist_ok=True)
    document_dir = args.document_dir or cwd / "mayaProductHelps"

    maya = cwd / "src" / f"maya{int(float(version))}.yml"
    with open(create_pyi, "r") as file:
        data = yaml.safe_load(file)
    with open(maya, "r") as file:
        maya_data = yaml.safe_load(file)
    data["maya"] = maya_data

    option = IntelliSenseOptionModel(**data)

    mayacmd = CreateMayaCommandPYI(
        document_root=document_dir,
        export_path=export_path,
        language=language,
        version=version,
        option=IntelliSenseOptionModel(**data),
    )
    mayacmd.run()
