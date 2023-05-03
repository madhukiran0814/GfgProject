from rest_framework import serializers
from .models import Work, Artist

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'name')

class WorkSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(many=False, read_only=True)
    
    class Meta:
        model = Work
        fields = ('id', 'link', 'work_type', 'artist')
