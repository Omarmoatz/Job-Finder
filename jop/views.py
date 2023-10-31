from django.shortcuts import render
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Jop , JopForm

def jop_list(request):
    all_jobs = Jop.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(all_jobs, 40)
    try:
        all_jobs = paginator.page(page)
    except PageNotAnInteger:
        all_jobs = paginator.page(1)
    except EmptyPage:
        all_jobs = paginator.page(paginator.num_pages)
    return render(request, 'jop/job_list.html', {'jop':all_jobs})


def jop_detail(request, slug):
    jobs = Jop.objects.get(slug=slug)
    return render(request, 'jop/job_details.html', {'jop':jobs})


class ApplyForm(generic.CreateView):
    model = JopForm
    fields = ['name','email','link_url','github_url','cv','cover_letter']
    success_url = ['/jop/']