import logging
from djproject.middlewares.request_id import get_current_request_id


class RequestIDFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        record.requestId = get_current_request_id()
        return True
