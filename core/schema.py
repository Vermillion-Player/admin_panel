import graphene
import graphql_jwt
from graphql_jwt.decorators import login_required

from .models import Category, Actor
from .types import CategoryType, ActorType
from channel.schema import ChannelQuery
from movie.schema import MovieQuery
from program.schema import ProgramQuery, SeasonQuery, EpisodesQuery


class AuthMutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

class CategoryQuery(graphene.ObjectType):
    all_categories = graphene.List(CategoryType)
    category_by_id = graphene.Field(CategoryType, id=graphene.Int(required=True))

    @login_required
    def resolve_all_categories(root, info):
        return Category.objects.all()

    @login_required
    def resolve_category_by_id(root, info, id):
        try:
            return Category.objects.get(id=id)
        except Category.DoesNotExist:
            return None


class ActorQuery(graphene.ObjectType):
    all_actors = graphene.List(ActorType)
    actor_by_id = graphene.Field(ActorType, id=graphene.Int(required=True))

    @login_required
    def resolve_all_actors(root, info):
        return Actor.objects.all()
    
    @login_required
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


class Mutation(
    AuthMutation, 
    graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)