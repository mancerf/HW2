from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, ProductDetailView, ProductListView, ProductCreateView, ProductDeleteView, \
    ProductUpdateView, ProductListByCategoryView
from django.views.decorators.cache import cache_page

app_name = CatalogConfig.name

urlpatterns = [
    path('home/', home, name='home'),
    # path('contacts/', contacts, name='contacts'),
    path('', ProductListView.as_view(), name='product_list'),
    path('catalog/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),  #
    path("create/", ProductCreateView.as_view(), name="product_create"),
    path("<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"),
    path("<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),
    path('category/<str:category_name>/', ProductListByCategoryView.as_view(), name='product_list_by_category'),
]
