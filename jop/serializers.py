from rest_framework import serializers
from .models import Job,Company,Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class JobSerializer(serializers.ModelSerializer):
    company = serializers.StringRelatedField()
    category = serializers.StringRelatedField()
    class Meta:
        model = Job
        exclude = ('location',)

class JobDetailSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    category = CategorySerializer()
    class Meta:
        model = Job
        exclude = ('location',)