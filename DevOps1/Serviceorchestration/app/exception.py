#!/usr/bin/python

import logging
import sys
# from translator.toscalib.utils.gettextutils import _
# from app.gettextutils import _
from gettext import gettext as _
log = logging.getLogger(__name__)


class ServiceOrchestrationException(Exception):
    '''Base exception class for TOSCA
    To correctly use this class, inherit from it and define
    a 'msg_fmt' property.
    '''
    _FATAL_EXCEPTION_FORMAT_ERRORS = False
    message = _('An unknown exception occurred.')

    def __init__(self, **kwargs):
        try:
            self.message = self.msg_fmt % kwargs
        except KeyError:
            exc_info = sys.exc_info()
            log.exception(_('Exception in string format operation: %s')
                          % exc_info[1])
            if ServiceOrchestrationException._FATAL_EXCEPTION_FORMAT_ERRORS:
                raise exc_info[0]

    def __str__(self):
        return self.message

    @staticmethod
    def set_fatal_format_exception(flag):
        if isinstance(flag, bool):
            ServiceOrchestrationException._FATAL_EXCEPTION_FORMAT_ERRORS = flag


class InvalidFileException(ServiceOrchestrationException):
    msg_fmt = _('%(what)s is not a "%(required)s" file.')


class InvalidInputException(ServiceOrchestrationException):
    msg_fmt = _('An error with input parameter.')


class NoVnfPackageException(ServiceOrchestrationException):
    msg_fmt = _('All VNFs are not On Boarded.')


class VnfNotEnabledException(ServiceOrchestrationException):
    msg_fmt = _('All VNFs are not enabled.')


class NoNsdException(ServiceOrchestrationException):
    msg_fmt = _('No NSD of given id is found.')


class NoVnfException(ServiceOrchestrationException):
    msg_fmt = _('No Package of given id is found.')


class NsdNotEnabledException(ServiceOrchestrationException):
    msg_fmt = _('The given NSD is not enabled.')


class NotOnBoardedException(ServiceOrchestrationException):
    msg_fmt = _('The given package is not On Boarded.')


class NoResourcesException(ServiceOrchestrationException):
    msg_fmt = _('Resources are not available.')
