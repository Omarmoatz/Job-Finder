from django.urls import path
from .views import jop_list, jop_detail, ApplyForm, AddJob, debug
from .api import JobDetailtApi , JobListApi

urlpatterns = [
    path('', jop_list),
    path('debug', debug),

    path('add', AddJob.as_view()),
    path('<slug:slug>', jop_detail),
    path('<slug:slug>/apply', ApplyForm.as_view()),



    path('api/list', JobListApi.as_view()),
    path('api/list/<int:pk>', JobDetailtApi.as_view())

]