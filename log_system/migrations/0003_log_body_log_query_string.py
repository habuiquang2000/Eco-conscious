# Generated by Django 4.2.7 on 2024-04-20 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_system', '0002_alter_log_endpoint_alter_log_state_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='body',
            field=models.TextField(blank=True, null=True, verbose_name='Body'),
        ),
        migrations.AddField(
            model_name='log',
            name='query_string',
            field=models.TextField(blank=True, null=True, verbose_name='Query'),
        ),
    ]
