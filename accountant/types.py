from enum import StrEnum


class Currency(StrEnum):
    EUROS = "euros"
    DOLLARS = "dollars"


class Download(StrEnum):
    PDF = "pdf"
    HTML = "html"


class Language(StrEnum):
    EN = "en"
