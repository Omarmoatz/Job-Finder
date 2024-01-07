from django.shortcuts import render
from django.views import generic
from django.db.models import Count

from .models import Blog,Comment,Category


class BlogList(generic.ListView):
    model = Blog
    paginate_by=5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ctgs"] = Category.objects.all().annotate(blog_num=Count('ctg_blog'))
        context["blogs"] = Blog.objects.all()[:5]
        return context
    
    
class BlogDetail(generic.DetailView):
    model=Blog

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comment"] = Comment.objects.filter(blog=self.get_object()) 
        context["ctgs"] = Category.objects.all().annotate(blog_num=Count('ctg_blog'))
        context["blogs"] = Blog.objects.all()[:5]
        return context
    

