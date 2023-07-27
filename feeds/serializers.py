from rest_framework.serializers import ModelSerializer
from .models import Feed
from reviews.serializers import ReviewSerializer
from users.serializers import UserSerializer


class FeedSerializer(ModelSerializer):
    # feed 는 User의 자녀니까
    user = UserSerializer()
    review_set = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Feed
        fields = "__all__"
