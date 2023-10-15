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


class OrmAccessControlPolicyEdges(object):
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
        'group': 'OrmGroup',
        'organization': 'OrmOrganization',
        'project': 'OrmProject',
        'root_organization': 'OrmOrganization',
        'user': 'OrmUser'
    }

    attribute_map = {
        'group': 'group',
        'organization': 'organization',
        'project': 'project',
        'root_organization': 'root_organization',
        'user': 'user'
    }

    def __init__(self, group=None, organization=None, project=None, root_organization=None, user=None, local_vars_configuration=None):  # noqa: E501
        """OrmAccessControlPolicyEdges - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._group = None
        self._organization = None
        self._project = None
        self._root_organization = None
        self._user = None
        self.discriminator = None

        if group is not None:
            self.group = group
        if organization is not None:
            self.organization = organization
        if project is not None:
            self.project = project
        if root_organization is not None:
            self.root_organization = root_organization
        if user is not None:
            self.user = user

    @property
    def group(self):
        """Gets the group of this OrmAccessControlPolicyEdges.  # noqa: E501


        :return: The group of this OrmAccessControlPolicyEdges.  # noqa: E501
        :rtype: OrmGroup
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this OrmAccessControlPolicyEdges.


        :param group: The group of this OrmAccessControlPolicyEdges.  # noqa: E501
        :type group: OrmGroup
        """

        self._group = group

    @property
    def organization(self):
        """Gets the organization of this OrmAccessControlPolicyEdges.  # noqa: E501


        :return: The organization of this OrmAccessControlPolicyEdges.  # noqa: E501
        :rtype: OrmOrganization
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this OrmAccessControlPolicyEdges.


        :param organization: The organization of this OrmAccessControlPolicyEdges.  # noqa: E501
        :type organization: OrmOrganization
        """

        self._organization = organization

    @property
    def project(self):
        """Gets the project of this OrmAccessControlPolicyEdges.  # noqa: E501


        :return: The project of this OrmAccessControlPolicyEdges.  # noqa: E501
        :rtype: OrmProject
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this OrmAccessControlPolicyEdges.


        :param project: The project of this OrmAccessControlPolicyEdges.  # noqa: E501
        :type project: OrmProject
        """

        self._project = project

    @property
    def root_organization(self):
        """Gets the root_organization of this OrmAccessControlPolicyEdges.  # noqa: E501


        :return: The root_organization of this OrmAccessControlPolicyEdges.  # noqa: E501
        :rtype: OrmOrganization
        """
        return self._root_organization

    @root_organization.setter
    def root_organization(self, root_organization):
        """Sets the root_organization of this OrmAccessControlPolicyEdges.


        :param root_organization: The root_organization of this OrmAccessControlPolicyEdges.  # noqa: E501
        :type root_organization: OrmOrganization
        """

        self._root_organization = root_organization

    @property
    def user(self):
        """Gets the user of this OrmAccessControlPolicyEdges.  # noqa: E501


        :return: The user of this OrmAccessControlPolicyEdges.  # noqa: E501
        :rtype: OrmUser
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this OrmAccessControlPolicyEdges.


        :param user: The user of this OrmAccessControlPolicyEdges.  # noqa: E501
        :type user: OrmUser
        """

        self._user = user

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
        if not isinstance(other, OrmAccessControlPolicyEdges):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrmAccessControlPolicyEdges):
            return True

        return self.to_dict() != other.to_dict()
