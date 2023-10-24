from django.contrib import admin
from .models import Jop, Company ,Category

class Jop_admin(admin.ModelAdmin):
    search_fields = ['title','category','description']
    list_display = ['title','location','jop_nature','vacancy','category']
    list_filter = ['category','experince','vacancy','jop_nature']


admin.site.register(Jop,Jop_admin)
admin.site.register(Company)
admin.site.register(Category)



