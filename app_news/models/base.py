from django.db import models
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField


# Create your models here.
class NewsCommon(models.Model):
    user = models.ForeignKey(
        to=User,
        null=True,
        on_delete=models.SET_NULL,
        # related_name='user_created',
    )

    title = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    description = models.TextField(
        blank=True,
        null=True
    )
    content = RichTextField(
        blank=True,
        null=True
    )
    image = models.ImageField(
        upload_to='blog/%Y/%m/%d/',
        default="/_default/blog/bf4.jpg"
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        abstract = True


class NewsCommentCommon(models.Model):
    user = models.ForeignKey(
        to=User,
        null=True,
        on_delete=models.SET_NULL,
        # related_name='user_comment',
    )
    comment_to_reply = models.ForeignKey(
        to="self",
        null=True,
        on_delete=models.CASCADE,
        related_name='replies',
    )

    fullname = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    avatar = models.ImageField(
        upload_to='comment/avatar/%Y/%m/%d/',
        default="/_default/user/auser.jpg"
    )
    content = RichTextField(
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        abstract = True
