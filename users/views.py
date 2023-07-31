from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, MyInfoSerializer
from .models import User


class UserInfo(APIView):
    def get(self, request):
        all_user = User.objects.all()
        serializer = UserSerializer(all_user, many=True)
        return Response(serializer.data)


# django의 기본적인 session을 이용한 로그인
# url : http://127.0.0.1:8000/api/v1/users/login
# Method : POST
from rest_framework.exceptions import ParseError
from django.contrib.auth import authenticate, login
from rest_framework import status


class Login(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        # 데이터가 비어서 오는 경우의 예외처리
        if not username or not password:
            return ParseError()

        user = authenticate(
            request,
            username=username,
            password=password,
        )

        if user:
            login(request, user)
            return Response(status.HTTP_200_OK)
        else:
            return Response(status.HTTP_404_NOT_FOUND)


from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import logout


class Logout(APIView):
    permission_classes = [IsAuthenticated]  # 로그인된 유저만 이 API 호출을 허용하겠다.and

    def post(self, request):
        logout(request)

        return Response({"data": "success"})


class MyInfo(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        if user:
            serializer = MyInfoSerializer(user)
            return Response(serializer.data)


import jwt
from django.conf import settings


class LoginJWT(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        # 데이터가 비어서 오는 경우의 예외처리
        if not username or not password:
            return ParseError()

        user = authenticate(
            request,
            username=username,
            password=password,
        )

        if user:
            jwt_token = jwt.encode(
                {"id": user.id, "username": user.username},
                settings.SECRET_KEY,
                algorithm="HS256",
            )

            return Response({"jwt_token": jwt_token})
