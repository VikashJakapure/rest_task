from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Movie, Genre
class MovieSerializer(serializers.ModelSerializer):
    """
    Serializer for Movie model
    """
    genre = serializers.SlugRelatedField(many=True,queryset=Genre.objects.all(),slug_field="name")
    class Meta:
        model = Movie
        fields = ('name', 'imdb_score', 'popularity', 'director', 'genre')

class GenreSerializer(serializers.ModelSerializer):
    """
    Serializer for Genre model
    """
    genre=MovieSerializer(many=True,read_only=True)
    class Meta:
        model = Genre
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    isStaff=serializers.BooleanField(default=False)
    class Meta:
        model=get_user_model()
        fields=('username','password',"isStaff")
