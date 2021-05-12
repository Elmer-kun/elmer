from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import HttpResponse
from django.db.models import Sum
from . import models
import json
import datetime
# uid=odVNV425yvKRwX3EeUKwfIwfQS4A


@csrf_exempt
def opt_clock(req):
    texts = {}
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
    texts = {}
    if req.POST:
        opt = req.POST['opt']
        if opt == 'add':
            texts = add_clock_info(req)
        else:
            texts = search_clock_info(req.POST['uid'])
    if not texts:
        texts = {'text': 'n'}
    return HttpResponse(texts)


@csrf_exempt
def clock_collect(req):
    texts = {}
    if req.POST:
        texts = get_usr_clock_collect(req.POST['uid'])
    if not texts:
        texts = {'text': 'n'}
    return HttpResponse(texts)


@csrf_exempt
def clock_limit(req):
    texts = {}
    if req.POST:
        texts = search_clock_by_len(req.POST['uid'], req.POST['len'])
    if not texts:
        texts = {'text': 'n'}
    return HttpResponse(texts)


def add_clock_info(req):
    c_len = req.POST['c_len']
    user_id = req.POST['uid']
    usr_name = req.POST['name']
    text_info = req.POST['text']
    info = models.UserClockInfo(clockInfo=text_info, userId=user_id, username=usr_name, clockLen=c_len, )
    info.save()
    texts = {'text': 'ok'}
    return HttpResponse(texts)


def search_clock_info(u_id):
    infos = []
    hisinfo = models.UserClockInfo.objects.filter(userId=u_id,).order_by('-endTime')
    for info in hisinfo:
        inn = {'title': info.clockInfo, 'date': info.endTime, 'len': info.clockLen}
        infos.append(inn)
    texts = {'text': infos}
    return json.dumps(texts, cls=DateEncoder)


def add_clock_text(req):
    user_id = req.POST['uid']
    usr_name = req.POST['name']
    text_info = req.POST['text']
    user_input = models.ClockText(clockInfo=text_info, userId=user_id, username=usr_name, )
    user_input.save()
    texts = {'text': 'ok'}
    return json.dumps(texts)


def del_clock_text(req):
    user_id = req.POST['uid']
    text_id = req.POST['id']
    user_input = models.ClockText.objects.filter(id=text_id, userId=user_id, )
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
    info_ids = []
    if u_id:
        user_input = models.ClockText.objects.filter(userId=u_id)
        if user_input:
            for usr in user_input:
                info_ids.append(usr.id)
                response_str.append(usr.clockInfo)
    texts = {'text': response_str, 'ids': info_ids}
    return json.dumps(texts)


def search_clock_by_len(u_id, u_len):
    infos = []
    hisinfo = models.UserClockInfo.objects.filter(userId=u_id,).order_by('-endTime')[0: u_len]
    for info in hisinfo:
        inn = {'title': info.clockInfo, 'date': info.endTime, 'len': info.clockLen}
        infos.append(inn)
    texts = {'text': infos}
    return json.dumps(texts, cls=DateEncoder)


def get_usr_clock_collect(u_id):
    infos = []
    hisinfo = models.UserClockInfo.objects.filter(userId=u_id).values('clockInfo').annotate(cLen=Sum('clockLen'))
    for info in hisinfo:
        inn = {'title': info['clockInfo'], 'len': info['cLen']}
        infos.append(inn)
    texts = {'text': infos}
    return json.dumps(texts)


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')

        elif isinstance(obj, datetime.date):
            return obj.strftime("%Y-%m-%d")

        else:
            return json.JSONEncoder.default(self, obj)
