from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# 利用参数区别请求方式
def test1(request):
    print(request.method)
    return HttpResponse('test1')

# 视图函数
def test2(request):
    if request.method=='GET':
        return HttpResponse('get')
    else:
        return HttpResponse('post')

#类视图
from django.views import View
class test3(View):
    def get(self,request):
        return HttpResponse('jd-test3-get')
    def post(self,request):
        return HttpResponse('jd-test3-post')

#类视图
from django.views import View
class test4(View):
    def get(self,request):
        isLogin=True
        if isLogin:
            return HttpResponse('test4-get')
        else:
            return HttpResponse('登录')
    def post(self,request):
        isLogin = False
        if isLogin:
            return HttpResponse('test4-post')
        else:
            return HttpResponse('登录')

#类视图
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
class test5(LoginRequiredMixin,View):
    def get(self,request):
        return HttpResponse('test5-get')
    def post(self,request):
        return HttpResponse('test5-post')