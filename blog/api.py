from rest_framework import generics
from .serializers import BlogSerializer
from .models import Blog


class BlogListAPI(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    

class BlogDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
