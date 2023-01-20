from rest_framework.generics import ListAPIView, ListCreateAPIView, CreateAPIView
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from Product.models import Product, Product_version
from Core.models import Subscriber
from Order.models import wishlist, basket, basket_item
from .serializers import (
                    ProductReadSerializer, 
                    ProductVersionSerializer,
                    SubscriberSerializer,
                    WishlistSerializer,
                    BasketSerializer,
                    BasketItemSerializer
                )
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

class ProductAPI(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductReadSerializer

class ProductVersionAPI(ListAPIView):
    queryset = Product_version.objects.all()
    serializer_class = ProductVersionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['product__category', 'color__name', 'product__manufacturer__name']
    
class SubscriberAPI(CreateAPIView):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer

class WishlistAPI(APIView):
    queryset = wishlist.objects.all()
    serializer_class = WishlistSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'delete']

    def get(self, request, *args, **kwargs):
        obj, created = wishlist.objects.get_or_create(user = request.user)
        serializer = self.serializer_class(obj)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        product_id = request.data.get('product')
        product = Product_version.objects.filter(pk=product_id).first()
        if product:
            wishlist1, created = wishlist.objects.get_or_create(user = request.user)
            wishlist2 = wishlist.objects.filter(user = request.user).first()
            wishlist2.product.add(product)
            message = {'success': True, 'message' : 'Product added to your wishlist.'}
            return Response(message, status = status.HTTP_201_CREATED)
        message = {'success' : False, 'message': 'Product not found.'}
        return Response(message, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        ProductID = request.data.get('product')
        if ProductID:
            user_wishlist =  wishlist.objects.filter(user = self.request.user).first()
            product = user_wishlist.product.filter(id = ProductID)
            user_wishlist.product.remove(product[0].id)
        return Response(status = status.HTTP_200_OK)

class BasketAPI(APIView):
    serializer_class = BasketSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'delete']

    def get(self, request, *args, **kwargs):
        obj, created = basket.objects.get_or_create(user = request.user, is_active = True)
        serializer = self.serializer_class(obj)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        quantity = request.data.get('quantity')
        product_id = request.data.get('product')
        product = Product_version.objects.filter(pk=product_id).first()
        if product:
            for_basket, created = basket_item.objects.get_or_create(product = product, user = request.user)
            basket2 = basket_item.objects.get(user = request.user, product = product)
            basket2.quantity += quantity
            basket2.save()
            basket1, created = basket.objects.get_or_create(user = request.user, is_active = True)
            basket1.items.add(basket2)   
            arr = []
            for item in basket1.items.all():
                serializer = BasketItemSerializer(item)
                arr.append(serializer.data)
            message = {'success': True, 'message' : 'Product added to your card.'}
            return Response(arr, status = status.HTTP_201_CREATED)
        message = {'success' : False, 'message': 'Product not found.'}
        return Response(message, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        ProductID = request.data.get('product')
        if ProductID:
            user_basket = basket_item.objects.get(product = ProductID, user = request.user)
            user_basket.delete()
        return Response(status = status.HTTP_200_OK)

