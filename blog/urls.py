from django.urls import path
from .views import BlogList,BlogDetail,add_comment,AddBlog
from .api import BlogListAPI,BlogDetailAPI,CategoryAPI,CommentAPI,AutherAPI

app_name='blog'

urlpatterns = [
    path('',BlogList.as_view(), name='blog_list'),
    path('<slug:slug>',BlogDetail.as_view(), name='blog_detail'),
    path('<slug:slug>/add-comment',add_comment, name='add_comment'),
    path('add/',AddBlog.as_view(), name='add_blog'),

    #__  API  __
    path('api/',BlogListAPI.as_view()),
    path('api/<int:pk>',BlogDetailAPI.as_view()),
    path('api/ctg',CategoryAPI.as_view()),
    path('api/comment',CommentAPI.as_view()),
    path('api/auther',AutherAPI.as_view()),
]


