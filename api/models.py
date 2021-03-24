from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

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
