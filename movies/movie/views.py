from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 
from django.shortcuts import render
from django.http import HttpResponse
import requests
import time
from .serializers import CollectionsSerializer, CounterSerializer
from .models import Collections, Counter, Movies, Genres
# Create your views here.

class Register(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(Register, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key})

@api_view(['GET'])
def movielist(request):
    try:
        response = requests.get('https://demo.credy.in/api/v1/maya/movies/', auth=("iNd3jDMYRKsN1pjQPMRz2nrq7N99q4Tsp9EY9cM0", "Ne5DoTQt7p8qrgkPdtenTK8zd6MorcCR5vXZIJNfJwvfafZfcOs4reyasVYddTyXCz9hcL5FGGIVxw3q02ibnBLhblivqQTp4BIC93LZHj4OppuHQUzwugcYu7TIC5H1"))
        moviesdata = response.json()
        populateMovies(moviesdata)
        return Response(moviesdata)
    except Exception:
        time.sleep(1)
        return movielist()

@api_view(['GET','POST'])
def collection(request):
    if request.method == 'POST':
        serializer = CollectionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'collection_uuid':serializer.data['uuid']})
        return Response(serializer.errors)

    elif request.method == 'GET':
        collection = Collections.objects.all()
        serializer = CollectionsSerializer(collection, many=True)
        coll = {'success': True, 'data':{'collections':serializer.data}}
        return Response(coll)

@api_view(['GET', 'PUT', 'DELETE'])
def editCollection(request, uuid):
    collection = Collections.objects.filter(uuid=uuid)
    if request.method == 'GET':
        serializer = CollectionsSerializer(collection, many=True)
        return Response(serializer.data)
    
    if request.method == 'DELETE':
        collection.delete()
        return Response("Deleted")

    if request.method == 'PUT':
        coll = Collections.objects.filter(uuid=uuid).first()
        coll_serializer = CollectionsSerializer(coll, data=request.data)
        if coll_serializer.is_valid():
            print(coll_serializer)
            coll_serializer.save()
            return Response(coll_serializer.data)
        return Response(coll_serializer.errors)
    
@api_view(['GET'])
def counter(request):
    count = Counter.objects.all().count()
    response = {'requests': count}
    return Response(response)
    
@api_view(['POST'])
def resetcounter(request):
    Counter.objects.all().delete()
    response = {'message': 'request count reset successfully”'}
    return Response(response)

def populateMovies(moviesdata):
    for i in range(len(moviesdata['results'])):
        current_uuid = moviesdata['results'][i]['uuid']
        if (Movies.objects.filter(movie_uuid= current_uuid).count() == 0):
            Movies.objects.create(movie_uuid = current_uuid)
            for j in moviesdata['results'][i]['genres'].split(","):
                if(Genres.objects.filter(genre = j).count() != 0):
                    Movies.objects.get(movie_uuid = current_uuid).genre.add(Genres.objects.get(genre = j))