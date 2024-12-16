from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator

from online_delivery.models import Product, ProductCategory, Order
from online_delivery.models import BaseUser


def index(request):
    products = Product.objects.all()
    paginator = Paginator(products, 15)
    page = request.GET.get("page")
    page_obj = paginator.get_page(page)
    context = {"page_obj": page_obj}

    return render(request, "online_delivery/index.html", context=context)


def register(request):
    if request.method == "POST":
        username = request.POST.get("username", None)
        email = request.POST.get("email", None)
        password = request.POST.get("password", None)
        user = BaseUser.objects.create(username=username, email=email)
        user.set_password(password)
        user.save()
    return redirect("index")


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
    order_by = "id"


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context["product_counts"] = [n for n in range(1, 11)]
        return context


class OrderListView(ListView):
    model = Order
    paginate_by = 15


class OrderDetailView(DetailView):
    model = Order


def create_order(request):
    if request.method == "POST":
        product_id = request.POST.get("product_id", None)
        count = request.POST.get("count")
        product = Product.objects.get(id=product_id)
        order = Order.objects.create(
            product=product, user=request.user, price=100, product_count=count
        )
        order.save()
    return redirect("orders")
