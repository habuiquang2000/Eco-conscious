from django.db import models
from django.contrib.auth.models import User

from .base import NewsCommon, NewsCommentCommon


# Create your models here.
class Event(NewsCommon):
    pass


class EventComment(NewsCommentCommon):
    blog = models.ForeignKey(
        to=Event,
        on_delete=models.CASCADE,
        related_name="comments",
    )
