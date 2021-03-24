from django.test import TestCase
import pytest

# Create your tests here.
from rest_framework.utils import json


def test_get_token(client):
    response = client.get('/api/health')
    assert response.json()['hello'] == 'hello'
