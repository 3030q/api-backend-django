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
                               'name': 'Test',
                               'url': 'Test.com/test/test',
                               'rating': 5.0,
                               'dev_name': 'Testus',
                               'version': 'v.2',
                               'last_modified': datetime.now(tz=timezone.utc),
                               'count_reviews': 1000,
                               'platform': 'Google Play',
                               'active': True
                           }, **header_with_auth)
    assert response.data['name'] == 'Test'
    assert response.status_code == 201
