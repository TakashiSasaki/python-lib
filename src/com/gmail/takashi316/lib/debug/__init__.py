from __future__ import  print_function, unicode_literals
import inspect as _inspect

def _getNameInPreviousFrame():
    current_frame = _inspect.currentframe(2)
    name = current_frame.f_globals["__name__"]
    return name

import logging as _logging
LOG_LEVEL = _logging.INFO
_logging.basicConfig(level=LOG_LEVEL)
logger = _logging.getLogger("")
logger.setLevel(LOG_LEVEL)

def debug(message):
    _logger = _logging.getLogger(_getNameInPreviousFrame())
    _logger.debug(message)

def info(message):
    _logger = _logging.getLogger(_getNameInPreviousFrame())
    _logger.info(message)

def warn(message):
    _logger = _logging.getLogger(_getNameInPreviousFrame())
    _logger.warn(message)

def error(message):
    _logger = _logging.getLogger(_getNameInPreviousFrame())
    _logger.error(message)

def critical(message):
    _logger = _logging.getLogger(_getNameInPreviousFrame())
    _logger.critical(message)

def exception(message):
    _logger = _logging.getLogger(_getNameInPreviousFrame())
    _logger.exception(message)

