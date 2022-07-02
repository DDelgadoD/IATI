from datetime import datetime

from rest_framework import generics  #https://www.django-rest-framework.org/ (need to be added as app)
from rest_framework.response import Response

from shop.models import Product, Cart, Item
from .serializers import ProductSerializer, CartSerializer
from django.shortcuts import get_object_or_404


class ProductApiView(generics.ListAPIView):
    queryset = Product.objects.all().order_by('polymorphic_ctype')
    serializer_class = ProductSerializer


class CartApiView(generics.UpdateAPIView):
    serializer_class = CartSerializer

    @staticmethod
    def post(request, product_id):
        default_time = datetime.now().strftime('%Y-%m-%d')
        creation_date = datetime.strptime(request.POST.get('cart', default_time), '%Y-%m-%d').date()

        quantity = int(request.POST.get('quantity', '1'))

        product = get_object_or_404(Product, pk=product_id)
        cart, created = Cart.objects.get_or_create(creation_date=creation_date)
        item, created = Item.objects.get_or_create(product=product, cart=cart,  defaults={'quantity': 1})

        if not created:
            item.quantity += quantity
        item.save()

        return Response(CartSerializer(cart).data)

    @staticmethod
    def get(request, creation_date):
        cart = get_object_or_404(Cart, creation_date=datetime.strptime(creation_date, '%Y-%m-%d').date())
        return Response(CartSerializer(cart).data)

