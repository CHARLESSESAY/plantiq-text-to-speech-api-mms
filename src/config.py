from dataclasses import dataclass
from typing import List

@dataclass
class LanguageModel:
    name: str
    code: str
    model: str

SUPPORTED_LANGUAGES: List[LanguageModel] = [
    LanguageModel(name="English", code="eng", model="facebook/mms-tts-eng"),
    LanguageModel(name="Krio", code="kri", model="facebook/mms-tts-kri"),
    LanguageModel(name="Mende", code="men", model="facebook/mms-tts-men"),
    LanguageModel(name="Temne", code="tem", model="facebook/mms-tts-tem"),
]
