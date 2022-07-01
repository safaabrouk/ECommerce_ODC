from django.urls import path
from Apps.products.views import new_product, product_details, product_list

app_name ='products'

urlpatterns = [
    path('produits/', product_list ,name='product_list'),
    path('produit/<int:id>', product_details ,name='product_details'),
    path('produit/add', new_product ,name='new_product'),
]