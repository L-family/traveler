# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Base(models.Model):
    name = models.CharField(max_length=40, verbose_name="基地名称")
    address = models.CharField(max_length=100, verbose_name="基地地址")
    phone = models.CharField(max_length=11, verbose_name="联系方式")
    lowPrice = models.IntegerField(verbose_name="最低价格")
    highPrice = models.IntegerField(verbose_name="最高价格")
    detail = models.TextField(verbose_name="详细描述")
    picture = models.ImageField(verbose_name="简介图片")


class BasePict(models.Model):
    baseId = models.ForeignKey(Base)
    picture = models.ImageField(verbose_name="详细图片")


class BaseUser(models.Model):
    STATUS = (
        ('0', '取消收藏'),
        ('1', '收藏'),
    )
    baseId = models.ForeignKey(Base)
    userId = models.ForeignKey(User)
    status = models.CharField(max_length=1, verbose_name='收藏状态',
                              choices=STATUS)

