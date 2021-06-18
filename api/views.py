from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from jsonrpc.backend.django import api


@api_view(['GET'])
def health(request):
    """
    Пинг проверки сервера
    """
    return Response({'hello': 'hello'})
