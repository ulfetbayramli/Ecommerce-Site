from django.urls import path
from .views import AddressInfo, BillingInfo, ShippingInfo, CheckoutView, BasketView, WishlistView

urlpatterns = [
    path('address_info/', AddressInfo.as_view(), name = "address_info"),
    path('billing_info/', BillingInfo.as_view(), name = "billing_info"),
    path('shipping_info/', ShippingInfo.as_view(), name = "shipping_info"),
    path('checkout/', CheckoutView.as_view(), name = "checkout"),
    path('shopping_cart/', BasketView.as_view(), name = "shopping_cart"),
    path('  ', WishlistView.as_view(), name = 'wishlist'),
]