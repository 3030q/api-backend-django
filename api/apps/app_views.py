from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.models import App
from api.serializer import AppSerializer


# @permission_classes([IsAuthenticated])
# @api_view(['GET'])
# def apps_list(request):
#     apps = App.objects.filter(user_id=request.user.id).all()
#     serializer = AppSerializer(data=apps, many=True)
#     return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_app(request):
    """
    Добавляет приложение приложение в общий пул
    """
    serializer = AppSerializer(data=request.data)
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
    return Response(serializer.data, status=status.HTTP_200_OK)
