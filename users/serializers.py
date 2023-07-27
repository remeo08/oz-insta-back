from rest_framework.serializers import ModelSerializer
from .models import User

# from feeds.serializers import FeedSerializer


class UserSerializer(ModelSerializer):
    # feeds = FeedSerializer(many=True)

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "username",
            "profileImg",
            "profileIntroduce",
        )
