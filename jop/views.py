from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Jop , JopForm
from .forms import AddForm




def jop_list(request):
    all_jobs = Jop.objects.all()
    job_count = all_jobs.count()
    page = request.GET.get('page', 1)

    paginator = Paginator(all_jobs, 40)
    try:
        all_jobs = paginator.page(page)
    except PageNotAnInteger:
        all_jobs = paginator.page(1)
    except EmptyPage:
        all_jobs = paginator.page(paginator.num_pages)
    return render(request, 'jop/job_list.html', {'jop':all_jobs, 'job_count':job_count})


def jop_detail(request, slug):
    jobs = Jop.objects.get(slug=slug)
    return render(request, 'jop/job_details.html', {'jop':jobs})


class ApplyForm(generic.CreateView):
    model = JopForm
    fields = ['name','email','link_url','github_url','cv','cover_letter']
    success_url ='/jop/'


    def form_valid(self, form):
        # Get the slug from the URL
        slug = self.kwargs['slug']
        # Get the job using the slug from the Job model
        job = get_object_or_404(Jop, slug=slug)
        # Add the job to the saved job apply
        form.instance.job = job
        return super().form_valid(form)
    

class AddJob(generic.CreateView):
    model = Jop
    #fields = ['title','location','company','salary_start','salary_end','vacancy','experince','jop_nature','description','category']
    success_url = '/jop/'
    form_class = AddForm
    