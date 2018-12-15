from modeltranslation.translator import translator, TranslationOptions
from .models import Film
from .models import News

class FilmTranslationOptions(TranslationOptions):

    fields = ('film_name', 'description', 'content',)


class NewsTranslationOptions(TranslationOptions):

    fields = ('title', 'content',)

translator.register(Film, FilmTranslationOptions)
translator.register(News, NewsTranslationOptions)
