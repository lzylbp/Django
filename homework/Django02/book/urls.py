from book.views import index
from django.urls import path

urlpatterns = [
    # path('admin/', admin.site.urls),

    # path('',index),
    path('index/',index),
]