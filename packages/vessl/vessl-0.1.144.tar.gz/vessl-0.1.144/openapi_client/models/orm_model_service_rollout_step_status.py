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


class OrmModelServiceRolloutStepStatus(object):
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
        'created_revision_number': 'int',
        'last_updated': 'datetime',
        'message': 'str',
        'step_started': 'datetime',
        'step_status': 'str'
    }

    attribute_map = {
        'created_revision_number': 'created_revision_number',
        'last_updated': 'last_updated',
        'message': 'message',
        'step_started': 'step_started',
        'step_status': 'step_status'
    }

    def __init__(self, created_revision_number=None, last_updated=None, message=None, step_started=None, step_status=None, local_vars_configuration=None):  # noqa: E501
        """OrmModelServiceRolloutStepStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._created_revision_number = None
        self._last_updated = None
        self._message = None
        self._step_started = None
        self._step_status = None
        self.discriminator = None

        if created_revision_number is not None:
            self.created_revision_number = created_revision_number
        if last_updated is not None:
            self.last_updated = last_updated
        if message is not None:
            self.message = message
        if step_started is not None:
            self.step_started = step_started
        if step_status is not None:
            self.step_status = step_status

    @property
    def created_revision_number(self):
        """Gets the created_revision_number of this OrmModelServiceRolloutStepStatus.  # noqa: E501


        :return: The created_revision_number of this OrmModelServiceRolloutStepStatus.  # noqa: E501
        :rtype: int
        """
        return self._created_revision_number

    @created_revision_number.setter
    def created_revision_number(self, created_revision_number):
        """Sets the created_revision_number of this OrmModelServiceRolloutStepStatus.


        :param created_revision_number: The created_revision_number of this OrmModelServiceRolloutStepStatus.  # noqa: E501
        :type created_revision_number: int
        """

        self._created_revision_number = created_revision_number

    @property
    def last_updated(self):
        """Gets the last_updated of this OrmModelServiceRolloutStepStatus.  # noqa: E501


        :return: The last_updated of this OrmModelServiceRolloutStepStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this OrmModelServiceRolloutStepStatus.


        :param last_updated: The last_updated of this OrmModelServiceRolloutStepStatus.  # noqa: E501
        :type last_updated: datetime
        """

        self._last_updated = last_updated

    @property
    def message(self):
        """Gets the message of this OrmModelServiceRolloutStepStatus.  # noqa: E501


        :return: The message of this OrmModelServiceRolloutStepStatus.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this OrmModelServiceRolloutStepStatus.


        :param message: The message of this OrmModelServiceRolloutStepStatus.  # noqa: E501
        :type message: str
        """

        self._message = message

    @property
    def step_started(self):
        """Gets the step_started of this OrmModelServiceRolloutStepStatus.  # noqa: E501


        :return: The step_started of this OrmModelServiceRolloutStepStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._step_started

    @step_started.setter
    def step_started(self, step_started):
        """Sets the step_started of this OrmModelServiceRolloutStepStatus.


        :param step_started: The step_started of this OrmModelServiceRolloutStepStatus.  # noqa: E501
        :type step_started: datetime
        """

        self._step_started = step_started

    @property
    def step_status(self):
        """Gets the step_status of this OrmModelServiceRolloutStepStatus.  # noqa: E501


        :return: The step_status of this OrmModelServiceRolloutStepStatus.  # noqa: E501
        :rtype: str
        """
        return self._step_status

    @step_status.setter
    def step_status(self, step_status):
        """Sets the step_status of this OrmModelServiceRolloutStepStatus.


        :param step_status: The step_status of this OrmModelServiceRolloutStepStatus.  # noqa: E501
        :type step_status: str
        """
        allowed_values = ["succeeded", "in_progress", "paused", "failed"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and step_status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `step_status` ({0}), must be one of {1}"  # noqa: E501
                .format(step_status, allowed_values)
            )

        self._step_status = step_status

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
        if not isinstance(other, OrmModelServiceRolloutStepStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrmModelServiceRolloutStepStatus):
            return True

        return self.to_dict() != other.to_dict()
