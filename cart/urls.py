from django.urls import path
from .views import cart, add_cart, remove_cart, remove, checkout

urlpatterns = [
    path('', cart , name = 'cart'),
    path('add_cart/<int:product_id>', add_cart, name = 'add_cart'),
    path('remove_cart/<int:product_id>/<int:cart_item_id>', remove_cart, name = 'remove_cart'),
    path('remove/<int:product_id>/<int:cart_item_id>', remove, name = "remove"),
    path('checkout/', checkout, name= "checkout")

]