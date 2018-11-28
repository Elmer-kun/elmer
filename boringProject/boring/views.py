# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render
from django.shortcuts import HttpResponse
from . import models
from moodLearning import moodout, createtestdata, inputdeal
import json
import random
import requests

# Create your views here.
def index(req):
    context = {}
    if req.POST:
        context['hisinput'] = req.POST['textinput']
    return render(req, 'boredIndex.html', context)


def textSubmit(req):
    context = {}
    if req.POST:
        textinput = models.textInput(text=req.POST['textinput'])
        textinput.save()
    # createtestdata.createData()  #创建基础数据用的，调一次就可以了
    context['hisinput'] = moodout.hisInput()
    context['mood'] = inputdeal.textdeal(req.POST['textinput'])
    return render(req, 'boredIndex.html', context)

@csrf_exempt
def dealSmallProgramPost(req):
    context = {}
    if req.POST:
        userid = req.POST['userid']
        usrname = req.POST['name']
        textinfo = req.POST['textinput']
        textinput = models.textInput(text=textinfo)
        # textinput.save()
        userinput = models.textLinkUser(text=textinfo, userid=userid, username=usrname, )
        userinput.save()
        print(textinput, userid, usrname)
    # context['hisinput'] = moodout.hisInput()
    texts = {'text':moodout.hisGetByUser(userid), 'mood':inputdeal.textdeal(textinfo)}
    return HttpResponse(json.dumps(texts))

@csrf_exempt
def dealSmallProgramDataCollect(req):
    context = {}
    if req.POST:
        # userid = request.POST['userid']
        # usrname = request.POST['name']
        textinfo = req.POST['textinput']
        mood = req.POST['mood']
        moodinput = models.textLinkMood(text=textinfo, mood=mood,)
        moodinput.save()
    texts = {'text':'sucess'}
    return HttpResponse(json.dumps(texts))

@csrf_exempt
def getMoodList(req):
    response_str = []
    moodmodel = models.moodModel.objects.filter(name=req.POST['moodmodel'])
    moodid = 1
    for moodm in moodmodel:
        moodid = moodm.id
    hislist = models.moodTextModel.objects.filter(name_id=moodid)[0:6]
    for his in hislist:
        response_str.append(his.text)
    moodlist = {'moodlist': response_str}
    return HttpResponse(json.dumps(moodlist))

def getMoodModel(req):
    response_str = []
    hislist = models.moodModel.objects.all()[0:6]
    for his in hislist:
        response_str.append(his.name)
    moodlist = {'moodlist': response_str}
    return HttpResponse(json.dumps(moodlist))

@csrf_exempt
def getSomeSentence(req):
    response_str = []
    sentences = models.textLinkKiding.objects.all()
    sentid = 1
    if sentences:
        sentid = random.randint(1,sentences.count())
    sen = models.textLinkKiding.objects.filter(id=sentid)
    if sen:
        for se in sen:
             response_str.append(se.text)
    else:
         response_str.append("It's a joke!")
    sentence = {'sen': response_str}
    return HttpResponse(json.dumps(sentence))

@csrf_exempt
def getOpenUserid(req):
    response_str = []
    code = req.POST['code']
    if code:
        url = 'https://api.weixin.qq.com/sns/jscode2session?appid=wxc89dfd93373e0cfd&secret=2084d2c4b8b8e28e00b8f64e2d5df881&grant_type=authorization_code&js_code='+code
        r = requests.get(url)
        # print(r.json())
        response_str.append(r.json()['openid'])
    sentence = {'userid': response_str}
    return HttpResponse(json.dumps(sentence))