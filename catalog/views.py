from django.shortcuts import render


# Create your views here.
def home(requests):
    return render(requests, template_name='catalog/home.html')


def contacts(requests):
    return render(requests, template_name='catalog/contacts.html')
