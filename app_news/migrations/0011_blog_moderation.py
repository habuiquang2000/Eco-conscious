# Generated by Django 4.2.7 on 2024-05-27 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0010_blogcomment_moderation'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='moderation',
            field=models.BooleanField(default=False, verbose_name='Đã kiểm duyệt'),
        ),
    ]
