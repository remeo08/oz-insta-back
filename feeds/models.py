from django.db import models
from common.models import Common


class Feed(Common):

    """Feed model definition"""

    caption = models.CharField(max_length=200)
    contentImg = models.URLField()
    likesNum = models.PositiveIntegerField(default=0)
