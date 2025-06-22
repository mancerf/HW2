from django import forms
from .models import User
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm  # Добавлен AuthenticationForm
from django.core.exceptions import ValidationError


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Пароль")
    password_confirmation = forms.CharField(widget=forms.PasswordInput, label="Подтверждение пароля")

    class Meta:
        model = User
        fields = ('email', 'password', 'password_confirmation')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirmation = cleaned_data.get("password_confirmation")

        if password != password_confirmation:
            raise forms.ValidationError("Пароли не совпадают")

        # Здесь можно добавить валидацию пароля по требованиям
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]  # Нужно явно установить email, так как его нет в defaults

        password = self.cleaned_data["password"]
        user.set_password(password)
        if commit:
            user.save()
        return user


class CustomAuthenticationForm(AuthenticationForm):  # Кастомная форма аутентификации для email
    username = forms.CharField(label="Email", max_length=254)  # Используем email как username
    password = forms.CharField(widget=forms.PasswordInput)
    error_messages = {
        'invalid_login': (
            "Пожалуйста, введите правильный email и пароль. "
            "Обратите внимание, что оба поля могут быть чувствительны к регистру."
        ),
        'inactive': "Эта учетная запись неактивна.",
    }

    def __init__(self, request=None, *args, **kwargs):
        """
        The 'request' parameter is set for custom password reset flows.
        It is the user submitting the login form.
        """
        self.request = request
        self.user_cache = None
        super().__init__(request, *args, **kwargs)

    def clean(self):
        email = self.cleaned_data.get('username')  # email как username
        password = self.cleaned_data.get('password')

        if email is not None and password:
            self.user_cache = authenticate(self.request, username=email, password=password)  # Email как username
            if self.user_cache is None:
                raise forms.ValidationError(
                    self.error_messages['invalid_login'],
                    code='invalid_login',
                )
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

    def get_user(self):
        return self.user_cache
