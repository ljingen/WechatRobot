# -*- coding: utf-8 -*-
# views.py

from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic.base import TemplateView
from django.http import HttpResponse, HttpRequest
from .helper import get_momo_answer
# Create your views here.


class ChatterBotAppView(TemplateView):
    template_name = "app.html"


class WechatBotView(View):
    """
    聊天机器人http请求处理
    """
    def get(self, request):
        ask = request.GET.get('ask')
        # 先获取url 参数值 如果没有值，返回 '你说啥'
        if ask:
            answer = get_momo_answer(ask)
            # return render(request, 'app.html', {'answer': answer})
            return HttpResponse(answer)
        else:
            '''还没做'''
            # return render(request, 'app.html', {"answer":"你说什么?"})
            return HttpResponse("你说什么")

    def post(self):
        pass
