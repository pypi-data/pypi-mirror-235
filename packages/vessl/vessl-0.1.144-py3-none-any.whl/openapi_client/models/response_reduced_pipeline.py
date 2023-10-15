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


class ResponseReducedPipeline(object):
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
        'created_dt': 'datetime',
        'description': 'str',
        'is_favorite': 'bool',
        'last_executions': 'list[ResponseReducedPipelineExecution]',
        'last_triggered_dt': 'datetime',
        'last_triggered_reason': 'str',
        'name': 'str',
        'updated_dt': 'datetime'
    }

    attribute_map = {
        'created_dt': 'created_dt',
        'description': 'description',
        'is_favorite': 'is_favorite',
        'last_executions': 'last_executions',
        'last_triggered_dt': 'last_triggered_dt',
        'last_triggered_reason': 'last_triggered_reason',
        'name': 'name',
        'updated_dt': 'updated_dt'
    }

    def __init__(self, created_dt=None, description=None, is_favorite=None, last_executions=None, last_triggered_dt=None, last_triggered_reason=None, name=None, updated_dt=None, local_vars_configuration=None):  # noqa: E501
        """ResponseReducedPipeline - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._created_dt = None
        self._description = None
        self._is_favorite = None
        self._last_executions = None
        self._last_triggered_dt = None
        self._last_triggered_reason = None
        self._name = None
        self._updated_dt = None
        self.discriminator = None

        self.created_dt = created_dt
        self.description = description
        self.is_favorite = is_favorite
        self.last_executions = last_executions
        self.last_triggered_dt = last_triggered_dt
        self.last_triggered_reason = last_triggered_reason
        self.name = name
        self.updated_dt = updated_dt

    @property
    def created_dt(self):
        """Gets the created_dt of this ResponseReducedPipeline.  # noqa: E501


        :return: The created_dt of this ResponseReducedPipeline.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this ResponseReducedPipeline.


        :param created_dt: The created_dt of this ResponseReducedPipeline.  # noqa: E501
        :type created_dt: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_dt is None:  # noqa: E501
            raise ValueError("Invalid value for `created_dt`, must not be `None`")  # noqa: E501

        self._created_dt = created_dt

    @property
    def description(self):
        """Gets the description of this ResponseReducedPipeline.  # noqa: E501


        :return: The description of this ResponseReducedPipeline.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ResponseReducedPipeline.


        :param description: The description of this ResponseReducedPipeline.  # noqa: E501
        :type description: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def is_favorite(self):
        """Gets the is_favorite of this ResponseReducedPipeline.  # noqa: E501


        :return: The is_favorite of this ResponseReducedPipeline.  # noqa: E501
        :rtype: bool
        """
        return self._is_favorite

    @is_favorite.setter
    def is_favorite(self, is_favorite):
        """Sets the is_favorite of this ResponseReducedPipeline.


        :param is_favorite: The is_favorite of this ResponseReducedPipeline.  # noqa: E501
        :type is_favorite: bool
        """
        if self.local_vars_configuration.client_side_validation and is_favorite is None:  # noqa: E501
            raise ValueError("Invalid value for `is_favorite`, must not be `None`")  # noqa: E501

        self._is_favorite = is_favorite

    @property
    def last_executions(self):
        """Gets the last_executions of this ResponseReducedPipeline.  # noqa: E501


        :return: The last_executions of this ResponseReducedPipeline.  # noqa: E501
        :rtype: list[ResponseReducedPipelineExecution]
        """
        return self._last_executions

    @last_executions.setter
    def last_executions(self, last_executions):
        """Sets the last_executions of this ResponseReducedPipeline.


        :param last_executions: The last_executions of this ResponseReducedPipeline.  # noqa: E501
        :type last_executions: list[ResponseReducedPipelineExecution]
        """
        if self.local_vars_configuration.client_side_validation and last_executions is None:  # noqa: E501
            raise ValueError("Invalid value for `last_executions`, must not be `None`")  # noqa: E501

        self._last_executions = last_executions

    @property
    def last_triggered_dt(self):
        """Gets the last_triggered_dt of this ResponseReducedPipeline.  # noqa: E501


        :return: The last_triggered_dt of this ResponseReducedPipeline.  # noqa: E501
        :rtype: datetime
        """
        return self._last_triggered_dt

    @last_triggered_dt.setter
    def last_triggered_dt(self, last_triggered_dt):
        """Sets the last_triggered_dt of this ResponseReducedPipeline.


        :param last_triggered_dt: The last_triggered_dt of this ResponseReducedPipeline.  # noqa: E501
        :type last_triggered_dt: datetime
        """

        self._last_triggered_dt = last_triggered_dt

    @property
    def last_triggered_reason(self):
        """Gets the last_triggered_reason of this ResponseReducedPipeline.  # noqa: E501


        :return: The last_triggered_reason of this ResponseReducedPipeline.  # noqa: E501
        :rtype: str
        """
        return self._last_triggered_reason

    @last_triggered_reason.setter
    def last_triggered_reason(self, last_triggered_reason):
        """Sets the last_triggered_reason of this ResponseReducedPipeline.


        :param last_triggered_reason: The last_triggered_reason of this ResponseReducedPipeline.  # noqa: E501
        :type last_triggered_reason: str
        """

        self._last_triggered_reason = last_triggered_reason

    @property
    def name(self):
        """Gets the name of this ResponseReducedPipeline.  # noqa: E501


        :return: The name of this ResponseReducedPipeline.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ResponseReducedPipeline.


        :param name: The name of this ResponseReducedPipeline.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def updated_dt(self):
        """Gets the updated_dt of this ResponseReducedPipeline.  # noqa: E501


        :return: The updated_dt of this ResponseReducedPipeline.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_dt

    @updated_dt.setter
    def updated_dt(self, updated_dt):
        """Sets the updated_dt of this ResponseReducedPipeline.


        :param updated_dt: The updated_dt of this ResponseReducedPipeline.  # noqa: E501
        :type updated_dt: datetime
        """
        if self.local_vars_configuration.client_side_validation and updated_dt is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_dt`, must not be `None`")  # noqa: E501

        self._updated_dt = updated_dt

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
        if not isinstance(other, ResponseReducedPipeline):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResponseReducedPipeline):
            return True

        return self.to_dict() != other.to_dict()
