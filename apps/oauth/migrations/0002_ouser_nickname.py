# Generated by Django 2.2.20 on 2022-01-07 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ouser',
            name='nickname',
            field=models.CharField(default='无名氏', help_text='代替帐号显示在评论或者文章作者栏', max_length=64, unique=True, verbose_name='昵称'),
        ),
    ]
