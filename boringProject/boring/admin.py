# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from boring.models import moodModel, textInput, moodTextModel

# Register your models here.
admin.site.register([moodModel, textInput, moodTextModel])
