from django.views.generic import ListView
from .models import Product


class ProductView (ListView):
    model = Product
    template_name = 'shop/home.html'
    queryset = Product.objects.all().order_by('polymorphic_ctype')
    context_object_name = 'products'
