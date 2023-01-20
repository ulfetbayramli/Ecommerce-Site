from modeltranslation.translator import register, TranslationOptions
from .models import Category, Product, Product_version


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', )

@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'overview', 'details')  