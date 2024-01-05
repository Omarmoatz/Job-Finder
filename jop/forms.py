from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from .models import Job
from django import forms


class AddForm(forms.ModelForm):
    description = forms.CharField(widget=SummernoteWidget())
    class Meta:
        model = Job
        fields = ['title','location','company','salary_start','salary_end','vacancy','experince','jop_nature','description','category']



