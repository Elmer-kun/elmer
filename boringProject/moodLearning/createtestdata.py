# -*- coding: utf-8 -*-
from boring import models
import random

def createData():
    texts = models.textInput.objects.all()
    for text in texts:
        size = models.moodTextModel.objects.count()
        rand_id = random.randint(1, size)
        moodata = models.moodTextModel.objects.get(id=rand_id)
        text_mood = models.textLinkMood(mood=moodata.text, text=text.text)
        text_mood.save()


