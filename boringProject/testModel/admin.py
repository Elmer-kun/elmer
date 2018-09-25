# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from testModel.models import usrModel, Tag, Contact

# Register your models here.
# admin.register([usrModel])
class ContactAdmin(admin.ModelAdmin):
    fields = ('name', 'email')


admin.site.register(Contact, ContactAdmin)
admin.site.register([usrModel, Tag])