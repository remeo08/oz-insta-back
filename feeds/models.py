from django.db import models
from common.models import Commonmodel


class Feed(Commonmodel):

    """Feed model definition"""

    caption = models.CharField(max_length=200)
    contentImg = models.URLField()
    likesNum = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )
