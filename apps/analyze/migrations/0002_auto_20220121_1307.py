# Generated by Django 2.2.20 on 2022-01-21 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyze', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requestrecord',
            name='liked_articles',
        ),
        migrations.AddField(
            model_name='requestrecord',
            name='access_time',
            field=models.DateTimeField(auto_now=True, verbose_name='访问时间'),
        ),
    ]