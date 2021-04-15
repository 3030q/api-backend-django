import datetime

from rest_framework.decorators import api_view
import pytest

from api.models import IntegrationType, Integration
from api.serializer import IntegrationSerializer



@pytest.mark.django_db
def test_add_integrations(client, auth, subscription, app, integration_type):
    token = f"Bearer {auth.data['access']}"
    header = {'HTTP_AUTHORIZATION': token}
    response = client.post('/api/add-integration',
                           {
                               'app_url': 'Test.com/test/test',
                               'integration_type_id': integration_type.id
                           }, **header)
    assert IntegrationSerializer(Integration.objects.get(pk=response.data['id'])).data == response.data


@pytest.mark.django_db
def test_add_integrations_with_expired_sub(client, auth, subscription, app, integration_type):
    token = f"Bearer {auth.data['access']}"
    header = {'HTTP_AUTHORIZATION': token}
    subscription.expired_at -= datetime.timedelta(days=30)
    subscription.save()
    response = client.post('/api/add-integration',
                           {
                               'app_url': 'Test.com/test/test',
                               'integration_type_id': integration_type.id
                           }, **header)
    assert response.status_code == 400
    try:
        fake_integration = Integration.objects.first()
    except Integration.DoesNotExist:
        fake_integration = None
    assert fake_integration is None


@pytest.mark.django_db
def test_add_integrations_with_bad_type(client, add_test_user, auth, subscription, app, integration_type):
    token = f"Bearer {auth.data['access']}"
    header = {'HTTP_AUTHORIZATION': token}
    response = client.post('/api/add-integration',
                           {
                               'app_url': 'Test.com/test/test',
                               'integration_type_id': -1
                           }, **header)
    assert response.status_code == 400
    try:
        fake_integration = Integration.objects.first()
    except Integration.DoesNotExist:
        fake_integration = None
    assert fake_integration is None


@pytest.mark.django_db
def test_add_integrations_without_app(client, auth, subscription, integration_type):
    token = f"Bearer {auth.data['access']}"
    header = {'HTTP_AUTHORIZATION': token}
    response = client.post('/api/add-integration',
                           {
                               'app_url': 'other.test.url',
                               'integration_type_id': integration_type.id
                           }, **header)

    assert response.status_code == 201
    assert IntegrationSerializer(Integration.objects.get(pk=response.data['id'])).data == response.data
    assert Integration.objects.get(pk=response.data['id']).app.url == 'other.test.url'


@pytest.mark.django_db
def test_add_integrations_max_limit(client, add_test_user, auth, subscription, app, integration_type):
    token = f"Bearer {auth.data['access']}"
    header = {'HTTP_AUTHORIZATION': token}
    subscription.subscription_type.max_app_count -= 100000
    subscription.subscription_type.save()
    response = client.post('/api/add-integration',
                           {
                               'app_url': 'other.test.url',
                               'integration_type_id': integration_type.id
                           }, **header)

    assert response.status_code == 400
    try:
        fake_integration = Integration.objects.first()
    except Integration.DoesNotExist:
        fake_integration = None
    assert fake_integration is None


@pytest.mark.django_db
def test_take_integration_types(client, integration_type):
    response = client.get('/api/integration-types')
    assert response.status_code == 200
