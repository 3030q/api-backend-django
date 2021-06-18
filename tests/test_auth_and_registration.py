import datetime

import pytest
from rest_framework_simplejwt.backends import TokenBackend

from api.models import CustomUser


@pytest.mark.django_db
def test_register(client):
    response = client.post('/api/registration',
                           {'password': 'Password!!!',
                            'first_name': 'TestUser',
                            'last_name': 'TestUser',
                            'email': 'email@email.email'})
    assert response.data['access']
    assert type(response.data['access']) is str


@pytest.mark.django_db
def test_auth(client, test_user):
    response = client.post('/api/login',
                           {'email': 'email@email.email',
                            'password': 'Password!!!'})
    assert response.data['access']
    assert type(response.data['access']) is str


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
    assert response.data == {'result': 'Logout was successful'}


@pytest.mark.django_db
@pytest.mark.freeze_time()
def test_take_user_info(client, auth):
    token = f"Bearer {auth.data['access']}"
    header = {'HTTP_AUTHORIZATION': token}
    response = client.get('/api/take-user-info', **header)
    assert response.data == {
        'id': 1,
        'last_login': None,
        'is_superuser': False,
        'first_name': 'TestUser',
        'last_name': 'TestUser',
        'is_staff': False,
        'is_active': True,
        'email': 'email@email.email',
        'groups': [],
        'user_permissions': []
    }
