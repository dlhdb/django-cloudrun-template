from asgiref.sync import iscoroutinefunction
from django.utils.decorators import sync_and_async_middleware

import uuid
from contextvars import ContextVar


request_id_var = ContextVar('request_id')


@sync_and_async_middleware
def request_id_middleware(get_response):

    if iscoroutinefunction(get_response):

        async def middleware(request):
            request_id_var.set(uuid.uuid4().hex)
            response = await get_response(request)
            return response

    else:

        def middleware(request):
            request_id_var.set(uuid.uuid4().hex)
            response = get_response(request)
            return response

    return middleware


# class RequestIdMiddleware:
#     async_capable = True
#     sync_capable = False
#
#     def __init__(self, get_response):
#         self.get_response = get_response
#
#     async def __call__(self, request):
#         request_id_var.set(uuid.uuid4().hex)
#         response = await self.get_response(request)
#         return response


def get_current_request_id():
    return request_id_var.get()

