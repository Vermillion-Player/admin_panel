import pytest
from model_bakery import baker
from graphene.test import Client
from django.contrib.auth import get_user_model
from core.schema import schema
from django.test.client import RequestFactory
from graphql_jwt.middleware import JSONWebTokenMiddleware
from core.utils import create_user_and_token, get_authenticated_context

# MODELS TESTS:
@pytest.mark.django_db
def test_program_model_str():
    """ Test str for program model """

    category = baker.make('core.Category')
    channel = baker.make('channel.Channel', main_category=category)
    program = baker.make(
        'program.Program',
        name="Programa de prueba",
        main_category=category,
        channel=channel
    )
    assert str(program) == "Programa de prueba"


@pytest.mark.django_db
def test_program_model_creation_and_relations():
    """ Test creation and relations of program model """

    main_category = baker.make('core.Category')
    other_categories = baker.make('core.Category', _quantity=2)
    actors = baker.make('core.Actor', _quantity=3)
    channel = baker.make('channel.Channel', main_category=main_category)
    program = baker.make(
        'program.Program',
        name="Programa Relacional",
        main_category=main_category,
        channel=channel
    )
    program.other_categories.set(other_categories)
    program.actors.set(actors)
    assert program.main_category == main_category
    assert program.other_categories.count() == 2
    assert program.actors.count() == 3


@pytest.mark.django_db
def test_season_model_str():
    """ Test str for season model """

    program = baker.make('program.Program')
    season = baker.make(
        'program.Season',
        name="Temporada de prueba",
        program=program
    )
    assert str(season) == "Temporada de prueba"


@pytest.mark.django_db
def test_episodes_model_str():
    """ Test str for episodes model """

    program = baker.make('program.Program')
    season = baker.make('program.Season', program=program)
    episodes = baker.make(
        'program.Episodes',
        name="Episodio 1: soy de prueba",
        program=program,
        season=season
    )
    assert str(episodes) == "Episodio 1: soy de prueba"


@pytest.mark.django_db
def test_episodes_model_creation_and_relations():
    """ Test creation and relations of episodes model """

    program = baker.make('program.Program')
    season = baker.make('program.Season', program=program)
    cast = baker.make('core.Actor', _quantity=3)
    episodes = baker.make(
        'program.Episodes',
        name="Episodio 1: soy de prueba",
        program=program,
        season=season
    )
    episodes.cast.set(cast)
    assert episodes.program == program
    assert episodes.season == season
    assert episodes.cast.count() == 3


