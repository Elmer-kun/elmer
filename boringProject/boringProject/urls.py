"""boringProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from testModel import models, views, testdb, search, search2
from boring import views
from moodLearning import moodout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name="index"),
    url(r'^textsubmit', views.textSubmit),
    url(r'^gettext', moodout.hisGet),
    url(r'^posttext', views.dealSmallProgramPost),
    url(r'^getmoodlist', views.getMoodList),
    url(r'^getmoodmodel', views.getMoodModel),
    url(r'^collectmood', views.dealSmallProgramDataCollect),
    url(r'^getSentence', views.getSomeSentence),
    url(r'^getOpenid', views.getOpenUserid),
    # url(r'^testdb', testdb.testdb, name="testdb"),
    # url(r'^search-form', search.search_form),
    # url(r'^search-post$', search2.search_post),
    # url(r'^search$', search.search),
]
