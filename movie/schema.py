import graphene
from .models import Movie
from .types import MovieType

class MovieQuery(graphene.ObjectType):
    all_movies = graphene.List(MovieType)
    movie_by_name = graphene.Field(MovieType, name=graphene.String(required=True))

    def resolve_all_movies(root, info):
        return Movie.objects.all()

    def resolve_movie_by_name(root, info, name):
        try:
            return Movie.objects.get(name=name)
        except Movie.DoesNotExist:
            return None