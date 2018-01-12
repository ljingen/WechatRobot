# -*- coding: utf-8 -*-
# filename :urls.py

from django.conf.urls import url, include
from .handle import HandleView

urlpatterns = [
    #  用户个人中心页面
    url(r'^wx/$', HandleView.as_view(), name='base_token'),
]