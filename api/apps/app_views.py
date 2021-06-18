from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.models import App
from api.serializer import AppSerializer, AddAppSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_app(request):
    """
    Добавляет приложение приложение в общий пул
    """
    serializer = AddAppSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def take_app(request):
    """
    Берёт информацию, по конкретному приложению
    """
    app = App.objects.get(pk=request.data['app_id'])
    serializer = AppSerializer(app)
    if not app.active:
        return Response('Приложение не готово к использованию', status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.data, status=status.HTTP_200_OK)
