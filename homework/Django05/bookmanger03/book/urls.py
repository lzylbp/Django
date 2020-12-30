from django.urls import path
from book.views import login,weibo,res_json,res_json1,set_cookie,get_cookie,set_session,get_session,lujing,site_register3,site_register4,get_header,get_method,JDLogin
from book.converters import MobileConverter
from django.urls import register_converter

from django.urls import converters


register_converter(MobileConverter,'phone')

urlpatterns = [

    path('login/',login),
    path('weibo/',weibo),

    path('<int:cat_id>/<int:id>/',lujing),

    path('site/register3/<mobile>',site_register3),

    path('site/register4/<phone:mobile>/',site_register4),

    path('header/',get_header),
    path('method/',get_method),

    # path('site/register')
    path('register/',res_json),
    path('register1/',res_json1),

    path('set_cookie/', set_cookie),
    path('get_cookie/', get_cookie),


    path('set_session/',set_session ),
    path('get_session/',get_session),


    path('jd/',JDLogin.as_view())


]