from django.http import JsonResponse
from .models import Movie
from .serializers import MovieSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])
def movie_list(request):
    if request.method=='GET':
        movies=Movie.objects.all()
        serializer = MovieSerializer(movies,many=True)
        return Response(serializer.data)
    if request.method=='POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)