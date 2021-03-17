from jsonrpc.backend.django import api
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.state import User
from django.core import serializers


@api_view(['GET'])
def index(request):
    a = 1337
    return Response({'sse': a})


@api.dispatcher.add_method
def my_method(request, *args, **kwargs):
    obj = serializers.serialize("json", User.objects.all())
    return obj

