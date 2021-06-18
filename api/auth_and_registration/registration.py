from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from api.auth_and_registration.auth_and_register_serializer import RegisterSerializer, UserSerializer

# Register API
from api.auth_and_registration.obtain_token import MyTokenObtainPairSerializer
from api.models import CustomUser


class RegisterApi(generics.GenericAPIView):
    """
    Регистрирует пользователя, выдавая ему access/refresh token
    """
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = MyTokenObtainPairSerializer.get_token(user)
        return Response({
            'message': "User created successfully!",
            'refresh': str(token),
            'access': str(token.access_token),
        })


@api_view(['Get'])
@permission_classes([IsAuthenticated])
def take_user_info(request):
    user = CustomUser.objects.get(pk=request.user.id)
    serializer = UserSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)