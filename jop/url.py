from django.urls import path
from .views import jop_list

urlpatterns = [
    path('', jop_list)
]