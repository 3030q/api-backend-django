from datetime import datetime, timezone

import pytest

from api.models import App


@pytest.mark.django_db
def test_take_app(client, app, header_with_auth):
    response = client.post('/api/take-app', {'app_id': app.id}, **header_with_auth)
    assert response.data['name'] == 'Test'
    assert response.data['last_modified']
    assert response.data['last_update_info']


@pytest.mark.django_db
def test_add_app(client, header_with_auth):
    response = client.post('/api/add-app',
                           {
                               'url': 'Test.com/test/test',
                               'platform': 'Google Play',
                               'active': False
                           }, **header_with_auth)
    assert response.data['url'] == 'Test.com/test/test'
    assert response.status_code == 201
