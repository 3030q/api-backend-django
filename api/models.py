from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class App(models.Model):
    name = models.CharField(max_length=50, default=None, blank=True, null=True)
    url = models.CharField(max_length=255, default=None, blank=True, null=True, unique=True)
    ratings = models.FloatField(default=None, blank=True, null=True)
    dev_name = models.CharField(max_length=50, default=None, blank=True, null=True)
    version = models.CharField(max_length=50, default=None, blank=True, null=True)
    last_modified = models.DateTimeField(default=None, blank=True, null=True)
    last_update_info = models.DateTimeField(auto_now=True, blank=True, null=True)
    count_reviews = models.IntegerField(default=None, blank=True, null=True)
    platform = models.CharField(max_length=50, default=None, blank=True, null=True)
    active = models.BooleanField(default=False)


class GooglePlayReviews(models.Model):
    app_id = models.ForeignKey(App, on_delete=models.CASCADE, db_column='app_id')
    username = models.CharField(max_length=255, default=None, blank=True, null=True)
    text = models.TextField(default=None, blank=True, null=True)
    posted_at = models.DateTimeField(default=None, blank=True, null=True)
    avatar_link = models.CharField(max_length=255, default=None, blank=True, null=True)
    rating = models.IntegerField(default=None, blank=True, null=True)
    relevance = models.IntegerField(default=None, blank=True, null=True)


class AppStoreReviews(models.Model):
    app_id = models.ForeignKey(App, on_delete=models.CASCADE, db_column='app_id')
    username = models.CharField(max_length=255, default=None, blank=True, null=True, unique=True)
    text = models.TextField(default=None, blank=True, null=True)
    rating = models.IntegerField(default=None, blank=True, null=True)
    relevance = models.IntegerField(default=None, blank=True, null=True)
    app_version = models.CharField(max_length=255, default=None, blank=True, null=True)


class AppGalleryReviews(models.Model):
    app_id = models.ForeignKey(App, on_delete=models.CASCADE, db_column='app_id')
    username = models.CharField(max_length=255, default=None, blank=True, null=True)
    text = models.TextField(default=None, blank=True, null=True)
    posted_at = models.DateTimeField(default=None, blank=True, null=True)
    avatar_link = models.CharField(max_length=255, default=None, blank=True, null=True)
    rating = models.IntegerField(default=None, blank=True, null=True)
    relevance = models.IntegerField(default=None, blank=True, null=True)
    app_version = models.CharField(max_length=255, default=None, blank=True, null=True)


class SubscriptionType(models.Model):
    name = models.CharField(max_length=50, unique=True)
    price = models.FloatField()
    description = models.TextField(default=None, blank=True, null=True)
    max_app_count = models.IntegerField()

    class Meta:
        db_table = 'api_subscription_type'


class Subscription(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, db_column='user_id')
    subscription_type = models.ForeignKey(
        SubscriptionType,
        on_delete=models.CASCADE,
        db_column='subscription_type_id'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    expired_at = models.DateTimeField()


class IntegrationType(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'api_integration_type'


class Integration(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, db_column='user_id')
    app = models.ForeignKey(App, on_delete=models.CASCADE, db_column='app_id')
    slack_token = models.CharField(max_length=255, default=None, blank=True, null=True)
