# Generated by Django 2.2.20 on 2022-01-21 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyze', '0002_auto_20220121_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestrecord',
            name='access_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='访问时间'),
        ),
    ]
