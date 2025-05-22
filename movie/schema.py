import graphene
from .models import Movie
from .types import MovieType

class MovieQuery(graphene.ObjectType):
    all_movies = graphene.List(MovieType)
    movie_by_id = graphene.Field(MovieType, id=graphene.Int(required=True))

    def resolve_all_movies(root, info):
        return Movie.objects.all()

    def resolve_movie_by_id(root, info, id):
        try:
            return Movie.objects.get(id=id)
        except Movie.DoesNotExist:
            return None