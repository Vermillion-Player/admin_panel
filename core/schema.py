import graphene
from .models import Category, Actor
from .types import CategoryType, ActorType
from channel.schema import ChannelQuery
from movie.schema import MovieQuery

class CategoryQuery(graphene.ObjectType):
    all_categories = graphene.List(CategoryType)
    category_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))

    def resolve_all_categories(root, info):
        return Category.objects.all()

    def resolve_category_by_name(root, info, name):
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            return None


class ActorQuery(graphene.ObjectType):
    all_actors = graphene.List(ActorType)
    actor_by_name = graphene.Field(ActorType, name=graphene.String(required=True))

    def resolve_all_actors(root, info):
        return Actor.objects.all()
    
    def resolve_actor_by_name(root, info, name):
        try:
            return Actor.objects.get(name=name)
        except:
            return None


# All queries pass here:
class Query(
    CategoryQuery, 
    ActorQuery,
    ChannelQuery, 
    MovieQuery,
    graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)