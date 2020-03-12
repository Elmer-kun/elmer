# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone


class ClockText(models.Model):
    userId = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    clockInfo = models.CharField(max_length=200)
    createDate = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.clockInfo


class UserClockInfo(models.Model):
    userId = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    clockInfo = models.CharField(max_length=200)
    startTime = models.DateTimeField(default=timezone.now())
    endTime = models.DateTimeField(default=timezone.now())
    clockLen = models.IntegerField(default=0)

    def __unicode__(self):
        return self.clockInfo
