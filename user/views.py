from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate, login, logout
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from base64 import b64decode
from rest_framework.authentication import BasicAuthentication

from user.serializers import UserModelSerializer

class LoginAPIView(APIView):
    permission_classes = [AllowAny,]

    def post(self, request, format=None):
        username = request.data.get("username", None)
        password = request.data.get("password", None)

        if not username or not password:
            raise AuthenticationFailed("Required credentials are not provided.")
        
        user = authenticate(request, username=username, password=password)
        if not user:
            raise AuthenticationFailed("Username or Password is invalide.")
        login(request, user)
        serializer = UserModelSerializer(user, context={"request":request})
        return Response(serializer.data)


class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated,]

    def post(self, request, format=None):
        logout(request)
        return Response()

        