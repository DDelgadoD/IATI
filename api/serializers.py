from rest_framework import serializers  # https://www.django-rest-framework.org/ (need to be added as app)

from shop.models import Product, Cap, Shirt, Cart, Item


class CapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cap
        exclude = ['polymorphic_ctype']


class ShirtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shirt
        exclude = ['polymorphic_ctype']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, obj):
        if isinstance(obj, Cap):
            return CapSerializer(obj, context=self.context).to_representation(obj)
        elif isinstance(obj, Shirt):
            return ShirtSerializer(obj, context=self.context).to_representation(obj)
        return super(ProductSerializer, self).to_representation(obj)


class ProductBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'description', 'picture_url', 'unitary_price']


class ItemSerializer(serializers.ModelSerializer):
    product = ProductBasicSerializer(read_only=True)

    class Meta:
        model = Item
        fields = ['product', 'quantity']


class CartSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, source='items_cart', read_only=True)

    class Meta:
        model = Cart
        fields = ['creation_date', 'total_products', 'items']
