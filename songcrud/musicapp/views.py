from django.shortcuts import render
# from django.http import JsonResponse
from .models import Artiste,Song
from .serializers import ArtisteSerializers,SongSerializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(['GET','POST'])
def artiste_list_and_song_List(request):
    #This get all the Artiste and serilaize them and return them in Json view
    if request.method=='GET':
        artiste=Artiste.objects.all()
        song=Song.objects.all()
        art_serializer=ArtisteSerializers(artiste,many=True)
        song_serializer=SongSerializers(song,many=True)
    # ResultModel=art_serializer.data+song_serializer.data
    # return JsonResponse({'Artiste':serializer.data})
        return Response({'Artiste':art_serializer.data + song_serializer.data})
    #ADDING THE ARTISTE AND SONG INTO THE MODEL
    if request.method=='POST':
        art_serializer=ArtisteSerializers(data=request.data)
        if art_serializer.is_valid():
            art_serializer.save()
            return Response(art_serializer.data,status=status.HTTP_201_CREATED)
        song_serializer=SongSerializers(data=request.data)
        if song_serializer.is_valid():
            song_serializer.save()
            return Response(song_serializer.data,status=status.HTTP_201_CREATED)
        
#FETCH, UPDATE AND DELETE A SONG IN THE MODEL
@api_view(['GET', 'PUT', 'DELETE'])      
def song_details(request,id):
    try:
        song=Song.objects.get(pk=id)
    except Song.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        song_serializer=SongSerializers(song)
        return Response(song_serializer.data)
    elif request.method=='PUT':
         song_serializer=SongSerializers(song,data=request.data)
         if song_serializer.is_valid():
                song_serializer.save()
                return Response(song_serializer.data)
         return Response(song_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)