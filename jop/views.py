from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.decorators.cache import cache_page

from .models import Job , JobForm
from .forms import AddForm
from .myfilter import JobFilter

@cache_page(60 * 15)
def debug(request):
    data = Job.objects.filter(experince__gt= 6)
    # data = Jop.objects.select_related()
    # queryset api
    # data = Jop.objects.only('title','id')
    return render(request, 'jop/debug.html', {'data': data})

class JobList(generic.ListView):
    model = Job
    paginate_by= 10

    def get_queryset(self):
        queryset = super().get_queryset()
        myfilter = JobFilter(self.request.GET, queryset=queryset)
        return myfilter.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['myfilter'] = JobFilter(self.request.GET, queryset=self.get_queryset())
        return context

def jop_detail(request, slug):
    jobs = Job.objects.get(slug=slug)
    return render(request, 'jop/job_detail.html', {'jop':jobs})


class ApplyForm(generic.CreateView):
    model = JobForm
    fields = ['name','email','link_url','github_url','cv','cover_letter']
    success_url ='/job/'

    def form_valid(self, form):
        # Get the slug from the URL
        slug = self.kwargs['slug']
        # Get the job using the slug from the Job model
        job = get_object_or_404(Job, slug=slug)
        # Add the job to the saved job apply
        form.instance.job = job
        return super().form_valid(form)
    

class AddJob(generic.CreateView):
    model = Job
    #fields = ['title','location','company','salary_start','salary_end','vacancy','experince','jop_nature','description','category']
    success_url = '/job/'
    form_class = AddForm
    