from django.shortcuts import render,redirect
from django.views import generic
from django.db.models import Count
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Blog,Comment,Category
from .forms import BlogForm


class BlogList(generic.ListView):
    model = Blog
    paginate_by=5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ctgs"] = Category.objects.all().annotate(blog_num=Count('ctg_blog'))
        context["blogs"] = Blog.objects.all().order_by('-id')[:5]
        return context
    
    
class BlogDetail(generic.DetailView):
    model=Blog

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comment"] = Comment.objects.filter(blog=self.get_object()) 
        context["ctgs"] = Category.objects.all().annotate(blog_num=Count('ctg_blog'))
        context["blogs"] = Blog.objects.all().order_by('-id')[:5]
        return context
    
@login_required
def add_comment(request,slug):
    blog = Blog.objects.get(slug=slug)

    comment_text = request.POST['comment']

    if request.user.is_authenticated:
        user = request.user
    else:
        user = None

    Comment.objects.create(
        user = user,
        content = comment_text,
        blog = blog,
    )
    comment = Comment.objects.filter(blog=blog)
    html = render_to_string('includes/comments.html',{'comment':comment})
    return JsonResponse({'html':html})


class AddBlog(LoginRequiredMixin,generic.CreateView):
    model = Blog
    form_class = BlogForm
    success_url = '/blog/'