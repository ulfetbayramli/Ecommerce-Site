from django.urls import path
from .views import ProductListView, ProductDetailView

urlpatterns = [
    path('product/<int:pk>/', ProductDetailView.as_view(), name = "product_detail"),
    path('product_list/', ProductListView.as_view(), name = "product_list"),
]