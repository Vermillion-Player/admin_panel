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
def test_movie_model_str():
    """ Test str for movie model """

    channel = baker.make('channel.Channel')
    movie = baker.make(
        'movie.Movie',
        name="La película de pruebas",
        channel=channel
    )
    assert str(movie) == "La película de pruebas"


@pytest.mark.django_db
def test_movie_model_creation_and_relations():
    """ Test creation and relations of movie model """

    cast = baker.make('core.Actor', _quantity=3)
    channel = baker.make('channel.Channel')
    movie = baker.make(
        'movie.Movie',
        name="Otra peli de probar",
        channel=channel
    )
    movie.cast.set(cast)
    assert movie.cast.count() == 3
    assert movie.channel == channel


# GRAPHQUL QUERY TESTS:
@pytest.mark.django_db
class Test_movies():
    """ Test of movie operation """

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
                        name = "Acción",
                        description = "Género para no despegarse de la pantalla",
                        only_adult = True,
                        logo = "accion.png")
        
        self.cast = baker.make("core.Actor", _quantity=3)

        self.others = baker.make("core.category", _quantity=3)

        self.channel = baker.make('channel.Channel',
                name="Cine de acción", 
                description="Sección con grandes películas de acción",
                logo="action.png",
                age="16",
                main_category=self.main,
                other_categories=self.others)
        
        self.movie = baker.make('movie.Movie',
                name="La gran película de acción",
                description="Una película llena de acción y emoción",
                image="action_movie.png",
                duration=120,
                release_date="2023-01-01",
                only_adult=False,
                channel=self.channel
            )
        self.movie.cast.set(self.cast)

        
    def test_all_movies_query(self):
        """ testing for all movies """
    
        query = '''
            query{
                allMovies{
                    name
                    description
                    image
                    duration
                    releaseDate
                    onlyAdult
                    cast{
                        name
                    }
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
        assert len(response['data']['allMovies']) == 1
        name = [channel['name'] for channel in response['data']['allMovies']]
        assert 'La gran película de acción' in name

    
    def test_movie_by_id_query(self):
        """ Testing for movie by id """

        query = '''
            query{
                movieById(id:1){
                    name
                    description
                    image
                    duration
                    releaseDate
                    onlyAdult
                    cast{
                        name
                    }
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
        data = response['data']['movieById']
        assert data is not None
        assert data['name'] == "La gran película de acción"
        assert len(data['cast']) == 3
        assert data['channel']['name'] == "Cine de acción"


    def test_channel_by_id_query_not_found(self):
        query = '''
            query {
                movieById(id: 9999) {
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
        assert response['data']['movieById'] is None