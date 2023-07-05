from django.contrib import admin
from .models import Record, Category
# importiruem model adminki
from modeltranslation.admin import TranslationAdmin


# Register your models here.

# registriruem modeli dlya perevoda v adminke
class CategoryAdmin(TranslationAdmin):
    model = Category


class RecordlAdmin(TranslationAdmin):
    model = Record


admin.site.register(Record)
admin.site.register(Category)

