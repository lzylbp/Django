from django.shortcuts import render
from django.http.response import HttpResponse

from django.shortcuts import render

# Create your views here.

def index(request):
    # return HttpResponse('TTT')
    data={
        "show":"快乐！"
    }
    return render(request,'book/index.html',context=data)