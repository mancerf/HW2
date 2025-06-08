from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from catalog.models import Category, Product


# Create your views here.
def home(requests):
    return render(requests, template_name='catalog/home.html')


def contacts(requests):
    return render(requests, template_name='catalog/contacts.html')


class ProductListView(ListView):
    model = Product
    # catalog/product_list.html


# def product_list(requests):
#     products = Product.objects.all()
#     context = {"products": products}
#     return render(requests, template_name='products_list.html', context = context)
#
class ProductDetailView(DetailView):
    model = Product
# def product_detail(requests,pk):
#     products = get_object_or_404(Product, pk=pk)
#     context = {"product": products}
#     return render(requests, template_name='product_detail.html', context=context)
