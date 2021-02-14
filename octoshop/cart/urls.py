
from django.urls import path
from . import views
app_name = 'cart'


urlpatterns = [
    # path('produits/', ProductsView.as_view(), name='products'),
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('update/<int:product_id>/', views.cart_update, name='cart_update'),


]
