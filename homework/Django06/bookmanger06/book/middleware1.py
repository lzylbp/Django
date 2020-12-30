from django.utils.deprecation import MiddlewareMixin

# 单个中间件的执行顺序
class BookMiddlewareMixin1(MiddlewareMixin):

    def process_request(self,request):
        print('request 每次请求前 都会调用111111')
        pass

    def process_response(self,request,reponse):
        print('response 每次响应前 都会调用11111')
        return reponse


