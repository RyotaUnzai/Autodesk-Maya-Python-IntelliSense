from abc import ABC, abstractmethod


class Translator(ABC):
    @property
    @abstractmethod
    def SYNOPSIS_WORD(self) -> str:
        pass

    @property
    @abstractmethod
    def SYNOPSIS_NOTE_TEXT(self) -> str:
        pass

    @property
    @abstractmethod
    def FLAGS_WORD(self) -> str:
        pass

    @property
    @abstractmethod
    def RETURN_WORD(self) -> str:
        pass

    @property
    @abstractmethod
    def RETURN_NONE_WORD(self) -> str:
        pass

    @property
    @abstractmethod
    def EXAMPLE_WORD(self) -> str:
        pass

    @property
    @abstractmethod
    def PROPERTIES_WORD(self) -> str:
        pass

    @abstractmethod
    def property_mode(self, prop: str) -> str:
        pass


class En(Translator):
    SYNOPSIS_WORD: str = "Synopsis"
    SYNOPSIS_NOTE_TEXT: str = "Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis."
    FLAGS_WORD: str = "Flags"
    RETURN_WORD: str = "Return"
    RETURN_NONE_WORD: str = "None"
    EXAMPLE_WORD: str = "Example"
    PROPERTIES_WORD: str = "properties"

    def property_mode(self, prop: str) -> str:
        return prop


class Jp(Translator):
    SYNOPSIS_WORD: str = "概要"
    SYNOPSIS_NOTE_TEXT: str = "注: オブジェクトの名前と引数を表す文字列は、カンマで区切る必要があります。これはシノプシスに示されていません。"
    FLAGS_WORD: str = "フラグ"
    RETURN_WORD: str = "戻り値"
    RETURN_NONE_WORD: str = "なし"
    EXAMPLE_WORD: str = "例"
    PROPERTIES_WORD: str = "プロパティ"

    def property_mode(self, prop: str) -> str:
        if prop == "create":
            return "作成"
        elif prop == "query":
            return "照会"
        elif prop == "edit":
            return "編集"
        elif prop == "multiuse":
            return "複数"
        else:
            return prop
