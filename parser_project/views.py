from django.http import HttpResponse
from jsonrpc.backend.django import api
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def index(request):
    a = 1337
    return Response({'sse': a})


@api.dispatcher.add_method
def my_method(request, *args, **kwargs):
    return args, kwargs
