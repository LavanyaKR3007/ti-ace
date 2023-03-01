# coding: utf-8

from __future__ import absolute_import

from datetime import date, datetime  # noqa: F401
from typing import List, Dict  # noqa: F401

from models import util
from models.base_model_ import Model
from models.context import Context  # noqa: F401,E501
from models.status_message import StatusMessage  # noqa: F401,E501


class StatusBody(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, context: Context=None, message: StatusMessage=None):  # noqa: E501
        """StatusBody - a model defined in Swagger

        :param context: The context of this StatusBody.  # noqa: E501
        :type context: Context
        :param message: The message of this StatusBody.  # noqa: E501
        :type message: StatusMessage
        """
        self.swagger_types = {
            'context': Context,
            'message': StatusMessage
        }

        self.attribute_map = {
            'context': 'context',
            'message': 'message'
        }
        self._context = context
        self._message = message

    @classmethod
    def from_dict(cls, dikt) -> 'StatusBody':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The status_body of this StatusBody.  # noqa: E501
        :rtype: StatusBody
        """
        return util.deserialize_model(dikt, cls)

    @property
    def context(self) -> Context:
        """Gets the context of this StatusBody.


        :return: The context of this StatusBody.
        :rtype: Context
        """
        return self._context

    @context.setter
    def context(self, context: Context):
        """Sets the context of this StatusBody.


        :param context: The context of this StatusBody.
        :type context: Context
        """
        if context is None:
            raise ValueError("Invalid value for `context`, must not be `None`")  # noqa: E501

        self._context = context

    @property
    def message(self) -> StatusMessage:
        """Gets the message of this StatusBody.


        :return: The message of this StatusBody.
        :rtype: StatusMessage
        """
        return self._message

    @message.setter
    def message(self, message: StatusMessage):
        """Sets the message of this StatusBody.


        :param message: The message of this StatusBody.
        :type message: StatusMessage
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message