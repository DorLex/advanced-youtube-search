from enum import Enum


class RelevanceLanguagesEnum(str, Enum):
    en = 'en'
    ru = 'ru'


class ContentTypesEnum(str, Enum):
    video = 'video'
    playlist = 'playlist'


class UrlTemplatesEnum(str, Enum):
    video = 'https://www.youtube.com/watch?v='
    playlist = 'https://www.youtube.com/playlist?list='
