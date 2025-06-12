from django import forms
from django.core.exceptions import ValidationError

from catalog.models import Product
from django.core.validators import EmailValidator, MaxLengthValidator


class ProductForm(forms.ModelForm):
        class Meta:
            model = Product
            fields = '__all__'

            # ['name', 'description', 'image', 'price', 'category']

        def __init__(self, *args, **kwargs):
            super(ProductForm, self).__init__(*args, **kwargs)

            self.fields['name'].widget.attrs.update({
                'class': 'form-control',
                'placeholder': 'Введите Имя'
            })
            self.fields['description'].widget.attrs.update({
                'class': 'form-control',
                'placeholder': 'Введите Описание'
            })
            self.fields['image'].widget.attrs.update({
                'class': 'form-control'
            })
            self.fields['price'].widget.attrs.update({
                'class': 'form-control',
                'placeholder': 'Введите Цену'
            })
            self.fields['category'].widget.attrs.update({
                'class': 'form-control'
            })

        def clean(self):
            cleaned_data = super().clean()
            name = cleaned_data.get('name')
            description = cleaned_data.get('description')

            # Исправляем форматирование списка и убираем лишние запятые
            tabu = [
                'казино',
                'криптовалюта',
                'крипта',
                'биржа',
                'дешево',
                'бесплатно',
                'обман',
                'полиция',
                'радар'
            ]

            # Проверяем наличие запрещенных слов в имени
            if name and any(word in name.lower() for word in tabu):
                self.add_error('name', 'Имя содержит запрещенное слово')

            # Проверяем наличие запрещенных слов в описании
            if description and any(word in description.lower() for word in tabu):
                self.add_error('description', 'Описание содержит запрещенное слово')

            return cleaned_data

        def clean_price(self):
            price = self.cleaned_data.get('price')
            if price < 0:
                raise ValidationError('Цена не может быть отрицательным')