# GRAPHQUL QUERY TESTS:
@pytest.mark.django_db
class Test_programs():
    """ Test of program operation """

    @pytest.fixture(autouse=True)
    def setUp(self):
        self.middleware = [JSONWebTokenMiddleware()]
        self.factory = RequestFactory() 

        self.username = "testuser"
        self.password = "testuser"
        self.user, self.client, self.token = create_user_and_token(
            schema, self.factory, self.middleware, self.username, self.password
        )
        self.context = get_authenticated_context(self.factory, self.token)

        self.main = baker.make("core.category", 
                        name = "Terror",
                        description = "Género para pasar miedo",
                        only_adult = True,
                        logo = "terror.png")
    
        self.others = baker.make("core.category", _quantity=3)

        self.actors = baker.make("core.Actor", _quantity=3)

        self.channel = baker.make('channel.Channel', 
                name="Cine de terror", 
                description="Sección con grandes películas de terror",
                logo="terror.png",
                age="18",
                main_category=self.main,
                other_categories=self.others)
        
        self.program = baker.make('program.Program',
                name="Programa de terror",
                description="Un programa para los amantes del terror",
                image="terror_program.png",
                age="18",
                main_category=self.main,
                other_categories=self.others,
                actors=self.actors,
                channel=self.channel,
                release_date="2023-10-01"
            )
        
        self.season = baker.make('program.Season',
                name="Temporada de terror",
                description="Una temporada llena de episodios de terror",
                image="terror_season.png",
                program=self.program,
                release_date="2023-10-01"
            )
        
        self.episodes = baker.make('program.Episodes',
                name="Episodio 1: El misterio del terror",
                description="Un episodio lleno de misterio y terror",
                image="terror_episode.png",
                duration=60,
                program=self.program,
                season=self.season,
                cast=self.actors,
                release_date="2023-10-01"
            )

        
    def test_all_programs_query(self):
        """ testing for all programs """
    
        query = '''
            query{
                allPrograms{
                    name
                    description
                    image
                    age
                    mainCategory{
                        name
                    }
                    otherCategories{
                        name
                    }
                    actors{
                        name
                    }
                    releaseDate
                    channel{
                        name
                    }
                }
            }
        '''
        response = self.client.execute(
            query, 
            context_value=self.context,
            middleware = self.middleware
            )

        assert 'errors' not in response
        assert len(response['data']['allPrograms']) == 1
        name = [channel['name'] for channel in response['data']['allPrograms']]
        assert 'Programa de terror' in name

    
    def test_program_by_id_query(self):
        """ testing for program by id """

        query = '''
            query{
                programById(id:1){
                    name
                    description
                    image
                    age
                    mainCategory{
                        name
                    }
                    otherCategories{
                        name
                    }
                    actors{
                        name
                    }
                    releaseDate
                    channel{
                        name
                    }
                }
            }
        '''
        
        response = self.client.execute(
            query,
            context_value=self.context,
            middleware=self.middleware
        )

        assert 'errors' not in response
        data = response['data']['programById']
        assert data is not None
        assert data['name'] == "Programa de terror"
        assert data['mainCategory']['name'] == "Terror"
        assert len(data['otherCategories']) == 3
        assert len(data['actors']) == 3
        assert data['channel']['name'] == "Cine de terror"


    def test_program_by_id_query_not_found(self):
        """ testing for program by id not found """

        query = '''
            query {
                programById(id: 9999) {
                    name
                }
            }
        '''
        
        response = self.client.execute(
            query,
            context_value=self.context,
            middleware=self.middleware
        )
        assert 'errors' not in response
        assert response['data']['programById'] is None


    def test_all_seasons_query(self):
        """ testing for all seasons """
    
        query = '''
            query{
                allSeasons{
                    name
                    description
                    image
                    program{
                        name
                    }
                    releaseDate
                }
            }
        '''
        response = self.client.execute(
            query, 
            context_value=self.context,
            middleware = self.middleware
            )

        assert 'errors' not in response
        assert len(response['data']['allSeasons']) == 1
        name = [channel['name'] for channel in response['data']['allSeasons']]
        assert 'Temporada de terror' in name

    
    def test_season_by_id_query(self):
        """ testing for season by id """

        query = '''
            query {
                seasonById(id: 1) {
                    name
                    description
                    image
                    program{
                        name
                    }
                    releaseDate
                }
            }
        '''
        
        response = self.client.execute(
            query,
            context_value=self.context,
            middleware=self.middleware
        )

        assert 'errors' not in response
        data = response['data']['seasonById']
        assert data is not None
        assert data['name'] == "Temporada de terror"
        assert data['program']['name'] == "Programa de terror"


    def test_season_by_id_query_not_found(self):
        """ testing for season by id not found """

        query = '''
            query {
                seasonById(id: 9999) {
                    name
                }
            }
        '''
        
        response = self.client.execute(
            query,
            context_value=self.context,
            middleware=self.middleware
        )
        assert 'errors' not in response
        assert response['data']['seasonById'] is None


    def test_all_episodes_query(self):
        """ testing for all episodes """
    
        query = '''
            query{
                allEpisodes{
                    name
                    description
                    image
                    duration
                    program{
                        name
                    }
                    season{
                        name
                    }
                    cast{
                        name
                    }
                    releaseDate
                }
            }
        '''
        response = self.client.execute(
            query, 
            context_value=self.context,
            middleware = self.middleware
            )

        assert 'errors' not in response
        assert len(response['data']['allEpisodes']) == 1
        name = [channel['name'] for channel in response['data']['allEpisodes']]
        assert 'Episodio 1: El misterio del terror' in name

    
    def test_episodes_by_id_query(self):
        """ testing for episodes by id """

        query = '''
            query {
                episodesById(id: 1) {
                    name
                    description
                    image
                    duration
                    program{
                        name
                    }
                    season{
                        name
                    }
                    cast{
                        name
                    }
                    releaseDate
                }
            }
        '''
        
        response = self.client.execute(
            query,
            context_value=self.context,
            middleware=self.middleware
        )

        assert 'errors' not in response
        data = response['data']['episodesById']
        assert data is not None
        assert data['name'] == "Episodio 1: El misterio del terror"
        assert data['program']['name'] == "Programa de terror"
        assert data['season']['name'] == "Temporada de terror"
        assert len(data['cast']) == 3


    def test_episodes_by_id_query_not_found(self):
        """ testing for episodes by id not found """

        query = '''
            query {
                episodesById(id: 9999) {
                    name
                }
            }
        '''
        
        response = self.client.execute(
            query,
            context_value=self.context,
            middleware=self.middleware
        )
        assert 'errors' not in response
        assert response['data']['episodesById'] is None