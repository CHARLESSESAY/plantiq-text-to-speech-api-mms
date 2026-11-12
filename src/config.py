from dataclasses import dataclass

@dataclass
class LanguageData:
    name: str
    code: str

    @property
    def value(self):
        return self.code

LanguageModel = [
    LanguageData(name="kri", code="kri"),
    LanguageData(name="men", code="men"),
    LanguageData(name="tem", code="tem"),
]
