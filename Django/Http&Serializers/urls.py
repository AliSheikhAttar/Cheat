from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('products/', views.product_list),
    path('products/<int:id>/', views.product_detail),#notation as indicates to input only in int
    path('collections/', views.collection_list),
    path('collections/<int:pk>/', views.collection_detail, name='collection-detail'),#for hyperlink to related colloction object, pk for look up key=> a convention in urls by django rest 
]