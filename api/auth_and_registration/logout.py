from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status


class Logout(APIView):
    """
    Выход из аккаунта и добавления токенов(access/refresh) в черный список
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            # access_token = request.data["access"]
            # access_token.blacklist()
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'result': 'Logout was successful'}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"exception": e}, status=status.HTTP_400_BAD_REQUEST)
