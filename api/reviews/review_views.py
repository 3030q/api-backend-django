from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.models import Review, App, Integration
from api.integrations.integration_serializer import IntegrationIdRequestSerializer
from api.reviews.review_serializer import AppIdRequestSerializer
from api.serializer import ReviewSerializer


@api_view(['Post'])
@permission_classes([IsAuthenticated])
def take_reviews(request):
    try:
        integration = Integration.objects.filter(
            pk=IntegrationIdRequestSerializer(request.data).data['integration_id'],
            user=request.user.id
        ).get()
    except Integration.DoesNotExist:
        return Response('Данной интеграции не существует, или она недоступна для этого пользователя',
                        status=status.HTTP_400_BAD_REQUEST)
    reviews = ReviewSerializer(Review.objects.filter(app_id=integration.app.id).all(), many=True)
    return Response(reviews.data, status=status.HTTP_200_OK)
