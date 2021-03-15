from jsonrpc.backend.django import api
from rest_framework import generics
from rest_framework.response import Response
from api.auth.auth_serializer import RegisterSerializer, UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken


# Register API
class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            'message': "User created successfully!",
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })
