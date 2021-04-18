import datetime

import pytest

from api.models import SubscriptionType, Subscription
from api.serializer import SubscriptionSerializer


@pytest.mark.django_db
def test_add_subscription(client, test_user, header_with_auth, subscription_type):
    response = client.post('/api/add-subscription',
                           {
                               'user': test_user.id,
                               'subscription_type': subscription_type.id,
                               'expired_at': datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(days=10)
                           }, **header_with_auth)
    assert Subscription.objects.get(pk=response.data['id']).user.id == test_user.id


@pytest.mark.django_db
def test_remove_subscription(client, header_with_auth, subscription):
    response = client.get('/api/remove-subscription', **header_with_auth)
    try:
        remote_record = Subscription.objects.get(pk=subscription.id)
    except Subscription.DoesNotExist:
        remote_record = None
    assert remote_record is None


@pytest.mark.django_db
def test_remove_expired_subscription(client, header_with_auth_admin, subscription):
    subscription.expired_at -= datetime.timedelta(days=30)
    subscription.save()
    assert Subscription.objects.get(pk=subscription.id)
    response = client.get('/api/remove-expired-subscription', **header_with_auth_admin)
    try:
        remote_record = Subscription.objects.get(pk=subscription.id)
    except Subscription.DoesNotExist:
        remote_record = None
    assert remote_record is None


@pytest.mark.django_db
def test_take_subscription(client, header_with_auth, subscription):
    response = client.get('/api/take-subscription', **header_with_auth)
    assert response.data == SubscriptionSerializer(subscription).data


# Суть теста в том, что мы не добавили подписку для пользователя
@pytest.mark.django_db
def test_take_fake_subscription(client, header_with_auth):
    response = client.get('/api/take-subscription', **header_with_auth)
    assert response.status_code == 400
