from graphene_django import DjangoObjectType
from .models import Channel


class ChannelType(DjangoObjectType):
    class Meta:
        model = Channel
        fields = (
            "id", 
            "name", 
            "description", 
            "logo", 
            "age", 
            "main_category", 
            "other_categories"
        )
