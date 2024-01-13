from django.urls import path
from .views import home,contact

app_name = 'settings'

urlpatterns = [
    path('', home),
    path('contact/',contact, name='contact'),
]

