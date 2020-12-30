from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index1(request):
    return HttpResponse('test-1!!!')

def index2(request):
    data={
        "show":"lalala"
    }
    return render(request,'book/index.html',context=data)