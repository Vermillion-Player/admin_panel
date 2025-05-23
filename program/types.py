from graphene_django import DjangoObjectType
from .models import Program, Season, Episodes


class ProgramType(DjangoObjectType):
    class Meta:
        model = Program
        fields = (
            "id",
            "name", 
            "description", 
            "image", 
            "age", 
            "main_category", 
            "other_categories", 
            "actors",
            "release_date",
            "channel"
            )
        

class SeasonType(DjangoObjectType):
    class Meta:
        model = Season
        fields = (
            "id",
            "name",
            "description",
            "image",
            "program",
            "release_date"
        )


class EpisodesType(DjangoObjectType):
    class Meta:
        model = Episodes
        fields = (
            "id",
            "name",
            "description",
            "image",
            "duration",
            "program",
            "season",
            "cast",
            "release_date",
            "link"
        )