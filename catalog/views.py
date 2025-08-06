from django.core.exceptions import PermissionDenied

from catalog.models import Product, Category
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProductForm, ProductModeratorForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required
from catalog.services import get_product_from_cache, get_products_by_category

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
        category_name = self.request.GET.get('category_name')
        return get_product_from_cache(category_name)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()  # Добавляем список категорий в контекст
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/product_detail.html"


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:product_list")
    permission_required = "catalog.can_unpublish_product"

    def get_success_url(self):
        return reverse("catalog:product_detail", args=[self.kwargs.get("pk")])

    def get_form_class(self):
        user = self.request.user
        for i in user.user_permissions.all():
            print(i)

        print(user.has_perm("catalog.can_unpublish_product"))
        if user.has_perm("catalog.can_unpublish_product"):
            return ProductModeratorForm
        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if (self.object.owner != request.user) or not request.user.has_perm("catalog.delete_product"):
            raise PermissionDenied("You do not have permission to delete this product.")
        return super().delete(request, *args, **kwargs)


class ProductListByCategoryView(ListView):
    model = Product
    template_name = "catalog/product_list_by_category.html"
    context_object_name = "products"

    def get_queryset(self):

            category_name = self.kwargs.get('category_name')
            if category_name:
                return Product.objects.filter(category__name=category_name)
            return Product.objects.all()  # Если категория не выбрана, выводим все товары

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_category'] = Category.objects.get(name=self.kwargs.get('category_name')) if self.kwargs.get(
            'category_name') else None
        return context
