from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify


class Blog(models.Model):
    auther = models.ForeignKey("Auther", related_name='auther_blog', on_delete=models.CASCADE)
    auther_comment = models.TextField(max_length=300,blank=True, null=True)
    title = models.CharField(max_length=200)
    img = models.ImageField( upload_to='blog_img')
    subtitle = models.TextField(max_length=400)
    content = models.TextField(max_length=10000)
    qoute = models.TextField(max_length=1000)
    created_at = models.DateField(default=timezone.now)
    category = models.ForeignKey("Category", related_name='ctg_blog',on_delete=models.SET_NULL,blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
       self.slug = slugify(self.title)
       super(Blog, self).save(*args, **kwargs)

class Auther(models.Model):
    name = models.CharField( max_length=50)
    img = models.ImageField( upload_to='auther_img',blank=True, null=True)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    tag = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Comment(models.Model):
    user = models.ForeignKey(User, related_name='user_comment', on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    blog = models.ForeignKey(Blog, related_name="blog_comments", on_delete=models.CASCADE)
    created_at = models.DateField(default=timezone.now)

    def __str__(self):
        return str(self.user)

