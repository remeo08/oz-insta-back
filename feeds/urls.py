from django.urls import path
from .views import AllFeeds

urlpatterns = [
    path("", AllFeeds.as_view()),  # 전체 게시글을 가져옴
    # path("<str:username>", UserNameFeeds.as_view()),  # 특정 유저가 작성한 게시글만 가져옴
]
