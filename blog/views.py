from django.shortcuts import render,redirect
from django.views import generic
from django.db.models import Count
from django.http import JsonResponse
from django.template.loader import render_to_string

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
    
def add_comment(request,slug):
    blog = Blog.objects.get(slug=slug)

    comment = request.POST['comment']

    if request.user.is_authenticated:
        user = request.user
    else:
        user = None

    Comment.objects.create(
        user = user,
        content = comment,
        blog = blog,
    )
    comments = Comment.objects.filter(blog=blog)
    html = render_to_string('includes/comments.html',{'comments':comments})
    return JsonResponse({'html':html})

