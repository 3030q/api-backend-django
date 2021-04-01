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
    name = models.CharField(max_length=50, unique=True)
    url = models.SlugField()
    ratings = models.FloatField(default=None, blank=True, null=True)
    dev_name = models.CharField(max_length=50, default=None, blank=True, null=True)
    version = models.CharField(max_length=50, default=None, blank=True, null=True)
    last_modified = models.DateTimeField(default=None, blank=True, null=True)
    last_update_info = models.DateTimeField(auto_now=True, blank=True, null=True)
    count_reviews = models.IntegerField(default=None, blank=True, null=True)
    platform = models.CharField(max_length=50, default=None, blank=True, null=True)


class Review(models.Model):
    app = models.ForeignKey(App, on_delete=models.CASCADE)
    description = models.TextField(default=None, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_info = models.DateTimeField(auto_now=True, blank=True, null=True)
    commentator_name = models.CharField(max_length=50, default=None, blank=True, null=True)
    rating = models.IntegerField(default=None, blank=True, null=True)
    is_notified = models.BooleanField(default=False)
    language = models.CharField(max_length=50, default=None, blank=True, null=True)


class SubscriptionType(models.Model):
    name = models.CharField(max_length=50, unique=True),
    price = models.FloatField()
    description = models.TextField(default=None, blank=True, null=True)

    class Meta:
        db_table = 'api_subscription_type'


class Subscription(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    subscription_type_id = models.ForeignKey(SubscriptionType, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    expired_at = models.DateTimeField()


class IntegrationType(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'api_integration_type'


class Integration(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    app_id = models.ForeignKey(App, on_delete=models.CASCADE)
    integration_type_id = models.ForeignKey(IntegrationType,
                                            on_delete=models.CASCADE)
