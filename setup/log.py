import logging
from datetime import datetime
from flask_log_request_id import RequestIDLogFilter
from pytz import utc


def initialize_logger(log_level="DEBUG",
                      log_format="%(asctime)s | %(levelname).5s | txnId=%(request_id).32s | %(funcName)s | %(message)s"):
    """
    @param log_level:
    @param log_format:
    @return:
    """
    # Setup logging
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter(log_format))
    handler.addFilter(RequestIDLogFilter())
    logging.basicConfig(level=log_level, format=log_format, handlers=[handler])
    logging.Formatter.converter = utc_time

def utc_time(*args):
    """
    @param args:
    @return:
    """
    utc_dt = utc.localize(datetime.utcnow())
    return utc_dt.timetuple()
