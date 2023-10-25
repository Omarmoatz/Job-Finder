from django.urls import path
from .views import jop_list, jop_detail

urlpatterns = [
    path('', jop_list),
    path('<slug:slug>', jop_detail),
]