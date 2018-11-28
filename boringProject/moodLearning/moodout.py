# -*- coding: utf-8 -*-
from boring import models
from django.shortcuts import HttpResponse

def hisInput():
    response_str = []
    hislist = models.textInput.objects.order_by('-id')[0:10]
    for his in hislist:
        response_str.append(his.text)
    return response_str

def hisGet(requeset):
    response_str = []
    hislist = models.textInput.objects.order_by('-id')[0:10]
    for his in hislist:
        response_str.append(his.text)
    return HttpResponse(response_str)

def hisGetByUser(usrid):
    response_str = []
    hislist = models.textLinkUser.objects.filter(userid=usrid).order_by('-id')[0:10]
    for his in hislist:
        response_str.append(his.text)
    return response_str

