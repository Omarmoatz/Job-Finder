from django.shortcuts import render
from django.db.models import Count
from django.core.mail import send_mail

from .models import Main
from jop.models import Job,Category,Company
from blog.models import Blog
from django.conf import settings


def home(request):
    category = Category.objects.all()[:8].annotate(job_num=Count('jop_category'))
    job = Job.objects.all()[:5]
    blog = Blog.objects.all()[:2]
    return render(request, 'settings/home.html',{
        'ctg':category,
        'job':job,
        'blog':blog,
    })

def contact(request):
    contact = Main.objects.last()

    if request.method == 'POSt':
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']

        send_mail(
            subject,
            message,
            email,
            [settings.EMAIL_HOST_USER],
        )

    return render(request,'settings/contact.html',{
        'contact':contact,
    })
