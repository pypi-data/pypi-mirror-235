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


class OrmStorageEdges(object):
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
        'credentials': 'OrmOrganizationCredentials',
        'kernel_clusters': 'list[OrmKernelCluster]',
        'organization': 'OrmOrganization',
        'region': 'OrmRegion'
    }

    attribute_map = {
        'credentials': 'credentials',
        'kernel_clusters': 'kernel_clusters',
        'organization': 'organization',
        'region': 'region'
    }

    def __init__(self, credentials=None, kernel_clusters=None, organization=None, region=None, local_vars_configuration=None):  # noqa: E501
        """OrmStorageEdges - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._credentials = None
        self._kernel_clusters = None
        self._organization = None
        self._region = None
        self.discriminator = None

        if credentials is not None:
            self.credentials = credentials
        if kernel_clusters is not None:
            self.kernel_clusters = kernel_clusters
        if organization is not None:
            self.organization = organization
        if region is not None:
            self.region = region

    @property
    def credentials(self):
        """Gets the credentials of this OrmStorageEdges.  # noqa: E501


        :return: The credentials of this OrmStorageEdges.  # noqa: E501
        :rtype: OrmOrganizationCredentials
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this OrmStorageEdges.


        :param credentials: The credentials of this OrmStorageEdges.  # noqa: E501
        :type credentials: OrmOrganizationCredentials
        """

        self._credentials = credentials

    @property
    def kernel_clusters(self):
        """Gets the kernel_clusters of this OrmStorageEdges.  # noqa: E501


        :return: The kernel_clusters of this OrmStorageEdges.  # noqa: E501
        :rtype: list[OrmKernelCluster]
        """
        return self._kernel_clusters

    @kernel_clusters.setter
    def kernel_clusters(self, kernel_clusters):
        """Sets the kernel_clusters of this OrmStorageEdges.


        :param kernel_clusters: The kernel_clusters of this OrmStorageEdges.  # noqa: E501
        :type kernel_clusters: list[OrmKernelCluster]
        """

        self._kernel_clusters = kernel_clusters

    @property
    def organization(self):
        """Gets the organization of this OrmStorageEdges.  # noqa: E501


        :return: The organization of this OrmStorageEdges.  # noqa: E501
        :rtype: OrmOrganization
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this OrmStorageEdges.


        :param organization: The organization of this OrmStorageEdges.  # noqa: E501
        :type organization: OrmOrganization
        """

        self._organization = organization

    @property
    def region(self):
        """Gets the region of this OrmStorageEdges.  # noqa: E501


        :return: The region of this OrmStorageEdges.  # noqa: E501
        :rtype: OrmRegion
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this OrmStorageEdges.


        :param region: The region of this OrmStorageEdges.  # noqa: E501
        :type region: OrmRegion
        """

        self._region = region

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
        if not isinstance(other, OrmStorageEdges):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrmStorageEdges):
            return True

        return self.to_dict() != other.to_dict()
