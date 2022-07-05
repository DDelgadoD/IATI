from datetime import datetime
from json2html import *
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework import generics  # https://www.django-rest-framework.org/ (need to be added as app)
from rest_framework.response import Response
from rest_framework.views import APIView
from shop.models import Product, Cart, Item
from .serializers import ProductSerializer, CartSerializer


class ProductApiView(generics.ListAPIView):
    http_method_names = ['get']
    queryset = Product.objects.all().order_by('polymorphic_ctype')
    serializer_class = ProductSerializer


class CartApiView(generics.UpdateAPIView):
    serializer_class = CartSerializer
    http_method_names = ['get', 'post']

    def post(self, request, product_id, quantity=1, cart=datetime.now().strftime('%Y-%m-%d')):
        # if the quantity and cart data comes from request JSON it overrides url
        cart = datetime.strptime(self.request.POST.get('cart', cart), '%Y-%m-%d').date()
        quantity = int(self.request.POST.get('quantity', quantity))

        product = get_object_or_404(Product, pk=product_id)
        cart, created = Cart.objects.get_or_create(creation_date=cart)
        item, created = Item.objects.get_or_create(product=product, cart=cart, defaults={'quantity': quantity})

        if not created:
            item.quantity += quantity

        item.save()
        # If product is not found the response will be 404 not found because these we don't need to do nothing
        return Response(CartSerializer(cart, context=self.get_serializer_context()).data)

    def get(self, request, creation_date):
        cart = get_object_or_404(Cart, creation_date=datetime.strptime(creation_date, '%Y-%m-%d').date())
        # If cart is not found the response will be 404 not found because these we don't need to do nothing
        return Response(CartSerializer(cart, context=self.get_serializer_context()).data)

    def get_serializer_context(self):
        context = {'request': self.request}
        return context


class CheckoutApiView(APIView):
    serializer_class = CartSerializer
    http_method_names = ['get']

    def get(self, request, creation_date):
        cart = get_object_or_404(Cart, creation_date=datetime.strptime(creation_date, '%Y-%m-%d').date())

        subject = "Tu compra en IATI SHOP"
        cart_data = CartSerializer(cart, context=self.get_serializer_context()).data
        html_table = json2html.convert(json=cart_data)
        message_hi = "Este es un resumen de tu compra:"
        message_bye = "Gracias por tu compra!"
        message_sign = "IATI SHOP"
        mail_msg = f"<p>{message_hi}</p>" + html_table + f"<p>{message_bye}</p>" + f"<p>{message_sign}</p>"
        from_ = "iati_shop@example.es"
        to_ = "user@example.es"

        send_mail(
            subject,
            mail_msg,
            from_,
            [to_],
            fail_silently=False,
        )

        # Empty the shopping cart
        Item.objects.filter(cart=cart).delete()

        return Response({"Email sent:": {
            'subject': subject,
            'message': [message_hi, cart_data, message_bye, message_sign],
            "from": from_,
            "to": to_}
        })

    def get_serializer_context(self):
        context = {'request': self.request}
        return context
