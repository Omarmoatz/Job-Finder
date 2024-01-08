from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Blog,Comment,Category,Auther


class BlogContent(SummernoteModelAdmin):
    summernote_fields = '__all__'

admin.site.register(Blog,BlogContent)
admin.site.register(Auther)
admin.site.register(Comment)
admin.site.register(Category)


