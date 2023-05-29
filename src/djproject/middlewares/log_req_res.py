from asgiref.sync import iscoroutinefunction
from django.utils.decorators import sync_and_async_middleware
from django.http import HttpRequest, HttpResponse

import logging
import time
import json

logger = logging.getLogger()


@sync_and_async_middleware
def log_req_res_middleware(get_response):
    def write_log(request: HttpRequest, response: HttpResponse):
        request_path = request.get_full_path()
        if request.content_type == 'application/json':
            request_body = json.dumps(json.loads(request.body))
        else:
            request_body = repr(request.body.decode('utf-8'))

        start_time = time.time()
        duration = time.time() - start_time

        response_body = repr(response.content.decode('utf-8'))

        logging.info(
            "[Duration] {:.2f}s [Request] {} {}, body: {} [Response] {} body: {}".format(
                duration,
                request.method,
                request_path,
                request_body,
                response.status_code,
                response_body)
        )

    if iscoroutinefunction(get_response):

        async def middleware(request):
            response = await get_response(request)
            write_log(request, response)
            return response

    else:

        def middleware(request):
            response = get_response(request)
            write_log(request, response)
            return response

    return middleware


# class ReqResLoggingMiddleware(object):
#     def __init__(self, get_response):
#         self.get_response = get_response
#
#     def __call__(self, request: HttpRequest) -> HttpResponse:
#         request_path = request.get_full_path()
#         if request.content_type == 'application/json':
#             request_body = json.dumps(json.loads(request.body))
#         else:
#             request_body = repr(request.body.decode('utf-8'))
#
#         start_time = time.time()
#         response: HttpResponse = self.get_response(request)
#         duration = time.time() - start_time
#
#         response_body = repr(response.content.decode('utf-8'))
#         logging.info(
#             "[Duration] {:.2f}s [Request] {} {}, {} [Response] {} body:{}".format(
#                 duration,
#                 request.method,
#                 request_path,
#                 request_body,
#                 response.status_code,
#                 response_body)
#         )
#
#         return response
