import datetime

import pytest

from api.models import SubscriptionType, Subscription
from api.serializer import SubscriptionSerializer


@pytest.mark.django_db
def test_add_subscription(client, add_test_user, auth, subscription_type):
    token = f"Bearer {auth.data['access']}"
    header = {'HTTP_AUTHORIZATION': token}
    response = client.post('/api/add-subscription',
                           {
                               'user': add_test_user.id,
                               'subscription_type': subscription_type.id,
                               'expired_at': datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(days=10)
                           }, **header)
    assert Subscription.objects.get(pk=response.data['id']).user.id == add_test_user.id


@pytest.mark.django_db
def test_remove_subscription(client, add_test_user, auth, subscription):
    token = f"Bearer {auth.data['access']}"
    header = {'HTTP_AUTHORIZATION': token}
    assert Subscription.objects.get(pk=subscription.id)
    response = client.get('/api/remove-subscription', **header)
    try:
        remote_record = Subscription.objects.get(pk=subscription.id)
    except Subscription.DoesNotExist:
        remote_record = None
    assert remote_record is None


@pytest.mark.django_db
def test_remove_expired_subscription(client, add_test_admin, auth_admin, subscription):
    subscription.expired_at -= datetime.timedelta(days=30)
    subscription.save()
    token = f"Bearer {auth_admin.data['access']}"
    header = {'HTTP_AUTHORIZATION': token}
    assert Subscription.objects.get(pk=subscription.id)
    response = client.get('/api/remove-expired-subscription', **header)
    try:
        remote_record = Subscription.objects.get(pk=subscription.id)
    except Subscription.DoesNotExist:
        remote_record = None
    assert remote_record is None


@pytest.mark.django_db
def test_take_subscription(client, add_test_user, auth, subscription):
    token = f"Bearer {auth.data['access']}"
    header = {'HTTP_AUTHORIZATION': token}
    response = client.get('/api/take-subscription', **header)
    assert response.data == SubscriptionSerializer(subscription).data


@pytest.mark.django_db
def test_take_fake_subscription(client, add_test_user, auth):
    token = f"Bearer {auth.data['access']}"
    header = {'HTTP_AUTHORIZATION': token}
    response = client.get('/api/take-subscription', **header)
    assert response.status_code == 400
