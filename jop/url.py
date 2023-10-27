from django.urls import path
from .views import jop_list, jop_detail
from .api import JobDetailtApi , JobListApi

urlpatterns = [
    path('', jop_list),
    path('<slug:slug>', jop_detail),

    path('api/list', JobListApi.as_view()),
    path('api/list/<int:pk>', JobDetailtApi.as_view())

]