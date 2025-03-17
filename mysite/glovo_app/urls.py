from .views import *
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UserProfileViewSet, basename='users')
router.register(r'cart', CartViewSet, basename='carts')
router.register(r'cart_item', CartItemViewSet, basename='items')


urlpatterns = [
    path('', include(router.urls)),
    path('store/', StoreListAPIView.as_view(), name='store_list'),
    path('store/<int:pk>/', StoreDetailAPIView.as_view(), name='store_detail' ),
    path('store_list/', StoreListOwnerAPIView.as_view(), name='store_list_owner' ),
    path( 'store_list/<int:pk>/', StoreDetailUpdateDestroyOwnerAPIView.as_view(),
          name='store_list_edit' ),
    path('store/create/', StoreCreateOwnerAPIView.as_view(), name='store_create' ),
    path('category/', CategoryAPIView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryDetailAPIView.as_view(), name='category_detail' ),
    path('product/', ProductListAPIView.as_view(), name='product_list' ),
    path('product/<int:pk>/', ProductDetailAPIView.as_view(), name='product_detail' ),
    path('combo/', ComboListAPIView.as_view(), name='combo_list' ),
    path('combo/<int:pk>/', ComboDetailAPIView.as_view(), name='combo_detail' ),
    path('review/', StoreReviewListAPIView.as_view(), name='review_create' ),
    path('store_review/<int:pk>/', StoreReviewDetailAPIView.as_view(), name='combo_detail' ),
]