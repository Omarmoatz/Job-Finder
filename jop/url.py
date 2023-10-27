from django.urls import path
from .views import jop_list, jop_detail
from .api import job_list_api , job_detail_api

urlpatterns = [
    path('', jop_list),
    path('<slug:slug>', jop_detail),

    path('api/list', job_list_api),
    path('api/list/<int:id>', job_detail_api)

]