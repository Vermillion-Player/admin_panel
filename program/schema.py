import graphene
from .models import Program, Season, Episodes
from .types import ProgramType, SeasonType, EpisodesType

class ProgramQuery(graphene.ObjectType):
    all_programs = graphene.List(ProgramType)
    program_by_name = graphene.Field(ProgramType, name=graphene.String(required=True))
    program_by_id = graphene.Field(ProgramType, id=graphene.Int(required=True))

    def resolve_all_programs(root, info):
        return Program.objects.all()

    def resolve_program_by_name(root, info, name):
        try:
            return Program.objects.get(name=name)
        except Program.DoesNotExist:
            return None
        
    def resolve_program_by_id(root, info, id):
        try:
            return Program.objects.get(id=id)
        except Program.DoesNotExist:
            return None


class SeasonQuery(graphene.ObjectType):
    all_seasons = graphene.List(SeasonType)
    season_by_name = graphene.Field(SeasonType, name=graphene.String(required=True))

    def resolve_all_seasons(root, info):
        return Season.objects.all()

    def resolve_season_by_name(root, info, name):
        try:
            return Season.objects.get(name=name)
        except Season.DoesNotExist:
            return None


class EpisodesQuery(graphene.ObjectType):
    all_episodes = graphene.List(EpisodesType)
    episodes_by_name = graphene.Field(EpisodesType, name=graphene.String(required=True))

    def resolve_all_episodes(root, info):
        return Episodes.objects.all()

    def resolve_episodes_by_name(root, info, name):
        try:
            return Episodes.objects.get(name=name)
        except Episodes.DoesNotExist:
            return None