from dataclasses import dataclass

@dataclass
class Language:
    name: str
    code: str
    model: str

LanguageModel = [
    Language(name="Krio", code="kri", model="facebook/mms-tts-kri"),
    Language(name="Mende", code="men", model="facebook/mms-tts-men"),
    Language(name="Temne", code="tem", model="facebook/mms-tts-tem"),
    Language(name="English", code="eng", model="facebook/mms-tts-eng"),
]
