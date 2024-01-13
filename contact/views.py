from django.shortcuts import render
from .models import MyData


def contact(request):
    return render(request,'contact/contact.html',{})
