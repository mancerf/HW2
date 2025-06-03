from django.shortcuts import render, get_object_or_404


from catalog.models import Category, Product


# Create your views here.
def home(requests):
    return render(requests, template_name='catalog/home.html')


def contacts(requests):
    return render(requests, template_name='catalog/contacts.html')


def product_list(requests):
    products = Product.objects.all()
    context = {"products": products}
    return render(requests, template_name='products_list.html', context = context)


def product_detail(requests,pk):
    products = get_object_or_404(Product, pk=pk)
    context = {"product": products}
    return render(requests, template_name='product_detail.html', context=context)
