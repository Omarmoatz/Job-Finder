from jop.models import Job,Category,Company

from django.shortcuts import render

def home(request):
    category = Category.objects.all()[:8]
    job = Job.objects.all()[:5]
    return render(request, 'settings/home.html',{
        'ctg':category,
        'job':job,
    })
