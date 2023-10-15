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


class V1GSRefForm(object):
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
        'bucket': 'str',
        'credential_name': 'str',
        'prefix': 'str'
    }

    attribute_map = {
        'bucket': 'bucket',
        'credential_name': 'credential_name',
        'prefix': 'prefix'
    }

    def __init__(self, bucket=None, credential_name=None, prefix=None, local_vars_configuration=None):  # noqa: E501
        """V1GSRefForm - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._bucket = None
        self._credential_name = None
        self._prefix = None
        self.discriminator = None

        self.bucket = bucket
        self.credential_name = credential_name
        self.prefix = prefix

    @property
    def bucket(self):
        """Gets the bucket of this V1GSRefForm.  # noqa: E501


        :return: The bucket of this V1GSRefForm.  # noqa: E501
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        """Sets the bucket of this V1GSRefForm.


        :param bucket: The bucket of this V1GSRefForm.  # noqa: E501
        :type bucket: str
        """
        if self.local_vars_configuration.client_side_validation and bucket is None:  # noqa: E501
            raise ValueError("Invalid value for `bucket`, must not be `None`")  # noqa: E501

        self._bucket = bucket

    @property
    def credential_name(self):
        """Gets the credential_name of this V1GSRefForm.  # noqa: E501


        :return: The credential_name of this V1GSRefForm.  # noqa: E501
        :rtype: str
        """
        return self._credential_name

    @credential_name.setter
    def credential_name(self, credential_name):
        """Sets the credential_name of this V1GSRefForm.


        :param credential_name: The credential_name of this V1GSRefForm.  # noqa: E501
        :type credential_name: str
        """

        self._credential_name = credential_name

    @property
    def prefix(self):
        """Gets the prefix of this V1GSRefForm.  # noqa: E501


        :return: The prefix of this V1GSRefForm.  # noqa: E501
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """Sets the prefix of this V1GSRefForm.


        :param prefix: The prefix of this V1GSRefForm.  # noqa: E501
        :type prefix: str
        """
        if self.local_vars_configuration.client_side_validation and prefix is None:  # noqa: E501
            raise ValueError("Invalid value for `prefix`, must not be `None`")  # noqa: E501

        self._prefix = prefix

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
        if not isinstance(other, V1GSRefForm):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1GSRefForm):
            return True

        return self.to_dict() != other.to_dict()
