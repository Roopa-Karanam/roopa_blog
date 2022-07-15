# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 15:19:35 2022

@author: karan
"""
from django.db.models import Count
from . import models


def base_context(request):
        topics =  models.Topic.objects.annotate(Count('blogroopa_posts')) \
        .order_by('-blogroopa_posts__count')[:10]

        return {'topics': topics}
