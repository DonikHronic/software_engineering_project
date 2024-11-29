from django.urls import path

from online_delivery import views

urlpatterns = [
    path('', views.index, name='index'),
    path('categories/', views.CategoriesView.as_view(), name='categories'),
    path('categories/<int:pk>', views.CategoriesDetailView.as_view(), name='category-detail'),
    path('products/', views.ProductsListView.as_view(), name='products'),
    path('products/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
]
