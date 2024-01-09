from rest_framework import serializers
from .models import Blog,Auther,Category,Comment


class CommentSerializer(serializers.ModelSerializer):
    blog = serializers.StringRelatedField()
    user = serializers.StringRelatedField()
    class Meta:
        model = Comment
        fields ='__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields ='__all__'

class AutherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auther
        fields ='__all__'

class BlogSerializer(serializers.ModelSerializer):
    category=CategorySerializer()
    class Meta:
        model = Blog
        fields ='__all__'

class BlogDetailSerializer(serializers.ModelSerializer):
    category=CategorySerializer()
    auther=AutherSerializer()
    comment = CommentSerializer(source='blog_comments' ,many=True)
    class Meta:
        model = Blog
        fields ='__all__'
