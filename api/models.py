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
    count_reviews = models.IntegerField()


