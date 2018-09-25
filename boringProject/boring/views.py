# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render
from django.shortcuts import HttpResponse
from . import models
from moodLearning import moodout
import json

# Create your views here.
def index(request):
    context = {}
    if request.POST:
        context['hisinput'] = request.POST['textinput']
    return render(request, 'boredIndex.html', context)


def textSubmit(request):
    context = {}
    if request.POST:
        textinput = models.textInput(text=request.POST['textinput'])
        textinput.save()
    context['hisinput'] = moodout.hisInput()
    return render(request, 'boredIndex.html', context)

@csrf_exempt
def dealSmallProgramPost(request):
    context = {}
    if request.POST:
        userid = request.POST['userid']
        usrname = request.POST['name']
        textinfo = request.POST['textinput']
        textinput = models.textInput(text=textinfo)
        # textinput.save()
        userinput = models.textLinkUser(text=textinfo, userid=userid, username=usrname, )
        userinput.save()
        print(textinput, userid, usrname)
    context['hisinput'] = moodout.hisInput()
    return HttpResponse(json.dumps(moodout.hisGetByUser(userid)))