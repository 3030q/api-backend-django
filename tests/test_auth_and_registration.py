import pytest
from rest_framework_simplejwt.backends import TokenBackend
import django.test.client

from api.models import CustomUser


@pytest.fixture
def add_test_user():
    return CustomUser.objects.create_user(password='Password!!!',
                                          first_name='TestUser',
                                          last_name='TestUser',
                                          email='email@email.email')


@pytest.fixture
def add_test_admin():
    return CustomUser.objects.create_user(password='Password!!!',
                                          first_name='TestUser',
                                          last_name='TestUser',
                                          email='admin@admin.admin',
                                          is_superuser=True,
                                          is_staff=True)


@pytest.fixture
def auth(client, add_test_user):
    auth = client.post('/api/login',
                       {'email': 'email@email.email',
                        'password': 'Password!!!'})
    return auth


@pytest.fixture
def auth_admin(client, add_test_user):
    auth = client.post('/api/login',
                       {'email': 'admin@admin.admin',
                        'password': 'Password!!!'})
    return auth


@pytest.mark.django_db
def test_register(client):
    response = client.post('/api/registration',
                           {'password': 'Password!!!',
                            'first_name': 'TestUser',
                            'last_name': 'TestUser',
                            'email': 'email@email.email'})
    valid_data = TokenBackend(algorithm='HS256').decode(response.data['access'], verify=False)
    assert valid_data['email'] == 'email@email.email'


@pytest.mark.django_db
def test_auth(client, add_test_user):
    response = client.post('/api/login',
                           {'email': 'email@email.email',
                            'password': 'Password!!!'})
    valid_data = TokenBackend(algorithm='HS256').decode(response.data['access'], verify=False)
    assert valid_data['email'] == 'email@email.email'


@pytest.mark.django_db
def test_logout(client, auth):
    token = f"Bearer {auth.data['access']}"
    header = {'HTTP_AUTHORIZATION': token}

    response = client.post('/api/logout',
                           data={'access': auth.data['access'],
                                 'refresh': auth.data['refresh']},
                           content_type='application/json',
                           **header)
    assert response.status_code == 205
