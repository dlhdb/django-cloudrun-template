from django.http import (
    HttpResponse,
    HttpRequest,
    JsonResponse,
    HttpResponseBadRequest
)
from django.views import View

import pydantic
import logging
from typing import *

logger = logging.getLogger()
