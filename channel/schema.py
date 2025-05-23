import graphene
from .models import Channel
from .types import ChannelType
from graphql_jwt.decorators import login_required

class ChannelQuery(graphene.ObjectType):
    all_channels = graphene.List(ChannelType)
    channel_by_id = graphene.Field(ChannelType, id=graphene.Int(required=True))

    @login_required
    def resolve_all_channels(root, info):
        return Channel.objects.all()

    @login_required
    def resolve_channel_by_id(root, info, id):
        try:
            return Channel.objects.get(id=id)
        except Channel.DoesNotExist:
            return None