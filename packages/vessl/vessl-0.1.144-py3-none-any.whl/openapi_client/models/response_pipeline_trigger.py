# coding: utf-8

"""
    Aron API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from openapi_client.configuration import Configuration


class ResponsePipelineTrigger(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'cron': 'ResponsePipelineTriggerCron',
        'description': 'str',
        'enabled': 'bool',
        'id': 'int',
        'kind': 'str',
        'name': 'str',
        'webhook': 'ResponsePipelineTriggerWebhook'
    }

    attribute_map = {
        'cron': 'cron',
        'description': 'description',
        'enabled': 'enabled',
        'id': 'id',
        'kind': 'kind',
        'name': 'name',
        'webhook': 'webhook'
    }

    def __init__(self, cron=None, description=None, enabled=None, id=None, kind=None, name=None, webhook=None, local_vars_configuration=None):  # noqa: E501
        """ResponsePipelineTrigger - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._cron = None
        self._description = None
        self._enabled = None
        self._id = None
        self._kind = None
        self._name = None
        self._webhook = None
        self.discriminator = None

        if cron is not None:
            self.cron = cron
        if description is not None:
            self.description = description
        if enabled is not None:
            self.enabled = enabled
        if id is not None:
            self.id = id
        if kind is not None:
            self.kind = kind
        if name is not None:
            self.name = name
        if webhook is not None:
            self.webhook = webhook

    @property
    def cron(self):
        """Gets the cron of this ResponsePipelineTrigger.  # noqa: E501


        :return: The cron of this ResponsePipelineTrigger.  # noqa: E501
        :rtype: ResponsePipelineTriggerCron
        """
        return self._cron

    @cron.setter
    def cron(self, cron):
        """Sets the cron of this ResponsePipelineTrigger.


        :param cron: The cron of this ResponsePipelineTrigger.  # noqa: E501
        :type cron: ResponsePipelineTriggerCron
        """

        self._cron = cron

    @property
    def description(self):
        """Gets the description of this ResponsePipelineTrigger.  # noqa: E501


        :return: The description of this ResponsePipelineTrigger.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ResponsePipelineTrigger.


        :param description: The description of this ResponsePipelineTrigger.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def enabled(self):
        """Gets the enabled of this ResponsePipelineTrigger.  # noqa: E501


        :return: The enabled of this ResponsePipelineTrigger.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this ResponsePipelineTrigger.


        :param enabled: The enabled of this ResponsePipelineTrigger.  # noqa: E501
        :type enabled: bool
        """

        self._enabled = enabled

    @property
    def id(self):
        """Gets the id of this ResponsePipelineTrigger.  # noqa: E501


        :return: The id of this ResponsePipelineTrigger.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ResponsePipelineTrigger.


        :param id: The id of this ResponsePipelineTrigger.  # noqa: E501
        :type id: int
        """

        self._id = id

    @property
    def kind(self):
        """Gets the kind of this ResponsePipelineTrigger.  # noqa: E501


        :return: The kind of this ResponsePipelineTrigger.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this ResponsePipelineTrigger.


        :param kind: The kind of this ResponsePipelineTrigger.  # noqa: E501
        :type kind: str
        """

        self._kind = kind

    @property
    def name(self):
        """Gets the name of this ResponsePipelineTrigger.  # noqa: E501


        :return: The name of this ResponsePipelineTrigger.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ResponsePipelineTrigger.


        :param name: The name of this ResponsePipelineTrigger.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def webhook(self):
        """Gets the webhook of this ResponsePipelineTrigger.  # noqa: E501


        :return: The webhook of this ResponsePipelineTrigger.  # noqa: E501
        :rtype: ResponsePipelineTriggerWebhook
        """
        return self._webhook

    @webhook.setter
    def webhook(self, webhook):
        """Sets the webhook of this ResponsePipelineTrigger.


        :param webhook: The webhook of this ResponsePipelineTrigger.  # noqa: E501
        :type webhook: ResponsePipelineTriggerWebhook
        """

        self._webhook = webhook

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ResponsePipelineTrigger):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResponsePipelineTrigger):
            return True

        return self.to_dict() != other.to_dict()
