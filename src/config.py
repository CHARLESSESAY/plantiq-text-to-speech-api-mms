from dataclasses import dataclass

@dataclass
class LanguageData:
    name: str
    code: str
    model: str

LanguageModel = [
    LanguageData(name="kri", code="kri", model="facebook/mms-tts-kri"),
    LanguageData(name="men", code="men", model="facebook/mms-tts-men"),
    LanguageData(name="tem", code="tem", model="facebook/mms-tts-tem"),
    LanguageData(name="eng", code="eng", model="facebook/mms-tts-eng"),
]
