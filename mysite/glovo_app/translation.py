from .models import Category, Store, Contact, Product, Combo
from modeltranslation.translator import TranslationOptions,register


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name',)


@register(Store)
class StoreTranslationOptions(TranslationOptions):
    fields = ('store_name', 'description', 'address')


@register(Contact)
class ContactTranslationOptions(TranslationOptions):
    fields = ('title', )


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('product_name', 'description')


@register(Combo)
class ComboTranslationOptions(TranslationOptions):
    fields = ('combo_name', 'description')