from django.http import HttpResponse
from django.middleware.http import MiddlewareMixin


class EBHealthCheckMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.META['PATH_INFO'] == '/health/':
            return HttpResponse('ok')
