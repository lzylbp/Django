from django.urls import path
from book.views import index1,index2

urlpatterns = [

    path('index1/',index1),
    path('index2/',index2),
]