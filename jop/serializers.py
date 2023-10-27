from rest_framework import serializers
from .models import Jop

class JopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jop
        exclude = ('location',)