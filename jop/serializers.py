from rest_framework import serializers
from .models import Job

class JopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        exclude = ('location',)