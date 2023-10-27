from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Jop
from .serializers import JopSerializer


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