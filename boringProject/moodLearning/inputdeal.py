# -*- coding: utf-8 -*-
from boring import models
import difflib

def textdeal(text):
    like_ratio = 0
    moodcate = models.textLinkMood.objects.all()
    for mood in moodcate:
        ratio = checkStrLike(text, mood.text)
        if(ratio >= like_ratio):
            like_ratio = ratio
            textmood = mood
    if not textmood:
        return '竟然没猜不到'
    return textmood.mood

def checkStrLike(s1, s2):
    return difflib.SequenceMatcher(None, s1, s2).quick_ratio()


