from products.views import product,product_create,rawform_create,rproduct,product_list
from django.urls import path
app_name='product'
urlpatterns = [
    path('product/<int:my_id>/', product, name='product'),
    path('rproduct/<int:my_id>/', rproduct, name='rproduct'),
    path('create/', product_create, name='create'),
    path('rcreate/', rawform_create, name='rcreate'),
    path('product_list/',product_list , name='product_list'),
    ]