from django.shortcuts import render
from .models import Jop

def jop_list(request):
    all_jobs = Jop.objects.all()
    return render(request, 'job/job_list.html', {'jop':all_jobs})

def jop_detail(request, slug):
    jobs = Jop.objects.get(slug=slug)
    return render(request, 'job/job_details.html', {'jop':jobs})
