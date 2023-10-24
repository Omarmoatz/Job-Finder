from django.db import models
from django_countries.fields import CountryField
from django.utils import timezone



JOP_CHOISE = (
    ('FullTime','Full_Time'),
    ('PartTime','PartTime'),
    ('Remote','Remote'),
    ('Freelance','Freelance')
)

class Jop(models.Model):
    title = models.CharField(max_length=150)
    location = CountryField()
    company =models.ForeignKey('Company', on_delete=models.CASCADE, related_name='jop_company')
    salary_start = models.PositiveIntegerField(null=True, blank=True)
    salary_end = models.PositiveIntegerField(null=True, blank=True)
    crated_at = models.DateTimeField(default=timezone.now)
    vacancy = models.PositiveIntegerField()
    experince = models.PositiveIntegerField()
    jop_nature = models.CharField(choices=JOP_CHOISE , max_length=10)
    description = models.TextField(max_length=5000)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL,null=True, blank=True, related_name='jop_category')
    
    def __str__(self) :
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100)
    logo = models.CharField(max_length=50)

    def __str__(self) :
        return self.name



class Company(models.Model):
    name = models.CharField(max_length=150)
    logo = models.ImageField(upload_to='company')
    website = models.URLField()
    email = models.EmailField()
    description = models.TextField(max_length=5000)

    def __str__(self) :
        return self.name