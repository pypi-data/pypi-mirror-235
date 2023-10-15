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


class ExternalGitBranchListResponse(object):
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
        'branches': 'list[ProtoBranch]'
    }

    attribute_map = {
        'branches': 'branches'
    }

    def __init__(self, branches=None, local_vars_configuration=None):  # noqa: E501
        """ExternalGitBranchListResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._branches = None
        self.discriminator = None

        self.branches = branches

    @property
    def branches(self):
        """Gets the branches of this ExternalGitBranchListResponse.  # noqa: E501


        :return: The branches of this ExternalGitBranchListResponse.  # noqa: E501
        :rtype: list[ProtoBranch]
        """
        return self._branches

    @branches.setter
    def branches(self, branches):
        """Sets the branches of this ExternalGitBranchListResponse.


        :param branches: The branches of this ExternalGitBranchListResponse.  # noqa: E501
        :type branches: list[ProtoBranch]
        """
        if self.local_vars_configuration.client_side_validation and branches is None:  # noqa: E501
            raise ValueError("Invalid value for `branches`, must not be `None`")  # noqa: E501

        self._branches = branches

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
        if not isinstance(other, ExternalGitBranchListResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ExternalGitBranchListResponse):
            return True

        return self.to_dict() != other.to_dict()
