from rest_framework import serializers
from models import *

class UserSerializer(serializers.ModelSerializer):
    movies = serializers.PrimaryKeyRelatedField(many=True, queryset=Movie.objects.all())

    class Meta:
        model = MyUser
        fields = {'id', 'username', 'movies'}

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book

class TVSeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TVSeries

class TVSeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = TVSeason

class TVEpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TVEpisode