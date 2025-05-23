from graphene_django import DjangoObjectType
from .models import Movie


class MovieType(DjangoObjectType):
    class Meta:
        model = Movie
        fields = (
            "id",
            "name", 
            "description", 
            "image", 
            "duration", 
            "release_date", 
            "only_adult", 
            "cast",
            "channel",
            "link"
            )
