from django.urls import path

from . import views
from api.auth_and_registration import registration, logout, obtain_token
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('health', views.health, name='index'),
    path('login', obtain_token.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('registration', registration.RegisterApi.as_view(), name='registration'),
    path('logout', logout.Logout.as_view(), name='logout'),
]

