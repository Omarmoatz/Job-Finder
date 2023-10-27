'''
from rest_framework.response import Response
from rest_framework.decorators import api_view
'''
from rest_framework import generics,filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import Jop
from .serializers import JopSerializer

'''
@api_view(['GET'])
def job_list_api(request):
    job = Jop.objects.all()
    data = JopSerializer(job, many=True).data
    return Response({'job':data})

@api_view(['GET'])
def job_detail_api(request,id):
    job =Jop.objects.get(id=id)
    data = JopSerializer(job).data
    return Response({'job':data})
'''

class JobListApi(generics.ListCreateAPIView):
    queryset = Jop.objects.all()
    serializer_class = JopSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['vacancy', 'jop_nature']
    search_fields = ['title', 'salary_start']
    ordering_fields = ['salary_end', 'salary_start', 'experince']


class JobDetailtApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Jop.objects.all()
    serializer_class = JopSerializer