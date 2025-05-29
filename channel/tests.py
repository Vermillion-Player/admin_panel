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
def test_channel_model_str():
    """ Test str for channel model """

    category = baker.make('core.Category')
    channel = baker.make(
        'channel.Channel',
        name="Canal de Prueba",
        main_category=category
    )
    assert str(channel) == "Canal de Prueba"

@pytest.mark.django_db
def test_channel_model_creation_and_relations():
    """ Test creation and relations of channel model """

    main_category = baker.make('core.Category')
    other_categories = baker.make('core.Category', _quantity=2)
    channel = baker.make(
        'channel.Channel',
        name="Canal Relacional",
        main_category=main_category
    )
    channel.other_categories.set(other_categories)
    assert channel.main_category == main_category
    assert channel.other_categories.count() == 2


# GRAPHQUL QUERY TESTS:
@pytest.mark.django_db
class Test_channels():
    """ Test of channel operation """

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

        self.channel = baker.make('channel.Channel', 
                name="Cine de terror", 
                description="Sección con grandes películas de terror",
                logo="terror.png",
                age="18",
                main_category=self.main,
                other_categories=self.others)

        
    def test_all_channels_query(self):
        """ testing for all channels """
    
        query = '''
            query{
                allChannels{
                    name
                    description
                    logo
                    age
                    mainCategory{
                    name
                    }
                    otherCategories{
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
        assert len(response['data']['allChannels']) == 1
        name = [channel['name'] for channel in response['data']['allChannels']]
        assert 'Cine de terror' in name

    
    def test_channel_by_id_query(self):
        """ testing for channel by id """

        query = f'''
            query {{
                channelById(id: {self.channel.id}) {{
                    name
                    description
                    logo
                    age
                    mainCategory {{
                        name
                    }}
                    otherCategories {{
                        name
                    }}
                }}
            }}
        '''
        
        response = self.client.execute(
            query,
            context_value=self.context,
            middleware=self.middleware
        )

        assert 'errors' not in response
        data = response['data']['channelById']
        assert data is not None
        assert data['name'] == "Cine de terror"
        assert data['mainCategory']['name'] == "Terror"
        assert len(data['otherCategories']) == 3


    def test_channel_by_id_query_not_found(self):
        """ testing for channel by id not found """

        query = '''
            query {
                channelById(id: 9999) {
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
        assert response['data']['channelById'] is None