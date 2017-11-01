# -*- coding: utf-8 -*-
"""
Albertifra Exceptions tree
+-- AlbertifraException
    +-- YourCustomException
"""

import logging


# GENERIC EXCEPTION
class AlbertifraException(Exception):
    """
    To import:
        from web import exceptions

    To raise:
        raise exceptions.AlbertifraException('text of error')

    To capture:
        try:
            [code]
        except exceptions.AlbertifraException as e:
            [code]
    """
    msg = ''

    def __init__(self, msg=None, write_log=True, level='ERROR'):
        """
        :param msg: error text message
        :param write_log: if true a log is written in /var/log/django/albertifra-exceptions.log
        """
        self.exception_logger = logging.getLogger('exceptions')
        self.log_level = level

        if msg:
            self.msg = msg
        if write_log:
            self.write_log(self.msg)

    def get_repr_str(self):
        repr_str = self.__class__.__name__ + u': '
        repr_str += u'{} {}'.format(self.log_level, self.msg)
        return repr_str

    def __str__(self):
        return repr(self.get_repr_str())

    def __repr__(self):
        return repr(self.get_repr_str())

    def write_log(self, msg):
        getattr(self.exception_logger, self.log_level.lower())(msg)


# CUSTOM EXCEPTIONS
class YourCustomException(AlbertifraException):
    """
    To import:
        from web import exceptions

    To raise:
        raise exceptions.YourCustomException('text of error')

    To capture:
        try:
            [code]
        except exceptions.YourCustomException as e:
            [code]
    """
    pass
