from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter, BaseFilterBackend
from rest_framework import status, generics
from .models import Universitiesm
from .serializers import UniversitiesmSerializer

# Create your views here.

def index(request):
    return HttpResponse("Hello!")

@api_view(['GET'])
def getUniversity(request):
    university = Universitiesm.objects.all()
    serializer = UniversitiesmSerializer(university, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createUniversity(request):
    serializer = UniversitiesmSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['POST'])
def updateUniversity(request, pk):
    university = Universitiesm.objects.get(id=pk)
    serializer = UniversitiesmSerializer(instance=university, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['DELETE'])
def deleteUniversity(request, pk):
    university = Universitiesm.objects.get(id=pk)
    university.delete()
    return Response("University deleted successfully!")

class searchUniversity(generics.ListCreateAPIView):
    search_fields = ['name', 'country']
    filter_backends = (SearchFilter, OrderingFilter)
    serializer_class = UniversitiesmSerializer
    # queryset = Universitiesm.objects.all()
    def get_queryset(self):
        queryList = Universitiesm.objects.all()
        cc = self.request.query_params.get('cc', None)
        if cc:
            queryList = queryList.filter(alpha_two_code = cc)
        return queryList