# -*- coding: utf-8 -*-
# filename:handle.py

import hashlib
from django.views.generic.base import View
from django.http import HttpResponse, Http404

TOKEN = 'dianshu_weinxin'


class HandleView(View):
    def get(self, request):
        print("++++开始请求+++++")
        try:
            signature = request.GET.get('signature', '')  # 从请求里面取出来signature签名  对比hashcode
            timestamp = request.GET.get('timestamp', '')  # 从请求里面取出来timestamp 时间戳
            nonce = request.GET.get('nonce', '')  # 从请求里面取出来nonce 随机数
            echostr = request.GET.get('echostr', '')  # 从请求里面取出来echo

            if len(signature) == 0 or len(timestamp) ==0 or len(nonce) ==0 or len(echostr) ==0:
                return HttpResponse("hello,this is handle view")

            token = TOKEN  # 请按照公众平台官网\基本配置中信息填写

            m_list = [token, timestamp, nonce]
            
            m_list.sort()

            sha1 = hashlib.sha1()  # #sha1对象，md5不能反解，但是加密是固定的，就是关系是一一对应，所以有缺陷，可以被对撞出来

            map(sha1.update, m_list)  # 使用sha1.update对list1里面的数据都进行hash运算并生成一个list
            hashcode = sha1.hexdigest()  # 拿到加密的hashcode
            print("Handle/GET func hashcode:" + hashcode + "--signature: " + signature)

            if hashcode == signature:
                return echostr
            else:
                return HttpResponse("加密的东西怎么不一样!")
        except Exception:
            return HttpResponse("出现异常了!")

    def post(self, request):
        pass