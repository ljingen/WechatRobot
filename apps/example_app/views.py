from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic.base import TemplateView
from .helper import get_momo_answer
# Create your views here.


class ChatterBotAppView(TemplateView):
    template_name = "app.html"


class WechatBotView(View):
    def get(self, request):
        ask = request.GET.get('ask')
        if ask:
            answer = get_momo_answer(ask)
            return render(request, 'app.html', {'answer': answer})
        else:
            '''还没做'''
            return render(request, 'app.html', {"answer":"你说什么?"})


    def post(self):
        pass
