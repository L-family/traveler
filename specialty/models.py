# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Specialty(models.Model):
    MARK = (
        ('0', '特产'),
        ('1', '服饰'),
    )
    name = models.CharField(max_length=50, verbose_name="名称")
    birthplace = models.CharField(max_length=100, verbose_name="产地")
    picture = models.ImageField(verbose_name="简介图")
    price = models.IntegerField(verbose_name="价格")
    detail = models.TextField(verbose_name="详细描述")
    mark = models.CharField(max_length=1, choices=MARK)


class SpecPict(models.Model):
    specId = models.ForeignKey(Specialty)
    picture = models.ImageField(verbose_name="详细图片")


class SpecUserCart(models.Model):
    STA = (
        ('0', '已加入购物车'),
        ('1', '已删除'),
    )
    specId = models.ForeignKey(Specialty)
    userId = models.ForeignKey(User)
    status = models.CharField(max_length=1, choices=STA)
    number = models.IntegerField(verbose_name="收藏数目")


class SpecUserStar(models.Model):
    STA = (
        ('0', '已收藏'),
        ('1', '已删除'),
    )
    specId = models.ForeignKey(Specialty)
    userId = models.ForeignKey(User)
    status = models.CharField(max_length=1, choices=STA)


