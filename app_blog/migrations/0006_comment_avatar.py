# Generated by Django 4.2.7 on 2024-04-20 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0005_alter_comment_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='avatar',
            field=models.ImageField(default='/_default/user/auser.jpg', upload_to='comment/avatar/%Y/%m/%d/'),
        ),
    ]