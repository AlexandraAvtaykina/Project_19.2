from django.urls import path
from catalog.views import contacts, ProductDetailView
from .apps import CatalogConfig
from .views import ProductListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product')
]
