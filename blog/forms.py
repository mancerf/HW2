from django import forms
from .models import Blog
from django.core.validators import EmailValidator, MaxLengthValidator


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        #['title', 'content', 'preview', 'is_published', 'views_count']
