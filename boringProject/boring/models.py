# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

# 心情模型，包含各种心情
class moodModel(models.Model):
    name = models.CharField(max_length=20)
    createDate = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.name

# 心情对应的关键字，一个心情可能有多个关键字，同时会有多条记录
class moodTextModel(models.Model):
    text = models.CharField(max_length=150)
    name = models.ForeignKey(moodModel, on_delete=models.CASCADE)
    createDate = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.text

# 提交的内容
class textInput(models.Model):
    text = models.CharField(max_length=150)
    createDate = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.text


# 提交的内容和用户名关联起来
class textLinkUser(models.Model):
    userid = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    text = models.CharField(max_length=150)
    createDate = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.text


# 提交的内容和心情关联起来,测试数据
class textLinkMood(models.Model):
    mood = models.CharField(max_length=50)
    text = models.CharField(max_length=150)
    createDate = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.text


# 提交的内容和心情关联起来,测试数据
class textLinkKiding(models.Model):
    mood = models.CharField(max_length=50)
    text = models.CharField(max_length=150)
    createDate = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.text