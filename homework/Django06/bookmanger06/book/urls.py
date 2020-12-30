from book.views import test1,test2,test3,test4,test5
from django.urls import path,include


urlpatterns = [
    # 利用参数区别请求方式
    path('test1/', test1),
    # 视图函数
    path('test2/', test2),
    #类视图
    path('test3/', test3.as_view()),
    #类视图
    path('test4/', test4.as_view()),
    #类视图
    path('test5/', test5.as_view()),


]