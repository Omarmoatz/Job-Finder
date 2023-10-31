from django.shortcuts import render
from django.views import generic
from .models import Jop , JopForm

def jop_list(request):
    all_jobs = Jop.objects.all()
    return render(request, 'jop/job_list.html', {'jop':all_jobs})

def jop_detail(request, slug):
    jobs = Jop.objects.get(slug=slug)
    return render(request, 'jop/job_details.html', {'jop':jobs})


class ApplyForm(generic.CreateView):
    model = JopForm
    fields = ['name','email','link_url','github_url','cv','cover_letter']
    success_url = ['/jop/']