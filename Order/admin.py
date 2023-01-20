from django.contrib import admin
from .models import billing_addresses, shipping_addresses, address_information, basket, order, wishlist, basket_item

admin.site.register(order)
admin.site.register(basket)
admin.site.register(basket_item)
admin.site.register(billing_addresses)
admin.site.register(shipping_addresses)
admin.site.register(address_information)
admin.site.register(wishlist)