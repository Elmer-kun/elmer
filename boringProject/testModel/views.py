# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    context['hello'] = 'hello world.'
    # return HttpResponse("Hello world.")
    return render(request, 'hello.html', context)