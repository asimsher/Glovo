from .models import *
from rest_framework import serializers



class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'status']


class UserProfileClientSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username']


class CategoryListSerializer( serializers.ModelSerializer ):
    class Meta:
        model = Category
        fields = ['id', 'category_name']


class CategorySimpleSerializer( serializers.ModelSerializer ):
    class Meta:
        model = Category
        fields = ['category_name']


class ProductListSerializer( serializers.ModelSerializer ):
    class Meta:
        model = Product
        fields = ['product_name', 'product_image', 'description', 'price']


class ProductDetailSerializer( serializers.ModelSerializer ):
    class Meta:
        model = Product
        fields = ['id', 'product_name', 'product_image', 'description', 'price', 'store']


class ComboListSerializer( serializers.ModelSerializer ):

    class Meta:
        model = Combo
        fields = ['combo_name', 'combo_image', 'description', 'price']



class ComboDetailSerializer( serializers.ModelSerializer ):
    class Meta:
        model = Combo
        fields = ['id', 'combo_name', 'combo_image', 'description', 'price', 'store']


class ContactSerializer( serializers.ModelSerializer ):
    class Meta:
        model = Contact
        fields = ['title', 'contact_number', 'social_network']


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class CartItemRSerializer( serializers.ModelSerializer ):
    class Meta:
        model = CartItem
        fields = '__all__'


class OrderSerializer( serializers.ModelSerializer ):
    class Meta:
        model = Order
        fields = '__all__'


class CourierSerializer( serializers.ModelSerializer ):
    class Meta:
        model = Courier
        fields = '__all__'



class StoreReviewSimpleSerializers(serializers.ModelSerializer):
    client = UserProfileClientSerializers(read_only=True)
    created_date = serializers.DateTimeField(format('%d-%m-%Y %H:%M'))

    class Meta:
        model = StoreReview
        fields = ['client', 'text', 'stars', 'client', 'created_date']


class StoreReviewSerializers(serializers.ModelSerializer):
    created_date = serializers.DateTimeField(format('%d-%m-%Y %H:%M'))

    class Meta:
        model = StoreReview
        fields = '__all__'


class CourierRatingSerializer( serializers.ModelSerializer ):
    class Meta:
        model = CourierRating
        fields = '__all__'


class StoreListSerializer(serializers.ModelSerializer):
    category = CategorySimpleSerializer()

    class Meta:
        model = Store
        fields = ['id', 'store_name', 'store_image', 'category']


class StoreDetailSerializer(serializers.ModelSerializer):
    category = CategorySimpleSerializer()
    owner = UserProfileSimpleSerializer()
    contacts = ContactSerializer(many=True, read_only=True)
    product_list = ProductListSerializer(many=True, read_only=True)
    combo_list = ComboListSerializer(many=True, read_only=True)
    store_review = StoreReviewSerializers(many=True, read_only=True)

    class Meta:
        model = Store
        fields = ['store_name', 'store_image', 'category', 'description',
                  'address', 'owner', 'contacts', 'product_list', 'combo_list', 'store_review']


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'


class CategoryDetailSerializer(serializers.ModelSerializer):
    store_list = StoreListSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['category_name', 'store_list']



