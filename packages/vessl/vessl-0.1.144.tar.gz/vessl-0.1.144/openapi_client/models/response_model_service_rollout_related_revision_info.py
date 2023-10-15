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


class ResponseModelServiceRolloutRelatedRevisionInfo(object):
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
        'available_replicas': 'int',
        'max_replica': 'int',
        'min_replica': 'int',
        'number': 'int',
        'status': 'str'
    }

    attribute_map = {
        'available_replicas': 'available_replicas',
        'max_replica': 'max_replica',
        'min_replica': 'min_replica',
        'number': 'number',
        'status': 'status'
    }

    def __init__(self, available_replicas=None, max_replica=None, min_replica=None, number=None, status=None, local_vars_configuration=None):  # noqa: E501
        """ResponseModelServiceRolloutRelatedRevisionInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._available_replicas = None
        self._max_replica = None
        self._min_replica = None
        self._number = None
        self._status = None
        self.discriminator = None

        if available_replicas is not None:
            self.available_replicas = available_replicas
        if max_replica is not None:
            self.max_replica = max_replica
        if min_replica is not None:
            self.min_replica = min_replica
        if number is not None:
            self.number = number
        if status is not None:
            self.status = status

    @property
    def available_replicas(self):
        """Gets the available_replicas of this ResponseModelServiceRolloutRelatedRevisionInfo.  # noqa: E501


        :return: The available_replicas of this ResponseModelServiceRolloutRelatedRevisionInfo.  # noqa: E501
        :rtype: int
        """
        return self._available_replicas

    @available_replicas.setter
    def available_replicas(self, available_replicas):
        """Sets the available_replicas of this ResponseModelServiceRolloutRelatedRevisionInfo.


        :param available_replicas: The available_replicas of this ResponseModelServiceRolloutRelatedRevisionInfo.  # noqa: E501
        :type available_replicas: int
        """

        self._available_replicas = available_replicas

    @property
    def max_replica(self):
        """Gets the max_replica of this ResponseModelServiceRolloutRelatedRevisionInfo.  # noqa: E501


        :return: The max_replica of this ResponseModelServiceRolloutRelatedRevisionInfo.  # noqa: E501
        :rtype: int
        """
        return self._max_replica

    @max_replica.setter
    def max_replica(self, max_replica):
        """Sets the max_replica of this ResponseModelServiceRolloutRelatedRevisionInfo.


        :param max_replica: The max_replica of this ResponseModelServiceRolloutRelatedRevisionInfo.  # noqa: E501
        :type max_replica: int
        """

        self._max_replica = max_replica

    @property
    def min_replica(self):
        """Gets the min_replica of this ResponseModelServiceRolloutRelatedRevisionInfo.  # noqa: E501


        :return: The min_replica of this ResponseModelServiceRolloutRelatedRevisionInfo.  # noqa: E501
        :rtype: int
        """
        return self._min_replica

    @min_replica.setter
    def min_replica(self, min_replica):
        """Sets the min_replica of this ResponseModelServiceRolloutRelatedRevisionInfo.


        :param min_replica: The min_replica of this ResponseModelServiceRolloutRelatedRevisionInfo.  # noqa: E501
        :type min_replica: int
        """

        self._min_replica = min_replica

    @property
    def number(self):
        """Gets the number of this ResponseModelServiceRolloutRelatedRevisionInfo.  # noqa: E501


        :return: The number of this ResponseModelServiceRolloutRelatedRevisionInfo.  # noqa: E501
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this ResponseModelServiceRolloutRelatedRevisionInfo.


        :param number: The number of this ResponseModelServiceRolloutRelatedRevisionInfo.  # noqa: E501
        :type number: int
        """

        self._number = number

    @property
    def status(self):
        """Gets the status of this ResponseModelServiceRolloutRelatedRevisionInfo.  # noqa: E501


        :return: The status of this ResponseModelServiceRolloutRelatedRevisionInfo.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ResponseModelServiceRolloutRelatedRevisionInfo.


        :param status: The status of this ResponseModelServiceRolloutRelatedRevisionInfo.  # noqa: E501
        :type status: str
        """

        self._status = status

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
        if not isinstance(other, ResponseModelServiceRolloutRelatedRevisionInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResponseModelServiceRolloutRelatedRevisionInfo):
            return True

        return self.to_dict() != other.to_dict()
