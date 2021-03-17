from rest_framework import generics
from rest_framework.response import Response
from api.auth.auth_serializer import RegisterSerializer


# Register API
from api.auth.obtain_token import MyTokenObtainPairSerializer


class RegisterApi(generics.GenericAPIView):
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
