from abc import ABC, abstractmethod

AbstractField = lambda: property(abstractmethod(lambda s: s))


class Translater(ABC):
    SYNOPSIS_WORD: str = AbstractField()
    SYNOPSIS_NOTE_TEXT: str = AbstractField()
    FLAGS_WORD: str = AbstractField()
    RETURN_WORD: str = AbstractField()
    RETURN_NONE_WORD: str = AbstractField()
    EXAMPLE_WORD: str = AbstractField()
    PROPERTIES_WORD: str = AbstractField()

    @abstractmethod
    def property_mode(self, prop: str) -> str:
        pass


class En(Translater):
    SYNOPSIS_WORD: str = "Synopsis"
    SYNOPSIS_NOTE_TEXT: str = "Note: Strings representing object names and arguments must be separated by commas. This is not depicted in the synopsis."
    FLAGS_WORD: str = "Flags"
    RETURN_WORD: str = "Return"
    RETURN_NONE_WORD: str = "None"
    EXAMPLE_WORD: str = "Example"
    PROPERTIES_WORD: str = "properties"

    def property_mode(self, prop: str) -> str:
        return prop


class Jp(Translater):
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
