from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField( upload_to='blog_img')
    subtitle = models.TextField(max_length=400)
    content = models.TextField(max_length=2000)
    created_at = models.DateField(default=timezone.now)
    category = models.ForeignKey("Category", related_name='ctg_blog',on_delete=models.SET_NULL,blank=True, null=True)


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    tag = models.CharField(max_length=50)

class Comment(models.Model):
    user = models.ForeignKey(User, related_name='user_comment', on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    blog = models.ForeignKey(Blog, related_name="blog_comments", on_delete=models.CASCADE)
    created_at = models.DateField(default=timezone.now)


