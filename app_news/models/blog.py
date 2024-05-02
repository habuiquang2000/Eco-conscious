from django.db import models
from django.contrib.auth.models import User

from .base import NewsCommon, NewsCommentCommon


# Create your models here.
class Blog(NewsCommon):
    pass


class BlogComment(NewsCommentCommon):
    blog = models.ForeignKey(
        to=Blog,
        on_delete=models.CASCADE,
        related_name="comments",
    )
