
from graphene_django import DjangoObjectType
from .models import Category, Actor

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = (
            "id", 
            "name", 
            "description", 
            "only_adult", 
            "logo"
            )


class ActorType(DjangoObjectType):
    class Meta:
        model = Actor
        fields = (
            "id", 
            "name", 
            "description", 
            "image", 
            "birthdate", 
            "birthplace", 
            "height", 
            "weight", 
            "genre",
              "only_adult"
            )
