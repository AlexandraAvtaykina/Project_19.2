from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.views import contacts, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView
from .apps import CatalogConfig
from .views import ProductListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete'),
]
