from django.db import models

class Main(models.Model):
    name = models.CharField( max_length=50)
    logo = models.ImageField( upload_to='company_logo')
    about_us = models.TextField( max_length=300)
    address = models.CharField( max_length=100)
    phone = models.CharField( max_length=50)
    email = models.EmailField( max_length=254)
    fb_link = models.URLField( max_length=200)
    twitter_link = models.URLField( max_length=200)
    linkedIn_link= models.URLField( max_length=200)

    def __str__(self):
        return self.name

