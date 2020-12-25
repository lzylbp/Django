from django.urls import path
from book.views import login,weibo

urlpatterns = [

    path('login/',login),
    path('weibo/',weibo)

]