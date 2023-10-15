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


class PipelineTriggerUpdateAPIInput(object):
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
        'description': 'str',
        'kind': 'str',
        'name': 'str',
        'trigger_cron': 'V1TriggerCron',
        'trigger_webhook': 'V1TriggerWebhook'
    }

    attribute_map = {
        'description': 'description',
        'kind': 'kind',
        'name': 'name',
        'trigger_cron': 'trigger_cron',
        'trigger_webhook': 'trigger_webhook'
    }

    def __init__(self, description=None, kind=None, name=None, trigger_cron=None, trigger_webhook=None, local_vars_configuration=None):  # noqa: E501
        """PipelineTriggerUpdateAPIInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._description = None
        self._kind = None
        self._name = None
        self._trigger_cron = None
        self._trigger_webhook = None
        self.discriminator = None

        if description is not None:
            self.description = description
        self.kind = kind
        self.name = name
        if trigger_cron is not None:
            self.trigger_cron = trigger_cron
        if trigger_webhook is not None:
            self.trigger_webhook = trigger_webhook

    @property
    def description(self):
        """Gets the description of this PipelineTriggerUpdateAPIInput.  # noqa: E501


        :return: The description of this PipelineTriggerUpdateAPIInput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PipelineTriggerUpdateAPIInput.


        :param description: The description of this PipelineTriggerUpdateAPIInput.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def kind(self):
        """Gets the kind of this PipelineTriggerUpdateAPIInput.  # noqa: E501


        :return: The kind of this PipelineTriggerUpdateAPIInput.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this PipelineTriggerUpdateAPIInput.


        :param kind: The kind of this PipelineTriggerUpdateAPIInput.  # noqa: E501
        :type kind: str
        """
        if self.local_vars_configuration.client_side_validation and kind is None:  # noqa: E501
            raise ValueError("Invalid value for `kind`, must not be `None`")  # noqa: E501
        allowed_values = ["cron", "webhook"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and kind not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `kind` ({0}), must be one of {1}"  # noqa: E501
                .format(kind, allowed_values)
            )

        self._kind = kind

    @property
    def name(self):
        """Gets the name of this PipelineTriggerUpdateAPIInput.  # noqa: E501


        :return: The name of this PipelineTriggerUpdateAPIInput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PipelineTriggerUpdateAPIInput.


        :param name: The name of this PipelineTriggerUpdateAPIInput.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def trigger_cron(self):
        """Gets the trigger_cron of this PipelineTriggerUpdateAPIInput.  # noqa: E501


        :return: The trigger_cron of this PipelineTriggerUpdateAPIInput.  # noqa: E501
        :rtype: V1TriggerCron
        """
        return self._trigger_cron

    @trigger_cron.setter
    def trigger_cron(self, trigger_cron):
        """Sets the trigger_cron of this PipelineTriggerUpdateAPIInput.


        :param trigger_cron: The trigger_cron of this PipelineTriggerUpdateAPIInput.  # noqa: E501
        :type trigger_cron: V1TriggerCron
        """

        self._trigger_cron = trigger_cron

    @property
    def trigger_webhook(self):
        """Gets the trigger_webhook of this PipelineTriggerUpdateAPIInput.  # noqa: E501


        :return: The trigger_webhook of this PipelineTriggerUpdateAPIInput.  # noqa: E501
        :rtype: V1TriggerWebhook
        """
        return self._trigger_webhook

    @trigger_webhook.setter
    def trigger_webhook(self, trigger_webhook):
        """Sets the trigger_webhook of this PipelineTriggerUpdateAPIInput.


        :param trigger_webhook: The trigger_webhook of this PipelineTriggerUpdateAPIInput.  # noqa: E501
        :type trigger_webhook: V1TriggerWebhook
        """

        self._trigger_webhook = trigger_webhook

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
        if not isinstance(other, PipelineTriggerUpdateAPIInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PipelineTriggerUpdateAPIInput):
            return True

        return self.to_dict() != other.to_dict()
