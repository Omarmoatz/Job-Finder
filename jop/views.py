from django.shortcuts import render
from .models import Jop

def jop_list(request):
    all_jobs = Jop.objects.all()
    return render(request, 'job/job_list.html', {'jop':all_jobs})
