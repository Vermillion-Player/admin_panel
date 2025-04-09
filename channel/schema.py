import graphene
from .models import Channel
from .types import ChannelType

class ChannelQuery(graphene.ObjectType):
    all_channels = graphene.List(ChannelType)
    channel_by_name = graphene.Field(ChannelType, name=graphene.String(required=True))

    def resolve_all_channels(root, info):
        return Channel.objects.all()

    def resolve_channel_by_name(root, info, name):
        try:
            return Channel.objects.get(name=name)
        except Channel.DoesNotExist:
            return None