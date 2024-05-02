from django.db import models
from django.contrib.auth.models import User

from .base import NewsCommon, NewsCommentCommon


# Create your models here.
class Gallery(NewsCommon):
    user = models.ForeignKey(
        to=User,
        null=True,
        on_delete=models.SET_NULL,
        related_name='user_created',
    )


class GalleryComment(NewsCommentCommon):
    blog = models.ForeignKey(
        to=Gallery,
        on_delete=models.CASCADE,
        related_name="comments",
    )
