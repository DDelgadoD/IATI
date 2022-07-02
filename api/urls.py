from django.urls import path
from .views import ProductApiView, CartApiView

urlpatterns = [
    path('product_list/', ProductApiView.as_view()),
    path('add_to_cart/<int:product_id>', CartApiView.as_view()),
    path('cart/<str:creation_date>', CartApiView.as_view()),
]
