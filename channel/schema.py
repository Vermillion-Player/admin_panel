import graphene
from graphene_django import DjangoObjectType

from .models import Channel

class ChannelType(DjangoObjectType):
    class Meta:
        model = Channel
        fields = ("id", "name", "description", "logo", "only_adult", "main_category", "other_categories")

class Query(graphene.ObjectType):
    all_channels = graphene.List(ChannelType)
    channel_by_name = graphene.Field(ChannelType, name=graphene.String(required=True))

    def resolve_all_channels(root, info):
        return Channel.objects.all()

    def resolve_channel_by_name(root, info, name):
        try:
            return Channel.objects.get(name=name)
        except Channel.DoesNotExist:
            return None

schema = graphene.Schema(query=Query)