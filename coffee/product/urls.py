from django.urls import path
from product import views


app_name = 'product'
urlpatterns = [
    path('', views.product, name='product'),
    path('productCreate/', views.productCreate, name='productCreate'),
    path('productRead/<int:productId>/', views.productRead, name='productRead'),
    path('productUpdate/<int:productId>/', views.productUpdate, name='productUpdate'),
    path('productDelete/<int:productId>/', views.productDelete, name='productDelete'),
    path('productLike/<int:productId>/', views.productLike, name='productLike'),
    path('commentCreate/<int:productId>/', views.commentCreate, name='commentCreate'),
    path('commentDelete/<int:commentId>/', views.commentDelete, name='commentDelete'),
    path('commentUpdate/<int:commentId>/', views.commentUpdate, name='commentUpdate'),
    path('productOrder/',views.productOrder,name='productOrder'),
    
]