import jwt  # poetry add pyjwt 설치
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.conf import settings
from users.models import User


class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        jwt_token = request.headers.get("jwt-token")

        # jwt_token이 없으면 패스
        if not jwt_token:
            print("jwt_token None")
            return None

        decoded = jwt.decode(
            jwt_token,
            settings.SECRET_KEY,
            algorithms=["HS256"],
        )

        print("decoded", decoded)

        user_id = decoded.get("id")
        user_name = decoded.get("username")

        if not user_id and not user_name:
            return AuthenticationFailed("Invalid Token")

        user = User.objects.get(id=user_id)

        return (user, None)
