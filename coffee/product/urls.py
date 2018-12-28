from django.urls import path
from product import views


app_name = 'product'
urlpatterns = [
    path('', views.product, name='product'),
    path('productCreate/', views.productCreate, name='productCreate'),
    path('productRead/<int:productId>/', views.productRead, name='productRead'),
    path('productUpdate/<int:productId>/', views.productUpdate, name='productUpdate'),
    path('productDelete/<int:productId>/', views.productDelete, name='productDelete'),
    
]