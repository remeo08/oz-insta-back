from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import User


class UserInfo(APIView):
    def get(self, request):
        all_user = User.objects.all()
        serializer = UserSerializer(all_user, many=True)
        return Response(serializer.data)
