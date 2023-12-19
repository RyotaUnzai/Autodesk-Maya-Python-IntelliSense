import re
from functools import cached_property
from pathlib import Path
from typing import Any

import autopep8
import yaml
from bs4 import BeautifulSoup, NavigableString, Tag

from models import ArgumentData, Arguments, FunctionData, HTags, IntelliSenseOptionModel
import translater


class CreateMayaCommandPYI:
    document_root: Path
    export_path: Path
    code_text: str
    code_texts: dict[str, dict[str, str]]
    html_content: str
    commands_data: dict[str, FunctionData]
    function_name: str
    argument_data: list[ArgumentData]
    current_letter: str | None = None
    translater: translater.Translater

    def __init__(
        self,
        document_root: str | Path,
        export_path: str | Path,
        language: str,
        version: str,
        option: IntelliSenseOptionModel,
    ) -> None:
        self.option = option
        if language == "jp":
            path = self.option.maya.documents[str(version)].jp
            self.translater = translater.Jp()
        else:
            path = self.option.maya.documents[str(version)].en
            self.translater = translater.En()
        self.document_root = Path(document_root) / path / "CommandsPython"

        self.export_path = Path(export_path)
        self.__init_export_dir()
        self.commands_data = {}
        self.__init_code_text()

    @cached_property
    def cloudhelp_url(self) -> str:
        return f"https://{self.option.maya.help_url.as_posix()}"

    @property
    def cmd_cloudhelp_url(self) -> str:
        return f"{self.cloudhelp_url}/{self._cmd_name}"

    @cmd_cloudhelp_url.setter
    def cmd_cloudhelp_url(self, cmd_name: str) -> None:
        self._cmd_name = cmd_name

    @cached_property
    def __import_typing_code(self) -> str:
        return """from typing import (
    NewType,
    Any
)\n\n\n"""

    @cached_property
    def __imports_code(self) -> str:
        code = ""
        for import_line in self.option.maya.imports:
            code += f"{import_line}\n"
        return code

    @cached_property
    def __new_types_code(self) -> str:
        code = ""
        for item in self.option.common.new_types.items:
            code += f'{item.name} = NewType("{item.name}", {item.type})\n'
        return code

    def __init_code_text(self) -> None:
        self.code_text = ""
        self.code_text += self.__imports_code
        self.code_text += self.__import_typing_code
        self.code_text += self.__new_types_code

    def extract_html_content(self, file_path: Path | str) -> None:
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                self.html_content = file.read()
        except Exception as e:
            raise e

    def __init_export_dir(self) -> None:
        self.export_path.mkdir(exist_ok=True)
        self.maya_dir
        self.cmds_dir

    @cached_property
    def maya_dir(self) -> Path:
        maya_dir = self.export_path / "maya"
        maya_dir.mkdir(exist_ok=True)
        return maya_dir

    @cached_property
    def cmds_dir(self) -> Path:
        cmds_dir = self.maya_dir / "cmds"
        cmds_dir.mkdir(exist_ok=True)
        return cmds_dir

    def export_pyi(self) -> None:
        code = self.code_text
        for fileName in sorted(self.code_texts[self.current_letter].keys()):
            code += self.code_texts[self.current_letter][fileName]
        path = self.cmds_dir / f"mayacmds_{self.current_letter}.pyi"
        with open(path, "w+", encoding="UTF-8") as file:
            v = autopep8.fix_code(code)
            file.write(v)

    def create_initpy(self) -> None:
        import_text = ""
        # https://github.com/tiangolo/typer/issues/142
        definitions = ""
        for definition in self.option.common.all_definition:
            definitions += f'    "{definition}",\n'
        import_text += f"__all__ = [\n{definitions}]\n\n\n"
        for first_letter in sorted(self.code_texts.keys()):
            import_text += f"from mayacmds_{first_letter} import *\n"
        with open(self.maya_dir / "__init__.py", "w+", encoding="UTF-8") as file:
            file.write("")
        with open(self.cmds_dir / "__init__.py", "w+", encoding="UTF-8") as file:
            v = autopep8.fix_code(import_text)
            file.write(v)

    @property
    def soup(self) -> BeautifulSoup:
        """Convert HTML content to a BeautifulSoup object for parsing.
        This property uses BeautifulSoup to parse the HTML content stored in
        self.html_content, facilitating HTML parsing and manipulation. It returns
        a BeautifulSoup object initialized with the HTML content.
        Returns:
            BeautifulSoup: A parser object created from the HTML content.
        """
        return BeautifulSoup(self.html_content, "html.parser")

    def getHTagContent(self, value: str) -> Tag | NavigableString | None:
        section = self.soup.find("a", {"name": value})
        if section:
            h2_parent = section.find_parent("h2")
            next_sibling = h2_parent.find_next_sibling() if h2_parent else None
            if next_sibling:
                return next_sibling
            else:
                return None
        else:
            return None

    def is_only_whitespace(self, text: str) -> bool:
        """Checks if the string is non-empty and consists only of whitespace characters"""
        return text.isspace() if text else False

    def create_docstrings_example_texts(self) -> str:
        hExamples_content = self.getHTagContent(HTags.hExamples.value)
        if hExamples_content:
            hExamples_content_text = hExamples_content.get_text(strip=True)
            if not self.is_only_whitespace(hExamples_content_text):
                hExamples_content_text = hExamples_content_text.replace("# ", "").replace("#", "---\n")
                return f"\n{self.translater.EXAMPLE_WORD}:\n---\n{hExamples_content_text}\n\n---"
        return ""

    def create_docstrings_flags_texts(self) -> str:
        text = f"\n{self.translater.FLAGS_WORD}:\n---\n\n"
        for argData in self.argument_data:
            types = ""
            for p in argData.properties:
                prop = self.translater.property_mode(p)
                types += f"{prop}, "
            types = types[:-2]
            text += f"""
---
{argData.longName}: {argData.type}
    {self.translater.PROPERTIES_WORD}: {types}
    {argData.docs}
"""
        return text

    def create_function_text(self) -> str:
        functionData = self.commands_data[self.function_name]
        docstrings = self.create_docstrings_example_texts()
        flags = self.create_docstrings_flags_texts()
        code = ""
        for arguments in functionData.arguments:
            code += f"{arguments[0]}: {arguments[1]}, "
        code = f'''def {self.function_name}({code[:-2]}) -> {self.return_typeHint}:
    """{functionData.description}
        
{docstrings}
{self.docstrings_text}
{flags}
URL:
---
{functionData.url} 
    """  
\n\n'''
        return code

    def extract_table_data(self) -> None:
        tables = self.soup.find_all("table")
        self.argument_data = []
        for table in tables:
            rows = table.find_all("tr")
            for row in rows:
                columns = row.find_all("td")
                if columns:
                    if len(columns) == 3:
                        argumentData = ArgumentData()
                        isAppend = True
                        for i, col in enumerate(columns):
                            if i == 1 and col.text.strip() == "":
                                isAppend = False
                            if i == 0:
                                argumentData.longName = col.text.strip()
                            elif i == 1:
                                argumentData.type = col.text.strip()
                            elif i == 2:
                                images = col.find_all("img")
                                argumentData.properties = [img["src"].replace("../gfx/", "").replace(".gif", "") for img in images]
                        if isAppend:
                            colspan_column = row.find_next_sibling("tr")
                            if colspan_column and colspan_column.get("bgcolor") != "#EEEEEE":
                                text_col = colspan_column.find("td")
                                if text_col and text_col.get("colspan") == "3":
                                    argumentData.docs = text_col.text.strip()
                            try:
                                if argumentData.docs:
                                    self.argument_data.append(argumentData)
                            except AttributeError:
                                print("Non: argumentData.docs")

    def extract_between_specific_h2_tags(self, start_h2_tag: str) -> str | Any | None:
        pattern = re.compile(rf"{re.escape(start_h2_tag)}(.*?)(?=<h2>)", re.DOTALL)
        matches = re.search(pattern, self.html_content)
        return matches.group(1) if matches else None

    def extract_next_p_content(self) -> None:
        allSynopsis = self.extract_between_specific_h2_tags(f'<h2><a name="hSynopsis">{self.translater.SYNOPSIS_WORD}</a></h2>')
        soup = BeautifulSoup(allSynopsis, "html.parser")
        docs = soup.get_text()
        synopsis = soup.find("p", {"id": "synopsis"})
        self.description = ""
        current_element = synopsis
        while current_element and current_element.name != "h2":
            self.description += str(current_element.get_text())
            current_element = current_element.find_next_sibling()
        note_text = self.translater.SYNOPSIS_NOTE_TEXT
        # description_split = self.description.split(note_text)
        # mention = description_split[1].split("\n")[0]
        # command_description = description_split[1].replace(mention, f"\n{mention}")
        synopsis_description, command_description = docs.split(note_text)

        self.description = f"""{self.translater.SYNOPSIS_WORD}:
---
---
{synopsis_description}
{note_text}
{command_description}"""

    @property
    def first_letter(self) -> str:
        """Returns the first letter of the function name.
        If the funtion name is empty, return an empty string.
        Example:
            self.function_name = "selection"
            self.first_letter
            >> "s"
        """
        return self.function_name[0] if self.function_name else ""

    def getArgmentsList(self) -> list[list[str]]:
        code_tags = self.synopsis.find_all("code")
        self.resultArgs: list[list[str]] = []
        for code_tag in code_tags:
            a_tags = code_tag.find_all("a")
            i_tags = code_tag.find_all("i")
            for a, i in zip(a_tags, i_tags):
                flag = a.contents[0]
                if i.text in self.option.common.maya_argments:
                    self.resultArgs.append([flag, self.option.common.maya_argments[i.text]])
                else:
                    self.resultArgs.append([flag, i.text])
        return self.resultArgs

    @property
    def synopsis(self) -> Tag | NavigableString | None:
        synopsis_section = self.soup.find("a", {"name": HTags.hSynopsis.value}).find_parent("h2")
        return synopsis_section.find_next_sibling("p")

    def add_code_texts_key(self) -> None:
        """Add code text to the dictionary.
        Adds an entry to the self.code_texts dictionary with self.first_letter as the key
        and self.code_text as the value. If the key already exists, it does nothing.
        """
        if self.first_letter not in self.code_texts:
            if self.current_letter != None:
                self.export_pyi()
                print(f"end: {self.current_letter}")
            self.current_letter = self.first_letter
            print(f"start: {self.first_letter}")
            self.code_texts[self.first_letter] = {}

    def hReturn(self) -> Tag | NavigableString | str:
        section = self.soup.find("a", {"name": "hReturn"})
        if section:
            h2_parent = section.find_parent("h2")
            next_sibling = h2_parent.find_next_sibling() if h2_parent else None
            if next_sibling:
                return next_sibling
            else:
                return None
        else:
            return None

    def getReturnTable(self, table: Tag | NavigableString) -> tuple[str, str]:
        td_tags = table.find_all("td")
        if len(td_tags) > 1:
            td_texts = td_tags[1].get_text(strip=True)
        i_tag = table.find("i").text
        if i_tag in option.common.maya_argments:
            i_tag = option.common.maya_argments[i_tag]
        return i_tag, td_texts

    def getReturnData(self) -> None:
        return_content = self.hReturn()
        self.return_typeHint = ""
        returns_texts: list[list[str, str]] = []
        returns = []
        if return_content.text != self.translater.RETURN_NONE_WORD:
            soup = BeautifulSoup(str(return_content), "html.parser")
            tables = soup.find("table")
            if tables:
                try:
                    for table in tables:
                        try:
                            i_tag, td_texts = self.getReturnTable(table)
                            returns.append(i_tag)
                            returns_texts.append([i_tag, td_texts])
                        except Exception:
                            pass
                    returns = sorted(list(set(returns)))
                    for typeHint in returns:
                        self.return_typeHint += f"{typeHint} | "
                    self.return_typeHint = self.return_typeHint[:-3]
                except Exception:
                    i_tag, td_texts = self.getReturnTable(tables)
                    returns_texts = [i_tag, td_texts]
                    self.return_typeHint = i_tag
            else:
                print(f"error: {self.function_name}")
        else:
            self.return_typeHint = self.translater.RETURN_NONE_WORD
        self.docstrings_text = ""
        if returns_texts != []:
            self.docstrings_text = f"{self.translater.RETURN_WORD}:\n---\n\n"
            for returns_text in returns_texts:
                self.docstrings_text += f"\n    {returns_text[0]}: {returns_text[1]}"

    def create_code_text(self) -> None:
        count = 0
        self.code_texts = {}
        length = 0
        for iter in self.document_root.iterdir():
            length += 1
        count = 0
        for iter in self.document_root.iterdir():
            print(f"{length-count}/{length}")
            self.function_name = iter.stem
            if iter.stem not in self.option.common.ignore:
                self.add_code_texts_key()
                self.commands_data[self.function_name] = FunctionData()
                self.cmd_cloudhelp_url = iter.name
                self.commands_data[self.function_name].url = self.cmd_cloudhelp_url
                self.extract_html_content(iter)
                self.getReturnData()
                self.commands_data[self.function_name].arguments = self.getArgmentsList()

                self.extract_table_data()
                self.extract_next_p_content()
                self.commands_data[self.function_name].description = self.description
                self.code_texts[self.first_letter][self.function_name] = self.create_function_text()
            count += 1

    def run(self) -> None:
        self.create_code_text()
        self.create_initpy()


if __name__ == "__main__":
    args = Arguments.parse_args()

    cwd = Path.cwd()
    create_pyi = cwd / "src" / "create_pyi.yml"
    version: str = args.version or "2024"
    export_dir = args.export_path or cwd / f"maya{int(float(version))}"
    export_dir.mkdir(exist_ok=True)
    export_path = export_dir / "typings"
    export_path.mkdir(exist_ok=True)
    language = args.language or "en"
    document_dir = args.document_dir or cwd / "mayaProductHelps"  # / "Autodesk Maya User Guide 2024.2 (ADE 2.1)=en" / "CommandsPython"

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
