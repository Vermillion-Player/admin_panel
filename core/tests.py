import pytest 
from django.contrib.auth import get_user_model
from graphql_jwt.testcases import JSONWebTokenTestCase
from graphql_jwt.middleware import JSONWebTokenMiddleware
from graphene.test import Client
from .schema import schema
from model_bakery import baker
from core.schema import schema
from django.test.client import RequestFactory
from core.utils import create_user_and_token, get_authenticated_context

# MODELS TESTS:
@pytest.mark.django_db
def test_category_model_str():
    """ Test str for category model """

    category = baker.make(
        'core.Category',
        name="Categoría de Prueba"
    )
    assert str(category) == "Categoría de Prueba"


@pytest.mark.django_db
def test_actor_model_str():
    """ Test str for actor model """

    actor = baker.make(
        'core.Actor',
        name="Actor de Prueba"
    )
    assert str(actor) == "Actor de Prueba"
    

# AUTH TEST:
class TokenAuthTest(JSONWebTokenTestCase):
    """ Test for authentication JWT """

    def test_token_auth_mutation(self):
        User = get_user_model()
        username = "testuser"
        password = "testpassword"
        user = User.objects.create_user(username=username, password=password)

        response = self.client.execute(
            '''
            mutation TokenAuth($username: String!, $password: String!) {
                tokenAuth(username: $username, password: $password) {
                    token
                }
            }
            ''',
            variables={"username": username, "password": password}
        )

        token = response.data["tokenAuth"]["token"]
        assert token is not None


# GRAPHQUL QUERY TESTS:
@pytest.mark.django_db
class Test_categories():
    """ Test of categories operation """

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

        self.category = baker.make("core.category", 
                        name = "Terror",
                        description = "Género para pasar miedo",
                        only_adult = True,
                        logo = "terror.png")
        
        
    def test_all_categories_query(self):
        """ testing for all categories """
    
        query = '''
            query{
                allCategories{
                    name
                    description
                    onlyAdult
                    logo
                }
            }
        '''
        
        response = self.client.execute(
            query, 
            context_value=self.context,
            middleware = self.middleware
            )

        assert 'errors' not in response
        assert len(response['data']['allCategories']) == 1
        name = [category['name'] for category in response['data']['allCategories']]
        assert 'Terror' in name


    def test_category_by_id_query(self):
        """ testing for category by id """

        query = '''
            query{
                categoryById(id:1){
                    name
                    description
                    onlyAdult
                    logo
                }
            }
        '''
        
        response = self.client.execute(
            query,
            context_value=self.context,
            middleware=self.middleware
        )

        assert 'errors' not in response
        data = response['data']['categoryById']
        assert data is not None
        assert data['name'] == "Terror"


    def test_category_by_id_query_not_found(self):
        """ testing for category by id not found """
        
        query = '''
            query {
                categoryById(id: 9999) {
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
        assert response['data']['categoryById'] is None


@pytest.mark.django_db
class Test_actors():
    """ Test of actors operation """

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

        self.actor = baker.make("core.actor", 
                        name = "Paco",
                        description = "Actor de prueba",
                        image = "paco.png",
                        birthdate = "1980-01-01",
                        birthplace = "Madrid",
                        height = 1.80,
                        weight = 75.0,
                        genre = "M",
                        only_adult = False)
        
        
    def test_all_actors_query(self):
        """ testing for all actors """
    
        query = '''
            query{
                allActors{
                    name
                    description
                    image
                    birthdate
                    birthplace
                    height
                    weight
                    genre
                    onlyAdult
                }
            }
        '''
        
        response = self.client.execute(
            query, 
            context_value=self.context,
            middleware = self.middleware
            )

        assert 'errors' not in response
        assert len(response['data']['allActors']) == 1
        name = [actor['name'] for actor in response['data']['allActors']]
        assert 'Paco' in name


    def test_category_by_id_query(self):
        """ testing for actor by id """

        query = '''
            query{
                actorById(id:1){
                    name
                    description
                    image
                    birthdate
                    birthplace
                    height
                    weight
                    genre
                    onlyAdult
                }
            }
        '''
        
        response = self.client.execute(
            query,
            context_value=self.context,
            middleware=self.middleware
        )

        assert 'errors' not in response
        data = response['data']['actorById']
        assert data is not None
        assert data['name'] == "Paco"


    def test_category_by_id_query_not_found(self):
        """ testing for actor by id not found """

        query = '''
            query {
                actorById(id: 9999) {
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
        assert response['data']['actorById'] is None