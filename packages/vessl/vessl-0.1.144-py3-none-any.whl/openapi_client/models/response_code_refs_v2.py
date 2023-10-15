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


class ResponseCodeRefsV2(object):
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
        'git_ref': 'str',
        'mount_name': 'str',
        'mount_path': 'str',
        'protocol': 'str',
        'ref_http': 'ResponseCodeRefHTTP',
        'ref_ssh': 'ResponseCodeRefSSH'
    }

    attribute_map = {
        'git_ref': 'git_ref',
        'mount_name': 'mount_name',
        'mount_path': 'mount_path',
        'protocol': 'protocol',
        'ref_http': 'ref_http',
        'ref_ssh': 'ref_ssh'
    }

    def __init__(self, git_ref=None, mount_name=None, mount_path=None, protocol=None, ref_http=None, ref_ssh=None, local_vars_configuration=None):  # noqa: E501
        """ResponseCodeRefsV2 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._git_ref = None
        self._mount_name = None
        self._mount_path = None
        self._protocol = None
        self._ref_http = None
        self._ref_ssh = None
        self.discriminator = None

        self.git_ref = git_ref
        if mount_name is not None:
            self.mount_name = mount_name
        if mount_path is not None:
            self.mount_path = mount_path
        if protocol is not None:
            self.protocol = protocol
        if ref_http is not None:
            self.ref_http = ref_http
        if ref_ssh is not None:
            self.ref_ssh = ref_ssh

    @property
    def git_ref(self):
        """Gets the git_ref of this ResponseCodeRefsV2.  # noqa: E501


        :return: The git_ref of this ResponseCodeRefsV2.  # noqa: E501
        :rtype: str
        """
        return self._git_ref

    @git_ref.setter
    def git_ref(self, git_ref):
        """Sets the git_ref of this ResponseCodeRefsV2.


        :param git_ref: The git_ref of this ResponseCodeRefsV2.  # noqa: E501
        :type git_ref: str
        """

        self._git_ref = git_ref

    @property
    def mount_name(self):
        """Gets the mount_name of this ResponseCodeRefsV2.  # noqa: E501


        :return: The mount_name of this ResponseCodeRefsV2.  # noqa: E501
        :rtype: str
        """
        return self._mount_name

    @mount_name.setter
    def mount_name(self, mount_name):
        """Sets the mount_name of this ResponseCodeRefsV2.


        :param mount_name: The mount_name of this ResponseCodeRefsV2.  # noqa: E501
        :type mount_name: str
        """

        self._mount_name = mount_name

    @property
    def mount_path(self):
        """Gets the mount_path of this ResponseCodeRefsV2.  # noqa: E501


        :return: The mount_path of this ResponseCodeRefsV2.  # noqa: E501
        :rtype: str
        """
        return self._mount_path

    @mount_path.setter
    def mount_path(self, mount_path):
        """Sets the mount_path of this ResponseCodeRefsV2.


        :param mount_path: The mount_path of this ResponseCodeRefsV2.  # noqa: E501
        :type mount_path: str
        """

        self._mount_path = mount_path

    @property
    def protocol(self):
        """Gets the protocol of this ResponseCodeRefsV2.  # noqa: E501


        :return: The protocol of this ResponseCodeRefsV2.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this ResponseCodeRefsV2.


        :param protocol: The protocol of this ResponseCodeRefsV2.  # noqa: E501
        :type protocol: str
        """
        allowed_values = ["http", "ssh"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and protocol not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `protocol` ({0}), must be one of {1}"  # noqa: E501
                .format(protocol, allowed_values)
            )

        self._protocol = protocol

    @property
    def ref_http(self):
        """Gets the ref_http of this ResponseCodeRefsV2.  # noqa: E501


        :return: The ref_http of this ResponseCodeRefsV2.  # noqa: E501
        :rtype: ResponseCodeRefHTTP
        """
        return self._ref_http

    @ref_http.setter
    def ref_http(self, ref_http):
        """Sets the ref_http of this ResponseCodeRefsV2.


        :param ref_http: The ref_http of this ResponseCodeRefsV2.  # noqa: E501
        :type ref_http: ResponseCodeRefHTTP
        """

        self._ref_http = ref_http

    @property
    def ref_ssh(self):
        """Gets the ref_ssh of this ResponseCodeRefsV2.  # noqa: E501


        :return: The ref_ssh of this ResponseCodeRefsV2.  # noqa: E501
        :rtype: ResponseCodeRefSSH
        """
        return self._ref_ssh

    @ref_ssh.setter
    def ref_ssh(self, ref_ssh):
        """Sets the ref_ssh of this ResponseCodeRefsV2.


        :param ref_ssh: The ref_ssh of this ResponseCodeRefsV2.  # noqa: E501
        :type ref_ssh: ResponseCodeRefSSH
        """

        self._ref_ssh = ref_ssh

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
        if not isinstance(other, ResponseCodeRefsV2):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResponseCodeRefsV2):
            return True

        return self.to_dict() != other.to_dict()
