
import datetime

import pytest

from api.models import App, CustomUser, IntegrationType, SubscriptionType, Subscription


@pytest.fixture()
def app():
    app = App.objects.create(
        name='Test',
        url='Test.com/test/test',
        ratings=5.0,
        dev_name='Testus',
        version='v.2',
        last_modified=datetime.datetime.now(tz=datetime.timezone.utc),
        count_reviews=1000,
        platform='Google Play',
        active=True
    )
    return app


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


@pytest.fixture
def integration_type():
    return IntegrationType.objects.create(name='test')


@pytest.fixture
def subscription_type():
    return SubscriptionType.objects.create(name='Test', price=1000, description='BlahBlah', max_app_count=100)


@pytest.fixture
def subscription(subscription_type, add_test_user):
    return Subscription.objects.create(
        user=add_test_user,
        subscription_type=subscription_type,
        expired_at=datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(days=10)
    )

