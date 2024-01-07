from django.urls import path
from .views import BlogList,BlogDetail,add_comment

app_name='blog'

urlpatterns = [
    path('',BlogList.as_view(), name='blog_list'),
    path('<slug:slug>',BlogDetail.as_view(), name='blog_detail'),
    path('<slug:slug>/add-comment',add_comment, name='add_comment'),

]


