from django_filters import rest_framework as filters

from .models import Job

class JobFilter(filters.FilterSet):
    class Meta:
        model = Job
        fields = ['category','jop_nature','experince','crated_at','salary_start']
