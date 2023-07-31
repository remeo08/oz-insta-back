from django.urls import path
from .views import UserInfo, Login, Logout, MyInfo, LoginJWT
from rest_framework.authtoken.views import obtain_auth_token


# url : http://127.0.0.1:8000/api/v1/users/login
# url : http://127.0.0.1:8000/api/v1/users/getToken

urlpatterns = [
    path("myInfo", MyInfo.as_view()),
    path("login", Login.as_view()),  # django session 로그인 처리
    path("logout", Logout.as_view()),  # django session 로그아웃 처리
    path("getToken", obtain_auth_token),
    path("loginJWT", LoginJWT.as_view()),
]

# API test program
# - POSTMAN
# - VSC: thunder client
