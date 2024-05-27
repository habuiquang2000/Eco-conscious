from django.db import models
from django.contrib.auth.models import User

from .base import NewsCommon, NewsCommentCommon


# Create your models here.
class Blog(NewsCommon):
    moderation = models.BooleanField(
        verbose_name="Đã kiểm duyệt",
        default=False
    )


class BlogComment(NewsCommentCommon):
    blog = models.ForeignKey(
        to=Blog,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    moderation = models.BooleanField(
        verbose_name="Đã kiểm duyệt",
        default=False
    )
