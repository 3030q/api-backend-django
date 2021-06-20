from django.urls import path

from . import views, slack_bot
from api.auth_and_registration import registration, logout, obtain_token
from rest_framework_simplejwt.views import TokenRefreshView

from api.apps import app_views
from api.subscription_and_payments import subscription_views
from api.integrations import integration_views
from api.reviews import review_views

urlpatterns = [
    path('health', views.health, name='index'),
    path('login', obtain_token.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('registration', registration.RegisterApi.as_view(), name='registration'),
    path('logout', logout.Logout.as_view(), name='logout'),
    # path('apps-list', app_views.apps_list, name='apps_list'),
    path('take-app', app_views.take_app, name='take_app'),
    path('add-app', app_views.add_app, name='add_app'),
    path('add-subscription', subscription_views.add_subscription, name='add_subscription'),
    path('remove-subscription', subscription_views.remove_subscription, name='remove_subscription'),
    path('remove-expired-subscription',
         subscription_views.remove_expired_subscription,
         name='remove_expired_subscription'),
    path('take-subscription', subscription_views.take_subscription, name='take_subscription'),
    path('integration-types', integration_views.take_all_integration_types, name='integration_types'),
    path('add-integration', integration_views.add_integration, name='add_integration'),
    path('integration-list', integration_views.take_integration_list, name='integration_list'),
    path('take-reviews', review_views.take_reviews, name='take_reviews'),
    path('take-user-info', registration.take_user_info, name='take_user_info'),
    path('slack/hello', slack_bot.hello, name='hello_slack_bot')

]

