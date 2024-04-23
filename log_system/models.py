from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.


class LogStatus(models.TextChoices):
    PROCESS = 'PROCESS', _('Đang xử lý')
    PENDDING = 'PENDDING', _('Chờ đợi')
    SUCCESS = 'SUCCESS', _('Thành công')
    ERROR = 'ERROR', _('Thất bại')


class Log(models.Model):  # Danh mục
    method = models.CharField(
        max_length=10,
        verbose_name="Phương thức"
    )
    endpoint = models.TextField(
        verbose_name="Đường dẫn"
    )
    status_code = models.IntegerField(
        verbose_name="Mã HTTP",
    )
    state_message = models.CharField(
        max_length=100,
        verbose_name="Đường dẫn"
    )

    query_string = models.TextField(
        null=True,
        blank=True,
        verbose_name="Query"
    )
    body = models.TextField(
        null=True,
        blank=True,
        verbose_name="Body"
    )

    # state_message = models.CharField(
    #     verbose_name="Trạng thái",
    #     max_length=50,
    #     choices=LogStatus.choices,
    #     default=LogStatus.PROCESS,
    # )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Thời giann"
    )

    scheme = models.CharField(
        max_length=8,
        verbose_name="SSL"
    )
    domain = models.CharField(
        max_length=255,
        verbose_name="Miền"
    )
    ip = models.CharField(
        max_length=255,
        verbose_name="Địa chỉ"
    )

    machinename = models.CharField(
        max_length=255,
        verbose_name="Tên máy"
    )
    machineinfo = models.CharField(
        max_length=255,
        verbose_name="Thông tin thiết bị"
    )
