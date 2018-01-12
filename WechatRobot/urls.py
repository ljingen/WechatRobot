"""WechatRobot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
# from chatterbot.ext.django_chatterbot import urls as chatterbot_urls
from example_app.views import WechatBotView, ChatterBotAppView

urlpatterns = [

    url(r'^$', ChatterBotAppView.as_view(), name='main'),

    url(r'^admin/', admin.site.urls),

    # http://127.0.0.1:8000/api/momo/?ask=我是程序员
    url(r'^api/momo/$', WechatBotView.as_view(), name='wechatrobot'),
    # 增加聊天机器人的支持
    url(r'^api/chatterbot/', include('chatterbot.ext.django_chatterbot.urls', namespace='chatterbot')),
    # 用户 列表的url配置
    url(r'^wechat/', include('wechat.urls', namespace='wechat')),
]
