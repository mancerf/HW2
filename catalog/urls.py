from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, ProductDetailView, ProductListView, ProductCreateView,ProductDeleteView, ProductUpdateView

app_name = CatalogConfig.name

urlpatterns = [
    path('home/', home, name='home'),
   # path('contacts/', contacts, name='contacts'),
    path('', ProductListView.as_view(), name ='product_list'),
    path('catalog/<int:pk>/', ProductDetailView.as_view(), name ='product_detail'),
    path("create/", ProductCreateView.as_view(), name="product_create"),
    path("<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"),
    path("<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),

]