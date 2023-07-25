from django.db import models
from common.models import Common


class Review(Common):

    """Review model definition"""

    rcaption = models.CharField(max_length=60)
