from django_filters import FilterSet
from .models import Category, Product, Combo


class CategoryFilter(FilterSet):
    class Meta:
        model = Category
        fields = {
            'category_name': ['exact'],
        }


class ProductFilter(FilterSet):
    class Meta:
        model = Product
        fields = {
            'product_name': ['exact'],
            'price': ['gt', 'lt'],
        }


class ComboFilter(FilterSet):
    class Meta:
        model = Combo
        fields = {
            'combo_name': ['exact'],
            'price': ['gt', 'lt'],
        }