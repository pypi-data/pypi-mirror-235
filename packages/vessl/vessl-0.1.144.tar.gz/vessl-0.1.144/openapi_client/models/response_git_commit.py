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


class ResponseGitCommit(object):
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
        'author': 'ResponseGitCommitAuthor',
        'date': 'datetime',
        'message': 'str',
        'sha': 'str'
    }

    attribute_map = {
        'author': 'author',
        'date': 'date',
        'message': 'message',
        'sha': 'sha'
    }

    def __init__(self, author=None, date=None, message=None, sha=None, local_vars_configuration=None):  # noqa: E501
        """ResponseGitCommit - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._author = None
        self._date = None
        self._message = None
        self._sha = None
        self.discriminator = None

        if author is not None:
            self.author = author
        if date is not None:
            self.date = date
        if message is not None:
            self.message = message
        if sha is not None:
            self.sha = sha

    @property
    def author(self):
        """Gets the author of this ResponseGitCommit.  # noqa: E501


        :return: The author of this ResponseGitCommit.  # noqa: E501
        :rtype: ResponseGitCommitAuthor
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this ResponseGitCommit.


        :param author: The author of this ResponseGitCommit.  # noqa: E501
        :type author: ResponseGitCommitAuthor
        """

        self._author = author

    @property
    def date(self):
        """Gets the date of this ResponseGitCommit.  # noqa: E501


        :return: The date of this ResponseGitCommit.  # noqa: E501
        :rtype: datetime
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this ResponseGitCommit.


        :param date: The date of this ResponseGitCommit.  # noqa: E501
        :type date: datetime
        """

        self._date = date

    @property
    def message(self):
        """Gets the message of this ResponseGitCommit.  # noqa: E501


        :return: The message of this ResponseGitCommit.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ResponseGitCommit.


        :param message: The message of this ResponseGitCommit.  # noqa: E501
        :type message: str
        """

        self._message = message

    @property
    def sha(self):
        """Gets the sha of this ResponseGitCommit.  # noqa: E501


        :return: The sha of this ResponseGitCommit.  # noqa: E501
        :rtype: str
        """
        return self._sha

    @sha.setter
    def sha(self, sha):
        """Sets the sha of this ResponseGitCommit.


        :param sha: The sha of this ResponseGitCommit.  # noqa: E501
        :type sha: str
        """

        self._sha = sha

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
        if not isinstance(other, ResponseGitCommit):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResponseGitCommit):
            return True

        return self.to_dict() != other.to_dict()
