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

def register(request):
    return HttpResponse("ok")

#路径参数
def lujing(request,cat_id,id):
    return HttpResponse('lujing')

#默认转化器
def site_register3(requset,mobile):
    print(mobile)
    return HttpResponse('ok')


#自定义转化器
def site_register4(requset,mobile):
    print(mobile)
    return HttpResponse('ok2')


# 获取请求头信息
def get_header(request):
    # print(request.META)
    print(request.META['HTTP_ACCEPT'])
    return HttpResponse('header_META')


def  get_method(request):
    print(request.method)
    return HttpResponse('header_Method')


from django.http import JsonResponse

# 常规
def res_json(request):
    data={
        'name':'it',
        'age':18
    }
    return JsonResponse(data)

#强制
def res_json1(request):
    data=[{
        'name':'it',
        'age':18
          },
        {
        'name':'it',
         'age':18
        }

    ]

    return JsonResponse(data,safe=False)

def set_cookie(request):
    name=request.GET.get('name')

    response=HttpResponse('set_cookie')

    response.set_cookie(key='name',value=name,max_age=0)

    # response.delete_cookie(key='name')

    return response



def get_cookie(request):
    cookie=request.COOKIESss

    print(cookie)
    return HttpResponse('get_cookie')

def set_session(request):
    request.session['name']='123'

    return HttpResponse('set_session')

def get_session(request):

    # name=request.session.['name']
    name=request.session.get('name')
    print(name)

    return HttpResponse('get_seeion')


