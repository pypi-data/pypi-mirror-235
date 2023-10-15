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


class ResponseReducedRunExecution(object):
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
        'id': 'int',
        'spec_title': 'str',
        'status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'spec_title': 'spec_title',
        'status': 'status'
    }

    def __init__(self, id=None, spec_title=None, status=None, local_vars_configuration=None):  # noqa: E501
        """ResponseReducedRunExecution - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._spec_title = None
        self._status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if spec_title is not None:
            self.spec_title = spec_title
        if status is not None:
            self.status = status

    @property
    def id(self):
        """Gets the id of this ResponseReducedRunExecution.  # noqa: E501


        :return: The id of this ResponseReducedRunExecution.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ResponseReducedRunExecution.


        :param id: The id of this ResponseReducedRunExecution.  # noqa: E501
        :type id: int
        """

        self._id = id

    @property
    def spec_title(self):
        """Gets the spec_title of this ResponseReducedRunExecution.  # noqa: E501


        :return: The spec_title of this ResponseReducedRunExecution.  # noqa: E501
        :rtype: str
        """
        return self._spec_title

    @spec_title.setter
    def spec_title(self, spec_title):
        """Sets the spec_title of this ResponseReducedRunExecution.


        :param spec_title: The spec_title of this ResponseReducedRunExecution.  # noqa: E501
        :type spec_title: str
        """

        self._spec_title = spec_title

    @property
    def status(self):
        """Gets the status of this ResponseReducedRunExecution.  # noqa: E501


        :return: The status of this ResponseReducedRunExecution.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ResponseReducedRunExecution.


        :param status: The status of this ResponseReducedRunExecution.  # noqa: E501
        :type status: str
        """
        allowed_values = ["queued", "pending", "running", "failed", "completed"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

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
        if not isinstance(other, ResponseReducedRunExecution):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResponseReducedRunExecution):
            return True

        return self.to_dict() != other.to_dict()
