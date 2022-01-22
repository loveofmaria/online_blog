from django.db import models


# 访问网站的 ip 地址、端点和次数
class RequestRecord(models.Model):
    ip = models.CharField(verbose_name='IP 地址', max_length=30, editable=False)
    location = models.CharField(verbose_name='IP 地理位置', max_length=30, editable=False)
    os_info = models.CharField(verbose_name='系统', max_length=16, editable=False)
    browser = models.CharField(verbose_name='浏览器', max_length=128, editable=False)
    access_time = models.DateTimeField('访问时间', auto_now_add=True, editable=False)

    class Meta:
        verbose_name = '访问记录'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "[IP: %s  地址: %s]" % (self.ip, self.location)

    # def update_articles(self, article, *args, **kwargs):
    #     self.liked_articles.add(article)
    #     self.save(update_fields=['liked_articles'])

# # 网站总访问次数
# class VisitNumber(models.Model):
#     count = models.IntegerField(verbose_name='网站访问总次数', default=0)  # 网站访问总次数
#
#     class Meta:
#         verbose_name = '网站访问总次数'
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return str(self.count)
#
#
# # 单日访问量统计
# class DayNumber(models.Model):
#     day = models.DateField(verbose_name='日期', auto_now=True)
#     count = models.IntegerField(verbose_name='网站访问次数', default=0)  # 网站访问总次数
#
#     class Meta:
#         verbose_name = '网站日访问量统计'
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return str(self.day)
