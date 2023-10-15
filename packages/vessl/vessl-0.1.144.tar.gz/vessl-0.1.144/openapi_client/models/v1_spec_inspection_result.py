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


class V1SpecInspectionResult(object):
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
        'errors': 'list[V1SpecError]',
        'is_spec_valid': 'bool',
        'warnings': 'list[V1SpecError]'
    }

    attribute_map = {
        'errors': 'errors',
        'is_spec_valid': 'is_spec_valid',
        'warnings': 'warnings'
    }

    def __init__(self, errors=None, is_spec_valid=None, warnings=None, local_vars_configuration=None):  # noqa: E501
        """V1SpecInspectionResult - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._errors = None
        self._is_spec_valid = None
        self._warnings = None
        self.discriminator = None

        if errors is not None:
            self.errors = errors
        if is_spec_valid is not None:
            self.is_spec_valid = is_spec_valid
        if warnings is not None:
            self.warnings = warnings

    @property
    def errors(self):
        """Gets the errors of this V1SpecInspectionResult.  # noqa: E501


        :return: The errors of this V1SpecInspectionResult.  # noqa: E501
        :rtype: list[V1SpecError]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this V1SpecInspectionResult.


        :param errors: The errors of this V1SpecInspectionResult.  # noqa: E501
        :type errors: list[V1SpecError]
        """

        self._errors = errors

    @property
    def is_spec_valid(self):
        """Gets the is_spec_valid of this V1SpecInspectionResult.  # noqa: E501


        :return: The is_spec_valid of this V1SpecInspectionResult.  # noqa: E501
        :rtype: bool
        """
        return self._is_spec_valid

    @is_spec_valid.setter
    def is_spec_valid(self, is_spec_valid):
        """Sets the is_spec_valid of this V1SpecInspectionResult.


        :param is_spec_valid: The is_spec_valid of this V1SpecInspectionResult.  # noqa: E501
        :type is_spec_valid: bool
        """

        self._is_spec_valid = is_spec_valid

    @property
    def warnings(self):
        """Gets the warnings of this V1SpecInspectionResult.  # noqa: E501


        :return: The warnings of this V1SpecInspectionResult.  # noqa: E501
        :rtype: list[V1SpecError]
        """
        return self._warnings

    @warnings.setter
    def warnings(self, warnings):
        """Sets the warnings of this V1SpecInspectionResult.


        :param warnings: The warnings of this V1SpecInspectionResult.  # noqa: E501
        :type warnings: list[V1SpecError]
        """

        self._warnings = warnings

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
        if not isinstance(other, V1SpecInspectionResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1SpecInspectionResult):
            return True

        return self.to_dict() != other.to_dict()
