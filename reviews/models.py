from django.db import models
from common.models import Commonmodel


class Review(Commonmodel):

    """Review model definition"""

    rcaption = models.CharField(max_length=60)
    reviewAuthor = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="review",
    )
    feed = models.ForeignKey(
        "feeds.Feed",
        on_delete=models.CASCADE,
        related_name="reviews",
    )
