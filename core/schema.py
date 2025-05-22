import graphene
from .models import Category, Actor
from .types import CategoryType, ActorType
from channel.schema import ChannelQuery
from movie.schema import MovieQuery
from program.schema import ProgramQuery, SeasonQuery, EpisodesQuery

class CategoryQuery(graphene.ObjectType):
    all_categories = graphene.List(CategoryType)
    category_by_id = graphene.Field(CategoryType, id=graphene.Int(required=True))

    def resolve_all_categories(root, info):
        return Category.objects.all()

    def resolve_category_by_id(root, info, id):
        try:
            return Category.objects.get(id=id)
        except Category.DoesNotExist:
            return None


class ActorQuery(graphene.ObjectType):
    all_actors = graphene.List(ActorType)
    actor_by_id = graphene.Field(ActorType, id=graphene.Int(required=True))

    def resolve_all_actors(root, info):
        return Actor.objects.all()
    
    def resolve_actor_by_id(root, info, id):
        try:
            return Actor.objects.get(id=id)
        except:
            return None


# All queries pass here:
class Query(
    CategoryQuery, 
    ActorQuery,
    ChannelQuery, 
    MovieQuery,
    ProgramQuery,
    SeasonQuery,
    EpisodesQuery,
    graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)