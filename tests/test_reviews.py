import pytest


@pytest.mark.django_db
def test_take_reviews(client, header_with_auth, review, integration):
    response = client.post('/api/take-reviews',
                           {
                                'integration_id': integration.id,
                                'platform': 'google_play'
                           }, **header_with_auth)
    assert response.data[0]['id'] == review.id


@pytest.mark.django_db
def test_take_reviews_bad_integration(client, header_with_auth, review, integration):
    response = client.post('/api/take-reviews',
                           {
                               'integration_id': 666,
                               'platform': 'google_play'
                           }, **header_with_auth)
    try:
        assert not response.data[0]['id'] == review.id
    except Exception:
        assert True
    assert response.status_code == 400
