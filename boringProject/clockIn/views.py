from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import HttpResponse
from . import models
import json


@csrf_exempt
def opt_clock(req):
    if req.POST:
        opt = req.POST['opt']
        if opt == 'se':
            texts = search_clock_text(req.POST['uid'])
        elif opt == 'up':
            texts = up_clock_text(req)
        elif opt == 'del':
            texts = del_clock_text(req)
        else:
            texts = add_clock_text(req)
    if not texts:
        texts = {'text': 'n'}
    return HttpResponse(texts)


@csrf_exempt
def clock_info(req):
    if req.POST:
        opt = req.POST['opt']
        if opt == 'add':
            texts = add_clock_info(req)
        else:
            texts = search_clock_info(req.POST['uid'])
    if not texts:
        texts = {'text': 'n'}
    return HttpResponse(texts)


def add_clock_info(req):
    c_len = req.POST['c_len']
    user_id = req.POST['uid']
    usr_name = req.POST['name']
    text_info = req.POST['text']
    info = models.UserClockInfo(clockInfo=text_info, userid=user_id, username=usr_name, clockLen=c_len,)
    info.save()
    texts = {'text': 'ok'}
    return HttpResponse(texts)


def search_clock_info(u_id):
    info = models.UserClockInfo.objects.filter(userid=u_id).order_by('endTime')[0:7]
    texts = {'text': info}
    return HttpResponse(texts)


def add_clock_text(req):
    if req.POST:
        user_id = req.POST['uid']
        usr_name = req.POST['name']
        text_info = req.POST['text']
        user_input = models.ClockText(clockInfo=text_info, userid=user_id, username=usr_name, )
        user_input.save()
    texts = {'text': 'ok'}
    return json.dumps(texts)


def del_clock_text(req):
    if req.POST:
        user_id = req.POST['uid']
        text_info = req.POST['text']
        user_input = models.ClockText.objects.filter(clockInfo=text_info, userid=user_id, )
        user_input.delete()
    texts = {'text': 'ok'}
    return json.dumps(texts)


def up_clock_text(req):
    user_id = req.POST['uid']
    t_id = req.POST['id']
    text_info = req.POST['text']
    user_input = models.ClockText.objects.filter(id=t_id)
    user_input.clockInfo = text_info
    user_input.save()
    texts = {'text': 'ok'}
    return json.dumps(texts)


def search_clock_text(u_id):
    response_str = []
    if u_id:
        user_input = models.ClockText.objects.filter(userId=u_id)
        if user_input:
            for usr in user_input:
                response_str.append(usr.clockInfo)
    texts = {'text': response_str}
    return json.dumps(texts)
