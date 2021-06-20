import datetime

import pytest

from api.models import App, CustomUser, IntegrationType, SubscriptionType, Subscription, Integration, GooglePlayReviews


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
def test_user():
    return CustomUser.objects.create_user(password='Password!!!',
                                          first_name='TestUser',
                                          last_name='TestUser',
                                          email='email@email.email')


@pytest.fixture
def test_admin():
    return CustomUser.objects.create_user(password='Password!!!',
                                          first_name='TestUser',
                                          last_name='TestUser',
                                          email='admin@admin.admin',
                                          is_superuser=True,
                                          is_staff=True)


@pytest.fixture
def auth(client, test_user):
    auth = client.post('/api/login',
                       {'email': 'email@email.email',
                        'password': 'Password!!!'})
    return auth


@pytest.fixture
def header_with_auth(client, test_user):
    auth = client.post('/api/login',
                       {'email': 'email@email.email',
                        'password': 'Password!!!'})
    token = f"Bearer {auth.data['access']}"
    header = {'HTTP_AUTHORIZATION': token}
    return header


@pytest.fixture
def auth_admin(client, test_admin):
    auth = client.post('/api/login',
                       {'email': 'admin@admin.admin',
                        'password': 'Password!!!'})
    return auth


@pytest.fixture
def header_with_auth_admin(client, test_admin):
    auth = client.post('/api/login',
                       {'email': 'admin@admin.admin',
                        'password': 'Password!!!'})
    token = f"Bearer {auth.data['access']}"
    header = {'HTTP_AUTHORIZATION': token}
    return header


@pytest.fixture
def integration_type():
    return IntegrationType.objects.create(name='test')


@pytest.fixture
def subscription_type():
    return SubscriptionType.objects.create(name='Test', price=1000, description='BlahBlah', max_app_count=100)


@pytest.fixture
def subscription(subscription_type, test_user):
    return Subscription.objects.create(
        user=test_user,
        subscription_type=subscription_type,
        expired_at=datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(days=10)
    )


@pytest.fixture
def integration(test_user, app, integration_type):
    integration = Integration.objects.create(
        user=test_user,
        app=app,
        slack_token='slack_token'
    )
    return integration


@pytest.fixture
def review(app):
    review = GooglePlayReviews.objects.create(
        app_id=app,
        text='TestTestTest',
        username='Eric Cartman',
        rating=5,
    )
    return review
