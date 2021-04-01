import pytest

from api.models import CustomUser


@pytest.mark.django_db
def test_register(client):
    response = client.post('/api/registration',
                           {'password': 'Password!!!',
                            'first_name': 'TestUser',
                            'last_name': 'TestUser',
                            'email': 'email@email.email'})
    assert response.data['access']
    assert response.status_code == 200


@pytest.mark.django_db
def test_auth(client):
    CustomUser.objects.create_user(password='Password!!!',
                                   first_name='TestUser',
                                   last_name='TestUser',
                                   email='email@email.email')
    response = client.post('/api/login',
                           {'email': 'email@email.email',
                            'password': 'Password!!!'})
    assert response.status_code == 200
    assert response.data['access']
    assert response.data['refresh']
