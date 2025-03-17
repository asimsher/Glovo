from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin,  TranslationInlineModelAdmin


class ContactInline(admin.TabularInline, TranslationInlineModelAdmin):
    model = Contact
    extra = 1


class StoreInline(admin.TabularInline,TranslationInlineModelAdmin):
    model = Store
    extra = 1


class ProductInline(admin.TabularInline, TranslationInlineModelAdmin):
    model = Product
    extra = 1


class ComboInline(admin.TabularInline, TranslationInlineModelAdmin):
    model = Combo
    extra = 1


@admin.register(Store)
class AllAdmin(TranslationAdmin):
    inlines = (ComboInline, ProductInline, ContactInline)

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Category, Contact, Product, Combo)
class CategoryAdmin(TranslationAdmin):

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }



admin.site.register(UserProfile)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(Courier)
admin.site.register(StoreReview)
admin.site.register(CourierRating)