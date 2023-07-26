from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Feed
from .serializers import FeedSerializer


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
        print("username", username)

    def delete(self, request, username):
        pass
