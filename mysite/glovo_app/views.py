from .filters import CategoryFilter, ProductFilter, ComboFilter
from .serializers import *
from .models import *
from rest_framework import viewsets, generics
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import CheckOwner, CheckUserReview, CheckStoreOwner
from .pagination import *

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)

class StoreListAPIView(generics.ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter ]
    filterset_fields = ['category']
    search_fields = ['store_name']
    pagination_class = StorePagination

class StoreListOwnerAPIView( generics.ListAPIView ):
    queryset = Store.objects.all()
    serializer_class = StoreListSerializer

    def get_queryset(self):
        return Store.objects.filter(owner=self.request.user)


class StoreDetailAPIView(generics.RetrieveAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreDetailSerializer


class StoreCreateOwnerAPIView(generics.CreateAPIView):
    serializer_class = StoreSerializer
    permission_classes = [CheckOwner]

class StoreDetailUpdateDestroyOwnerAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [CheckOwner, CheckStoreOwner]

class CategoryAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CategoryFilter

class CategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer



class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['product_name']
    ordering_fields = ['price']
    pagination_class = ProductPagination

class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer


class ComboListAPIView(generics.ListAPIView):
    queryset = Combo.objects.all()
    serializer_class = ComboListSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = ComboFilter
    ordering_fields = ['price']



class ComboDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Combo.objects.all()
    serializer_class = ComboDetailSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemRSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class CourierViewSet(viewsets.ModelViewSet):
    queryset = Courier.objects.all()
    serializer_class = CourierSerializer


class StoreReviewListAPIView(generics.CreateAPIView):
    serializer_class = StoreReviewSerializers
    permission_classes = [CheckUserReview]
class StoreReviewDetailAPIView(generics.RetrieveAPIView):
    queryset = StoreReview.objects.all()
    serializer_class = StoreReviewSimpleSerializers


class CourierRatingSerializer(serializers.ModelSerializer):
    queryset = CourierRating.objects.all()
    serializer_class = CourierRatingSerializer
    