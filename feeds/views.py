from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Feed
from .serializers import FeedSerializer
from users.models import User


class AllFeeds(APIView):
    def get(self, request):
        all_feeds = Feed.objects.all()
        serializer = FeedSerializer(all_feeds, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FeedSerializer(data=request.data)
        if serializer.is_valid():
            feed = serializer.save()
            return Response(FeedSerializer(feed).data)
        else:
            return serializer.errors


class UserNameFeeds(APIView):
    def get(self, request, username):
        user = User.objects.get(username=username)

        try:
            feeds = Feed.objects.filter(user=user)
        except Feed.DoesNotExist:
            raise NotFound

        serializer = FeedSerializer(feeds, many=True)
        return Response(serializer.data)
