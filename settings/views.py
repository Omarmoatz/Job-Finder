from django.shortcuts import render
from django.db.models import Count

from jop.models import Job,Category,Company
from blog.models import Blog


def home(request):
    category = Category.objects.all()[:8].annotate(job_num=Count('jop_category'))
    job = Job.objects.all()[:5]
    blog = Blog.objects.all()[:2]
    return render(request, 'settings/home.html',{
        'ctg':category,
        'job':job,
        'blog':blog,
    })
