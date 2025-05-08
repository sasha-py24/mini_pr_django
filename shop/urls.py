from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('product/', views.ProductCreationView.as_view(), name='product'),
    path('catalog/', views.ProductCatalog.as_view(), name='catalog'),


]