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


class ResponsePipelineStepNotificationResult(object):
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
        'email_addresses': 'list[str]',
        'email_contents': 'str',
        'email_subject': 'str'
    }

    attribute_map = {
        'email_addresses': 'email_addresses',
        'email_contents': 'email_contents',
        'email_subject': 'email_subject'
    }

    def __init__(self, email_addresses=None, email_contents=None, email_subject=None, local_vars_configuration=None):  # noqa: E501
        """ResponsePipelineStepNotificationResult - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._email_addresses = None
        self._email_contents = None
        self._email_subject = None
        self.discriminator = None

        if email_addresses is not None:
            self.email_addresses = email_addresses
        if email_contents is not None:
            self.email_contents = email_contents
        if email_subject is not None:
            self.email_subject = email_subject

    @property
    def email_addresses(self):
        """Gets the email_addresses of this ResponsePipelineStepNotificationResult.  # noqa: E501


        :return: The email_addresses of this ResponsePipelineStepNotificationResult.  # noqa: E501
        :rtype: list[str]
        """
        return self._email_addresses

    @email_addresses.setter
    def email_addresses(self, email_addresses):
        """Sets the email_addresses of this ResponsePipelineStepNotificationResult.


        :param email_addresses: The email_addresses of this ResponsePipelineStepNotificationResult.  # noqa: E501
        :type email_addresses: list[str]
        """

        self._email_addresses = email_addresses

    @property
    def email_contents(self):
        """Gets the email_contents of this ResponsePipelineStepNotificationResult.  # noqa: E501


        :return: The email_contents of this ResponsePipelineStepNotificationResult.  # noqa: E501
        :rtype: str
        """
        return self._email_contents

    @email_contents.setter
    def email_contents(self, email_contents):
        """Sets the email_contents of this ResponsePipelineStepNotificationResult.


        :param email_contents: The email_contents of this ResponsePipelineStepNotificationResult.  # noqa: E501
        :type email_contents: str
        """

        self._email_contents = email_contents

    @property
    def email_subject(self):
        """Gets the email_subject of this ResponsePipelineStepNotificationResult.  # noqa: E501


        :return: The email_subject of this ResponsePipelineStepNotificationResult.  # noqa: E501
        :rtype: str
        """
        return self._email_subject

    @email_subject.setter
    def email_subject(self, email_subject):
        """Sets the email_subject of this ResponsePipelineStepNotificationResult.


        :param email_subject: The email_subject of this ResponsePipelineStepNotificationResult.  # noqa: E501
        :type email_subject: str
        """

        self._email_subject = email_subject

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
        if not isinstance(other, ResponsePipelineStepNotificationResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResponsePipelineStepNotificationResult):
            return True

        return self.to_dict() != other.to_dict()
