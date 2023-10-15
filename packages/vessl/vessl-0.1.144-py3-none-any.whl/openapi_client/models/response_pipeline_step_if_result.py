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


class ResponsePipelineStepIfResult(object):
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
        'condition': 'V1BranchingCondition',
        'result': 'str'
    }

    attribute_map = {
        'condition': 'condition',
        'result': 'result'
    }

    def __init__(self, condition=None, result=None, local_vars_configuration=None):  # noqa: E501
        """ResponsePipelineStepIfResult - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._condition = None
        self._result = None
        self.discriminator = None

        self.condition = condition
        self.result = result

    @property
    def condition(self):
        """Gets the condition of this ResponsePipelineStepIfResult.  # noqa: E501


        :return: The condition of this ResponsePipelineStepIfResult.  # noqa: E501
        :rtype: V1BranchingCondition
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this ResponsePipelineStepIfResult.


        :param condition: The condition of this ResponsePipelineStepIfResult.  # noqa: E501
        :type condition: V1BranchingCondition
        """
        if self.local_vars_configuration.client_side_validation and condition is None:  # noqa: E501
            raise ValueError("Invalid value for `condition`, must not be `None`")  # noqa: E501

        self._condition = condition

    @property
    def result(self):
        """Gets the result of this ResponsePipelineStepIfResult.  # noqa: E501


        :return: The result of this ResponsePipelineStepIfResult.  # noqa: E501
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this ResponsePipelineStepIfResult.


        :param result: The result of this ResponsePipelineStepIfResult.  # noqa: E501
        :type result: str
        """

        self._result = result

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
        if not isinstance(other, ResponsePipelineStepIfResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResponsePipelineStepIfResult):
            return True

        return self.to_dict() != other.to_dict()
