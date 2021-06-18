from datetime import datetime, timezone

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status

from api.models import Subscription
from api.serializer import SubscriptionSerializer


@api_view(['Post'])
@permission_classes([IsAuthenticated])
def add_subscription(request):
    """
    Добавляет подписку для пользователя (заглушка!!!, необходима логика для отслеживания пайментов и др.)
    """
    if Subscription.objects.filter(user_id=request.user.id).count() >= 1:
        return Response("Данный пользователь уже имеет подписку", status=status.HTTP_400_BAD_REQUEST)
    serializer = SubscriptionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['Get'])
@permission_classes([IsAuthenticated])
def remove_subscription(request):
    """
    Отменяет подписку
    """
    sub = Subscription.objects.filter(user_id=request.user.id, expired_at__gt=datetime.now(tz=timezone.utc))
    if sub.count() < 1:
        return Response("У данного пользователя нет подписки, или она истекла", status=status.HTTP_400_BAD_REQUEST)
    else:
        Subscription.objects.filter(user_id=request.user.id).delete()
        return Response({'result': "Подписка отменена"}, status=status.HTTP_205_RESET_CONTENT)


@api_view(['Get'])
@permission_classes([IsAuthenticated])
def take_subscription(request):
    """
    Достает информацию о подписке пользователя, если она есть
    """
    sub = Subscription.objects.filter(user_id=request.user.id, expired_at__gt=datetime.now(tz=timezone.utc))
    if sub.count() < 1:
        return Response("У данного пользователя нет подписки, или она истекла", status=status.HTTP_400_BAD_REQUEST)
    else:
        serializer = SubscriptionSerializer(sub.get())
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['Get'])
@permission_classes([IsAdminUser])
def remove_expired_subscription(request):
    """
    Удаляет из базы все подписки, чей срок истёк (Доступно только админу) TODO: вынести это в очередь задач
    """
    Subscription.objects.filter(expired_at__lt=datetime.now(tz=timezone.utc)).delete()
    return Response("Удалены все истекшие подписки", status=status.HTTP_205_RESET_CONTENT)
