from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator

from online_delivery.models import Product, ProductCategory

def add_numbers(a: int, b: int) -> int:
    return a + b

def index(request):
    products = Product.objects.all()
    paginator = Paginator(products, 15)
    page = request.GET.get("page")
    page_obj = paginator.get_page(page)
    context = {
        "page_obj": page_obj
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
    paginate_by = 15
    order_by = 'id'


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context["product_counts"] = [n for n in range(1, 11)]
        return context



