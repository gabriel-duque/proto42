from rest_framework import serializers

from backend.models import Artist, Song, Album, Genre


class ArtistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        fields = ('id', 'name')

class SongSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields = ('id', 'name', 'duration', 'artist', 'album', 'genre', 'path',
                  'track_number')

class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        fields = ('id', 'name', 'artist', 'genre', 'date', 'track_count',
                  'front', 'cover_image')

class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('id', 'name', 'period')
