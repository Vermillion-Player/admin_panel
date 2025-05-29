from django.contrib.auth import get_user_model
from graphene.test import Client

def create_user_and_token(schema, factory, middleware, username="testuser", password="testuser"):
    User = get_user_model()
    user = User.objects.create_user(username=username, password=password)
    client = Client(schema)
    request = factory.post('/graphql/')
    context = request

    response = client.execute(
        '''
        mutation TokenAuth($username: String!, $password: String!) {
            tokenAuth(username: $username, password: $password) {
                token
            }
        }
        ''',
        variables={"username": username, "password": password},
        context_value=context,
        middleware=middleware
    )

    token = response["data"]["tokenAuth"]["token"]
    return user, client, token


def get_authenticated_context(factory, token):
    request = factory.post('/graphql/')
    request.META['HTTP_AUTHORIZATION'] = f'JWT {token}'
    return request