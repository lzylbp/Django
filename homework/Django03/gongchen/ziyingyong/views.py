from django.http.response import HttpResponse
from django.shortcuts import render
from ziyingyong.models import BookInfo,PeopelInfo

# Create your views here.
BookInfo.objects.all()
def index(requset):
    return HttpResponse('ok')

BookInfo.objects.filter(name__isnull=True)





