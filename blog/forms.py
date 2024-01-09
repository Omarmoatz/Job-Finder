from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from .models import Blog

class BlogForm(forms.ModelForm):
    content = forms.CharField(widget=SummernoteWidget())
    qoute = forms.CharField(widget=SummernoteWidget())
    class Meta:
        model = Blog
        fields = ['title','img','subtitle','content','qoute','auther','auther_comment','category']

