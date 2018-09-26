from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class News(models.Model):
    MARK = (
        ('0', '养生'),
        ('1', '文体艺术'),
        ('2', '孝道文化')
    )
    title = models.CharField(max_length=100, verbose_name="标题")
    detail = models.TextField(verbose_name="详细信息")
    mark = models.CharField(max_length=1, verbose_name="分类",
                            choices=MARK)
    picture = models.ImageField(verbose_name="图片")


class NewsPict(models.Model):
    newsId = models.ForeignKey(News)
    picture = models.ImageField()


class NewsUser(models.Model):
    STATUS = (
        ('0', '收藏'),
        ('1', '取消收藏'),
    )
    newsId = models.ForeignKey(News)
    userId = models.ForeignKey(User)
    status = models.CharField(max_length=1, choices=STATUS)