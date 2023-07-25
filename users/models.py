from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    """User model definition"""

    profileImg = models.URLField(blank=True)
    profileIntroduce = models.CharField(max_length=120)
    followerNum = models.PositiveIntegerField(default=0)
    followingNum = models.PositiveIntegerField(default=0)
