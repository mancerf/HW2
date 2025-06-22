from catalog.models import Product
from django.shortcuts import render, get_object_or_404
from .forms import ProductForm
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy, reverse


# Create your views here.
def home(requests):
    return render(requests, template_name='catalog/home.html')


def contacts(requests):
    return render(requests, template_name='catalog/contacts.html')

    # catalog/product_list.html


# def product_list(requests):
#     products = Product.objects.all()
#     context = {"products": products}
#     return render(requests, template_name='products_list.html', context = context)
#


# def product_detail(requests,pk):
#     products = get_object_or_404(Product, pk=pk)
#     context = {"product": products}
#     return render(requests, template_name='product_detail.html', context=context)


class ProductListView(ListView):
    model = Product
    template_name = "catalog/product_list.html"
    context_object_name = "products"

    def get_queryset(self):
        return Product.objects.filter(price__gt=0).order_by('price')


class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/product_detail.html"


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:product_list")


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:product_list")

    def get_success_url(self):
        return reverse("catalog:product_detail", args=[self.kwargs.get("pk")])


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")
