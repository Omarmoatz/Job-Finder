from django.db import models

class MyData(models.Model):
    address = models.CharField(max_length=200)
    phone_num = models.PositiveIntegerField()
    email = models.EmailField( max_length=300)

    def __str__(self):
        return self.email
