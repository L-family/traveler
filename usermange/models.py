# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Customer(models.Model):
    """
    客户信息，继承user表，包含地址等基础信息
    """
    id = models.ForeignKey(User)
    phone = models.CharField(max_length=11, verbose_name="联系方式")
    profile = models.ImageField(verbose_name="个人头像")
    address = models.CharField(max_length=100, verbose_name="收货地址")
    name = models.CharField(max_length=40, verbose_name="昵称")

