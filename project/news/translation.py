from .models import Category, Record
# importiruem dekoraror dlya perevoda i class nastroek, ot kotorogo budem nasledovatsya
from modeltranslation.translator import register, TranslationOptions


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', )  # ukazivaem polya kotorie budem perevodit


# registriruem modeli dlya perevoda
@register(Record)
class RecordlTranslationOptions(TranslationOptions):
    fields = ('title', 'full_text', )
