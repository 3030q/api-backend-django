from datetime import datetime, timezone

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from api.models import Subscription, Integration, App, IntegrationType
from api.serializer import IntegrationSerializer, IntegrationTypeSerializer


@api_view(['Post'])
@permission_classes([IsAuthenticated])
def add_integration(request):
    try:
        subscribe = Subscription.objects.get(user_id=request.user.id, expired_at__gt=datetime.now(tz=timezone.utc))
    except Subscription.DoesNotExist:
        return Response("У данного пользователя нет подписки", status=status.HTTP_400_BAD_REQUEST)

    try:
        integrations_count = Integration.objects.filter(user_id=request.user.id).count()
    except Subscription.DoesNotExist:
        integrations_count = 0

    if integrations_count >= subscribe.subscription_type.max_app_count:
        return Response("Количество доступных интеграций закончилось", status=status.HTTP_400_BAD_REQUEST)

    try:
        integration_type_id = IntegrationType.objects.get(pk=request.data['integration_type_id']).id
    except IntegrationType.DoesNotExist:
        return Response("Неверный тип интеграции", status=status.HTTP_400_BAD_REQUEST)

    try:
        app_id = App.objects.get(url=request.data['app_url']).id
    except App.DoesNotExist:
        app_id = App.objects.create(url=request.data['app_url']).id
    serializer = IntegrationSerializer(
        data={'user': request.user.id, 'app': app_id, 'integration_type': integration_type_id})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['Get'])
def take_all_integration_types(request):
    serializer = IntegrationTypeSerializer(IntegrationType.objects.all(), many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['Get'])
@permission_classes([IsAuthenticated])
def take_integration_list(request):
    serializer = IntegrationSerializer(Integration.objects.filter(user=request.user.id).all(), many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

