import re
from functools import cached_property
from pathlib import Path
from typing import Any

import autopep8
from bs4 import BeautifulSoup, NavigableString, Tag

from models import ArgumentData, FunctionData, HTags, IntelliSenseOptionModel


class CreateMayaCommandPYI:
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

    def __init__(
        self,
        document_root: str | Path,
        export_path: str | Path,
        option: IntelliSenseOptionModel,
    ) -> None:
        self.option = option
        self.document_root = Path(document_root) / self.option.maya.documents / "CommandsPython"

        self.export_path = Path(export_path)
        self.__init_export_dir()
        self.commands_data = {}
        self.__init_code_text()

    @cached_property
    def cloudhelp_url(self) -> str:
        """
        Generates and returns a fully qualified URL to the Maya help documentation based on the configured option.

        This method constructs the URL using the `help_url` attribute from the `maya` configuration option.
        The URL is created as an HTTPS URL. As a cached property, the generated URL is stored and reused,
        ensuring that it's only generated once during the lifespan of the instance.

        Returns:
            str: The full HTTPS URL pointing to the Maya help documentation.

        Usage:
            instance = YourClassName()
            help_url = instance.cloudhelp_url  # Accesses the cached URL
        """
        return f"https://{self.option.maya.help_url.as_posix()}"

    @property
    def cmd_cloudhelp_url(self) -> str:
        """
        Gets the full URL for the documentation of the currently processed Maya command.

        This property constructs the URL by appending the command's name to the base Maya help URL.
        The command name is set using the cmd_cloudhelp_url setter.

        Returns:
            str: The full URL pointing to the documentation of the specific Maya command.
        """
        return f"{self.cloudhelp_url}/{self._cmd_name}"

    @cmd_cloudhelp_url.setter
    def cmd_cloudhelp_url(self, cmd_name: str) -> None:
        """
        Sets the command name for which the cloud help URL is to be constructed.

        This setter updates the internal command name, which is used to generate the full URL
        for the command's documentation.

        Parameters:
            cmd_name (str): The name of the Maya command.
        """
        self._cmd_name = cmd_name

    @cached_property
    def __import_typing_code(self) -> str:
        """
        Generates and returns a string of import statements from the typing module.

        This cached property ensures the import code is generated only once and then reused.

        Returns:
            str: A string containing import statements from the typing module.
        """
        return """from typing import (
    NewType,
    Any
)\n\n\n"""

    @cached_property
    def __imports_code(self) -> str:
        """
        Constructs and returns the import statements required for the PYI file.

        This method iterates over the import lines defined in the configuration options
        and concatenates them into a single string.

        Returns:
            str: A string of concatenated import statements.
        """
        code = ""
        for import_line in self.option.maya.imports:
            code += f"{import_line}\n"
        return code

    @cached_property
    def __new_types_code(self) -> str:
        """
        Generates new type definitions for use in the PYI files.

        This method creates new type aliases based on the items specified in the configuration options.
        These types are used to enhance the type hinting in the generated PYI files.

        Returns:
            str: A string containing new type definitions.
        """
        code = ""
        for item in self.option.common.new_types.items:
            code += f'{item.name} = NewType("{item.name}", {item.type})\n'
        return code

    def __init_code_text(self) -> None:
        """
        Initializes the code text for PYI file generation.

        This method concatenates various parts of the code including imports and new type definitions,
        setting up the initial structure of the PYI file.
        """
        self.code_text = ""
        self.code_text += self.__imports_code
        self.code_text += self.__import_typing_code
        self.code_text += self.__new_types_code

    def extract_html_content(self, file_path: Path | str) -> None:
        """
        Reads the HTML content from the given file path and stores it in the instance.

        This method is used to read the HTML file corresponding to a Maya command and store its content
        for further processing.

        Parameters:
            file_path (Path | str): The path to the HTML file to be read.

        Raises:
            Exception: If there is an error reading the file.
        """
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                self.html_content = file.read()
        except Exception as e:
            raise e

    def __init_export_dir(self) -> None:
        """
        Initializes the export directory structure for the PYI files.

        This method ensures that the base export directory and its subdirectories for Maya and cmds exist.
        If they do not exist, they are created. This setup is necessary before starting the export of PYI files.
        """
        self.export_path.mkdir(exist_ok=True)
        self.maya_dir
        self.cmds_dir

    @cached_property
    def maya_dir(self) -> Path:
        """
        Gets the directory path for storing the exported Maya PYI files.

        This cached property ensures that the Maya directory is created only once and then reused.
        The directory is a subdirectory within the main export path specifically for Maya-related files.

        Returns:
            Path: The Path object representing the Maya directory.
        """
        maya_dir = self.export_path / "maya"
        maya_dir.mkdir(exist_ok=True)
        return maya_dir

    @cached_property
    def cmds_dir(self) -> Path:
        """
        Gets the directory path for storing the exported cmds PYI files.

        This cached property creates a 'cmds' subdirectory within the Maya directory. This directory
        is used to store the PYI files related to individual Maya commands.

        Returns:
            Path: The Path object representing the cmds directory.
        """
        cmds_dir = self.maya_dir / "cmds"
        cmds_dir.mkdir(exist_ok=True)
        return cmds_dir

    def export_pyi(self) -> None:
        """
        Exports the accumulated Python Interface (PYI) code for the current letter to a file.

        This method concatenates the PYI code for all the commands starting with the current letter
        and writes the combined code to a PYI file. The file is named based on the current letter and
        is formatted using the autopep8 tool for better readability.
        """
        code = self.code_text
        for fileName in sorted(self.code_texts[self.current_letter].keys()):
            code += self.code_texts[self.current_letter][fileName]
        path = self.cmds_dir / f"mayacmds_{self.current_letter}.pyi"
        with open(path, "w+", encoding="UTF-8") as file:
            v = autopep8.fix_code(code)
            file.write(v)

    def create_initpy(self) -> None:
        """
        Creates '__init__.py' files in the Maya and cmds directories.

        This method generates '__init__.py' files to ensure that the exported PYI files
        are recognized as Python modules. It includes dynamic import statements based on
        the command names processed, and adds a list of all command definitions to the '__all__' variable.

        The '__init__.py' file in the cmds directory imports all the generated mayacmds_<letter>.pyi files,
        while the one in the maya directory is created empty as a placeholder for the package.
        """
        import_text = ""
        # https://github.com/tiangolo/typer/issues/142
        definitions = ""
        for definition in self.option.common.all_definition:
            definitions += f'    "{definition}",\n'
        import_text += f"__all__ = [\n{definitions}]\n\n\n"
        for first_letter in sorted(self.code_texts.keys()):
            import_text += f"from .mayacmds_{first_letter} import *\n"
        with open(self.maya_dir / "__init__.py", "w+", encoding="UTF-8") as file:
            file.write("")
        with open(self.cmds_dir / "__init__.py", "w+", encoding="UTF-8") as file:
            v = autopep8.fix_code(import_text)
            file.write(v)

    @property
    def soup(self) -> BeautifulSoup:
        """
        Parses the stored HTML content into a BeautifulSoup object for easy manipulation and extraction.

        This property provides a convenient way to access and parse the HTML content of a Maya command's
        documentation. It utilizes BeautifulSoup to turn the raw HTML into a parseable tree structure,
        enabling efficient extraction and processing of the required information.

        Returns:
            BeautifulSoup: A BeautifulSoup object representing the parsed HTML content.
        """
        return BeautifulSoup(self.html_content, "html.parser")

    def getHTagContent(self, value: str) -> Tag | NavigableString | None:
        """
        Retrieves the content associated with a specific HTML anchor tag.

        This method searches for an anchor (`<a>`) tag with the given name attribute and then finds the content
        in its parent `<h2>` tag's next sibling. It's used to extract specific sections, such as examples or flags,
        from the HTML documentation of Maya commands.

        Parameters:
            value (str): The value of the 'name' attribute in the anchor tag to search for.

        Returns:
            Tag | NavigableString | None: The content of the next sibling of the parent `<h2>` tag of the found anchor,
            or None if no matching tag is found.
        """
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
        """
        Checks if the provided string consists only of whitespace characters.

        This utility method is used to determine if a given string is empty or contains only spaces,
        tabs, or newlines. It's helpful for validating the content extracted from HTML before processing it further.

        Parameters:
            text (str): The string to check.

        Returns:
            bool: True if the string is empty or only contains whitespace, False otherwise.
        """
        return text.isspace() if text else False

    def create_docstrings_example_texts(self) -> str:
        """
        Creates a formatted docstring section listing the flags and their descriptions.

        This method iterates over the argument data collected for a Maya command, formats each argument's information,
        and compiles them into a single string suitable for inclusion in a docstring. The information includes the flag name,
        type, properties, and its documentation.

        Returns:
            str: A formatted string containing the flags section for the docstring.
        """
        hExamples_content = self.getHTagContent(HTags.hExamples.value)
        if hExamples_content:
            hExamples_content_text = hExamples_content.get_text(strip=True)
            if not self.is_only_whitespace(hExamples_content_text):
                if '"""' in hExamples_content_text:
                    hExamples_content_text = hExamples_content_text.replace(r'"""', r"'''")

                return f"\n{self.option.common.html_contens.example_word}:\n---\n```\n{hExamples_content_text}\n```\n\n---"
        return ""

    def create_docstrings_flags_texts(self) -> str:
        """
        Generates a docstring section that lists all the flags and their properties for a Maya command.

        This method iterates through the argument data extracted from the command's documentation.
        It formats each flag's name, type, properties, and documentation into a structured docstring
        that can be included in the generated PYI files.

        Returns:
            str: A formatted docstring section listing all the flags and their details.
        """

        text = f"\n{self.option.common.html_contens.flags_word}:\n---\n\n"
        for argData in self.argument_data:
            types = ""
            for p in argData.properties:
                prop = self.option.common.html_contens.get_property_mode(p)
                types += f"{prop}, "
            types = types[:-2]
            text += f"""
---
{argData.longName}: {argData.type}
    {self.option.common.html_contens.properties_word}: {types}
    {argData.docs}
"""
        return text

    def create_function_text(self) -> str:
        """
        Constructs the function definition text for a Maya command.

        This method generates the complete function definition, including its arguments, return type hint,
        and docstrings. The docstrings include descriptions, examples, flag information, and a URL to the
        command's official documentation.

        Returns:
            str: The complete function definition as a string, ready to be included in a PYI file.
        """
        functionData = self.commands_data[self.function_name]
        docstrings = self.create_docstrings_example_texts()
        flags = self.create_docstrings_flags_texts()
        code = ""
        if self.option.common.html_contens.queryable in functionData.description:
            isQueryable = True
            if self.option.common.html_contens.not_queryable in functionData.description:
                isQueryable = False
            if isQueryable:
                code += "query: bool = ..., "

        for arguments in functionData.arguments:
            code += f"{arguments[0]}: {arguments[1]} = ..., "
        code = f'''def {self.function_name}(*args, {code[:-2]}) -> {self.return_typeHint}:
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
        """
        Extracts argument data from HTML tables in the command documentation.

        This method processes each table found in the command's HTML documentation, extracting data
        about the command's arguments, including their names, types, properties, and descriptions.
        The extracted data is stored in the argument_data attribute for further processing.
        """
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
        """
        Extracts and returns content found between specific H2 tags in the HTML documentation.

        This method uses regular expressions to find and return content located between
        the specified H2 tag and the next H2 tag in the HTML documentation. It's used to
        extract specific sections from the documentation for further processing.

        Parameters:
            start_h2_tag (str): The H2 tag from which to start the extraction.

        Returns:
            str | Any | None: The extracted content as a string, or None if no content is found.
        """
        pattern = re.compile(rf"{re.escape(start_h2_tag)}(.*?)(?=<h2>)", re.DOTALL)
        matches = re.search(pattern, self.html_content)
        return matches.group(1) if matches else None

    def extract_next_p_content(self) -> None:
        """
        Extracts and compiles the synopsis content from the HTML documentation of a Maya command.

        This method first extracts a segment of the HTML content that falls under the 'Synopsis' section
        and then parses it to compile a structured description. The method traverses through the HTML elements,
        concatenating the text content to form a comprehensive synopsis. The final synopsis is formatted and
        stored in the 'description' attribute of the class.

        Note:
            This method relies on specific HTML structure and id attributes (e.g., 'id="synopsis"') to identify
            and extract the relevant content. It also uses configured translator settings for specific text
            labels such as 'SYNOPSIS_WORD' and 'SYNOPSIS_NOTE_TEXT'.
        """
        allSynopsis = self.extract_between_specific_h2_tags(f'<h2><a name="hSynopsis">{self.option.common.html_contens.synopsis_word}</a></h2>')
        soup = BeautifulSoup(allSynopsis, "html.parser")
        docs = soup.get_text()
        synopsis = soup.find("p", {"id": "synopsis"})
        self.description = ""
        current_element = synopsis
        while current_element and current_element.name != "h2":
            self.description += str(current_element.get_text())
            current_element = current_element.find_next_sibling()
        note_text = self.option.common.html_contens.synopsis_note_text
        synopsis_description, command_description = docs.split(note_text)

        self.description = f"""{self.option.common.html_contens.synopsis_word}:
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
        """
        Extracts and returns a list of arguments and their types from the synopsis section.

        This method parses the synopsis section of the Maya command's documentation to extract arguments.
        It looks for `<code>` tags within the synopsis and then identifies each argument's flag and type.
        The method also checks if the argument type is present in the common Maya arguments configuration,
        and if so, uses the configured type.

        Returns:
            list[list[str]]: A list of lists, where each inner list contains the argument flag and its type.
        """
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
        """
        Retrieves the synopsis section from the HTML documentation of a Maya command.

        This property locates the 'Synopsis' section in the command's HTML documentation using a specific
        HTML structure and identifiers (e.g., an anchor tag with 'name' attribute as 'hSynopsis'). It returns
        the content immediately following this section, typically a paragraph, which contains the command's
        synopsis information.

        Returns:
            Tag | NavigableString | None: The BeautifulSoup tag or navigable string containing the synopsis,
            or None if the synopsis section is not found.
        """
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
        """
        Retrieves the content of the 'Return' section from the HTML documentation of a Maya command.

        This method searches for the 'Return' section in the command's HTML documentation, identified by an
        anchor tag with the name 'hReturn'. It then returns the content following this section, typically
        detailing the return values of the command.

        Returns:
            Tag | NavigableString | str: The content of the 'Return' section, or None if the section is not found.
        """
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
        """
        Extracts and returns the return type and description from a given table element.

        This method is used to parse return type information from a table in the 'Return' section of the command's
        documentation. It extracts the return type and its description, adjusting the type if it's listed in the
        common Maya arguments configuration.

        Parameters:
            table (Tag | NavigableString): The BeautifulSoup object representing the table to parse.

        Returns:
            tuple[str, str]: A tuple containing the return type and its description.
        """
        td_tags = table.find_all("td")
        if len(td_tags) > 1:
            td_texts = td_tags[1].get_text(strip=True)
        i_tag = table.find("i").text
        if i_tag in self.option.common.maya_argments:
            i_tag = self.option.common.maya_argments[i_tag]
        return i_tag, td_texts

    def getReturnData(self) -> None:
        """
        Extracts and processes the return data from the command's HTML documentation.

        This method retrieves the return type information from the documentation, parses it,
        and formats it into a structured form suitable for inclusion in the docstrings. It compiles
        the return types and their descriptions, updating the class attributes for further use in PYI file generation.
        """
        return_content = self.hReturn()
        self.return_typeHint = ""
        returns_texts: list[list[str] | str] = []
        if not isinstance(return_content, Tag):
            return_content_text = None
        else:
            return_content_text = return_content.text

        if return_content_text != self.option.common.html_contens.return_none_word:
            returns = []
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
            self.return_typeHint = "None"
        self.docstrings_text = ""
        if returns_texts != []:
            self.docstrings_text = f"{self.option.common.html_contens.return_word}:\n---\n\n"
            for returns_text in returns_texts:
                self.docstrings_text += f"\n    {returns_text[0]}: {returns_text[1]}"

    # @stop_watch
    def create_code_text(self) -> None:
        """
        Generates the complete code text for each Maya command.

        This method iterates through all the HTML files in the document root directory, extracts the necessary
        information (including return data, arguments, and descriptions), and creates the function definition text.
        The generated text is stored and organized for later use in PYI file export.
        """
        count = 0
        self.code_texts = {}
        length = 0
        for iter in self.document_root.iterdir():
            length += 1
        count = 0
        for iter in self.document_root.iterdir():
            # print(f"{length-count}/{length}")
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
        self.current_letter = self.first_letter
        self.export_pyi()

    def run(self) -> None:
        """
        Executes the complete process of generating PYI files for Maya commands.

        This method is the main entry point for the PYI file generation process. It ensures version compatibility,
        creates the function texts for all commands, and handles the export of the generated PYI files and
        the creation of '__init__.py' files.
        """
        self.versionCompatible()
        self.create_code_text()
        self.create_initpy()

    def versionCompatible(self) -> None:
        """
        Handles version-specific compatibility adjustments for the documentation.

        This method checks the specified version of the Maya documentation and performs necessary adjustments
        to ensure compatibility. For example, it handles specific file copying operations for Japanese documentation
        of Maya 2023.3.

        Note:
            Adjustments made by this method depend on the specific requirements of different versions of Maya documentation.
        """
        if self.option.maya.versioning == "2023.3" and self.option.common.language == "jp":
            import shutil

            source = self.document_root.parent.parent.with_name("contents") / self.option.maya.versioning / "workspaceControlState.content"
            target = self.document_root / "workspaceControlState.html"
            shutil.copy(target.as_posix(), source.as_posix())
