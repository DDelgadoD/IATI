from django.urls import path
from .views import ProductApiView, CartAddView, CartApiView, CheckoutApiView

urlpatterns = [
    path('product_list/', ProductApiView.as_view(), name='product_list'),
    path('add_to_cart/<int:product_id>', CartAddView.as_view()),
    path('add_to_cart/<int:product_id>/<int:quantity>', CartAddView.as_view()),
    path('add_to_cart/<int:product_id>/<str:cart>', CartAddView.as_view()),
    path('add_to_cart/<int:product_id>/<int:quantity>/<str:cart>', CartAddView.as_view()),
    path('cart/<str:creation_date>', CartApiView.as_view(), name='cart'),
    path('checkout/<str:creation_date>', CheckoutApiView.as_view(), name='checkout'),
]
