from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class Ouser(AbstractUser):
    link = models.URLField('个人网址', blank=True, help_text='提示：网址必须填写以http开头的完整形式')
    avatar = ProcessedImageField(upload_to='avatar/%Y/%m/%d',
                                 default='avatar/default.png',
                                 verbose_name='头像',
                                 processors=[ResizeToFill(80, 80)]
                                 )
    nickname = models.CharField('昵称', max_length=64, unique=True, null=False, blank=False, default='无名氏')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __str__(self):
        return self.nickname

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.nickname == '无名氏':
            self.nickname = self.nickname + '-' + str(self.id)
            super().save(update_fields=['nickname'])
