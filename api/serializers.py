from rest_framework import serializers
from Product.models import Product, Product_version, Category, Manufacturer, Color
from Core.models import Subscriber
from Order.models import basket_item, wishlist, basket
from verify_email import verify_email

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category 
        fields = [
            'id',
            'name',
            'is_navbar',
            'p_category'
        ]

class ManufacturerReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Manufacturer
        fields = [
            'name'
        ]

class ColorReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Color
        fields = [
            'name'
        ]

class ProductReadSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    detail_url = serializers.SerializerMethodField()
    manufacturer = ManufacturerReadSerializer()
    
    class Meta:
        model = Product 
        fields = [
            'id', 
            'name', 
            'overview',
            'price', 
            'in_sale',
            'discount', 
            'new_price',
            'manufacturer',
            'details', 
            'category',
            'detail_url'
        ]

    def get_detail_url(self, obj):
        return obj.get_absolute_url()

class ProductVersionSerializer(serializers.ModelSerializer):
    product = ProductReadSerializer()
    color = ColorReadSerializer()

    class Meta:
        model = Product_version
        fields = [
            'id', 
            'color',
            'cover_image',
            'product',
            'quantity',
            'review_count',
            'read_count'
        ]

class WishlistSerializer(serializers.ModelSerializer):
    product = ProductVersionSerializer(many=True)

    class Meta:
        model = wishlist
        fields = [
            'user',
            'product'
        ]

class BasketSerializer(serializers.ModelSerializer):

    class Meta:
        model = basket
        fields = [
            'user',
            'items',
            'is_active'
        ]

class BasketItemSerializer(serializers.ModelSerializer):
    product = ProductVersionSerializer()

    class Meta:
        model = basket_item
        fields = ['user', 'product', 'quantity']

class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = [
            'email'
        ]

    def create(self, validated_data):
        if verify_email(validated_data['email']):
            return super().create(validated_data)