from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from Product.models import Product, Product_version

class address_information(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    telephone = models.CharField(max_length=15)
    email = models.EmailField()
    street_address = models.CharField(max_length=150)
    country = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    province = models.CharField(max_length=150, null=True, blank=True)
    is_billing = models.BooleanField(default=False)
    is_shipping = models.BooleanField(default=False)  
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    zip = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.first_name}'s address information"

    class Meta:
        verbose_name = "Address Information"
        verbose_name_plural = "Address Informations"

class billing_addresses(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    telephone = models.CharField(max_length=15)
    email = models.EmailField()
    street_address = models.CharField(max_length=150)
    country = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    province = models.CharField(max_length=150, null=True, blank=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    zip = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.first_name}'s billing address"

    class Meta:
        verbose_name = "Billing Address"
        verbose_name_plural = "Billing Addresses"

class shipping_addresses(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    telephone = models.CharField(max_length=15)
    email = models.EmailField()
    street_address = models.CharField(max_length=150)
    country = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    province = models.CharField(max_length=150, null=True, blank=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    zip = models.CharField(max_length=10)
     
    def __str__(self):
        return f"{self.first_name}'s shipping address"

    class Meta:
        verbose_name = "Shipping Address"
        verbose_name_plural = "Shipping Addresses"

class wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="user_wishlist")
    product = models.ManyToManyField(Product_version, related_name="products_wishlist")

    def __str__(self):
        return f"{self.user}'s wishlist"

    class Meta:
        verbose_name = "Wishlist"
        verbose_name_plural = "Wishlists"   

class basket_item(models.Model):
    quantity = models.PositiveIntegerField(default=0)
    product = models.ForeignKey(Product_version, on_delete=models.CASCADE, null=True, blank=True, related_name="product_basket_item")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="user_basket_item")

    def __str__(self):
        return f"{self.user.username}'s basket item"

    def get_subtotal(self):
        if self.product.product.in_sale:
            subtotal = self.product.product.new_price*self.quantity
        else:
            subtotal = self.product.product.price*self.quantity
        return subtotal

    class Meta:
        verbose_name = "Basket Item"
        verbose_name_plural = "Basket Items"

class basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="user_basket")
    items = models.ManyToManyField(basket_item, related_name="basket_items")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username}'s basket"

    class Meta:
        verbose_name = "Basket"
        verbose_name_plural = "Baskets"

class order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_order")
    address = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user.username}'s order"

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
