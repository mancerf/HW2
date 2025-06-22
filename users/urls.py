from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from users.apps import UsersConfig
from users.views import RegisterView
from .forms import CustomAuthenticationForm

app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html', authentication_form=CustomAuthenticationForm), name='login'),
    path('logout/', LogoutView.as_view(next_page='catalog:product_list'),
         name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]
