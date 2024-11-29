from django.shortcuts import render
from django.views.generic import ListView, DetailView

from online_delivery.models import Product, ProductCategory

def add_numbers(a: int, b: int) -> int:
    return a + b

def index(request):
    context = {
        "products": Product.objects.all(),
    }
    
    return render(request, "online_delivery/index.html", context=context)


class CategoriesView(ListView):
    model = ProductCategory

    def get_queryset(self):
        queryset = ProductCategory.objects.all()
        return queryset


class CategoriesDetailView(DetailView):
    model = ProductCategory

    def get_context_data(self, **kwargs):
        context = super(CategoriesDetailView, self).get_context_data(**kwargs)
        context["products"] = Product.objects.filter(category_id=self.object.id)
        return context


class ProductsListView(ListView):
    model = Product
    context_object_name = "products"
    paginate_by = 50


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context["product_counts"] = [n for n in range(1, 11)]
        return context
