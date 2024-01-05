from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Job, Company ,Category, JobForm


class Jop_admin(SummernoteModelAdmin):
    search_fields = ['title','category','description']
    list_display = ['title','location','jop_nature','vacancy','category']
    list_filter = ['category','experince','vacancy','jop_nature']
    summernote_fields = '__all__'


admin.site.register(Job,Jop_admin)
admin.site.register(Company)
admin.site.register(Category)
admin.site.register(JobForm)



