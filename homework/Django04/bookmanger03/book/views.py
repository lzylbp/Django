from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

def book(request,cat_id,detail_id):
    # print(cat_id,detail_id)
    # return HttpResponse('kanshu')

    # query_string=request.GET
    # a=query_string['a']
    # b=query_string.get('b')
    # print(a,b)
    # return HttpResponse('kanshu')

    # 常规使用
    # query_string=request.GET
    # alist=query_string.getlist('a')
    # b=query_string.get('b')
    # print(alist,b)
    # return HttpResponse('kanshu')

    #非常规使用
    # query_string=request.GET
    # alist=query_string.get('a')
    # b=query_string.getlist('b')
    # print(alist,b)
    # return HttpResponse('kanshu')

    #默认值
    query_string=request.GET
    c=query_string.get('c',1)
    print(c)
    d = query_string.getlist('c', 2)
    print(d)
    return HttpResponse('kanshu')

def login(request):
    body=request.POST
    print(body)
    return HttpResponse('login')

def weibo(requset):
    body=requset.body
    print(body)
    body_str=body.decode()
    print(body_str)
    import json
    data=json.loads(body_str)
    print(data)
    return HttpResponse("weibo json")