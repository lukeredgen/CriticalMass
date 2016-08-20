from django.shortcuts import render
from django.http import HttpResponse
from models import *
from rest_framework import generics
from django.views.generic import ListView
from serializers import *

# Create your views here.
class UserList(generics.ListAPIView):
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer

# Views for album releases and reviews

class AlbumDetail(generics.RetrieveAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class AlbumReviews(generics.ListAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class AlbumDetail(generics.RetrieveAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

# Views for movie releases and reviews
class MovieReviews(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDetail(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class TrackDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class TVSeriesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TVSeries.objects.all()
    serializer_class = TVSeriesSerializer

class TVSeasonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TVSeason.objects.all()
    serializer_class = TVSeasonSerializer

class TVEpisodeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TVEpisode.objects.all()
    serializer_class = TVEpisodeSerializer