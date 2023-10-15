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


class OrmModelServiceEdges(object):
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
        'created_by': 'OrmUser',
        'gateway': 'OrmModelServiceGateway',
        'kernel_cluster': 'OrmKernelCluster',
        'last_updated_by': 'OrmUser',
        'organization': 'OrmOrganization',
        'revisions': 'list[OrmModelServiceRevision]',
        'rollouts': 'list[OrmModelServiceRollout]'
    }

    attribute_map = {
        'created_by': 'created_by',
        'gateway': 'gateway',
        'kernel_cluster': 'kernel_cluster',
        'last_updated_by': 'last_updated_by',
        'organization': 'organization',
        'revisions': 'revisions',
        'rollouts': 'rollouts'
    }

    def __init__(self, created_by=None, gateway=None, kernel_cluster=None, last_updated_by=None, organization=None, revisions=None, rollouts=None, local_vars_configuration=None):  # noqa: E501
        """OrmModelServiceEdges - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._created_by = None
        self._gateway = None
        self._kernel_cluster = None
        self._last_updated_by = None
        self._organization = None
        self._revisions = None
        self._rollouts = None
        self.discriminator = None

        if created_by is not None:
            self.created_by = created_by
        if gateway is not None:
            self.gateway = gateway
        if kernel_cluster is not None:
            self.kernel_cluster = kernel_cluster
        if last_updated_by is not None:
            self.last_updated_by = last_updated_by
        if organization is not None:
            self.organization = organization
        if revisions is not None:
            self.revisions = revisions
        if rollouts is not None:
            self.rollouts = rollouts

    @property
    def created_by(self):
        """Gets the created_by of this OrmModelServiceEdges.  # noqa: E501


        :return: The created_by of this OrmModelServiceEdges.  # noqa: E501
        :rtype: OrmUser
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this OrmModelServiceEdges.


        :param created_by: The created_by of this OrmModelServiceEdges.  # noqa: E501
        :type created_by: OrmUser
        """

        self._created_by = created_by

    @property
    def gateway(self):
        """Gets the gateway of this OrmModelServiceEdges.  # noqa: E501


        :return: The gateway of this OrmModelServiceEdges.  # noqa: E501
        :rtype: OrmModelServiceGateway
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway):
        """Sets the gateway of this OrmModelServiceEdges.


        :param gateway: The gateway of this OrmModelServiceEdges.  # noqa: E501
        :type gateway: OrmModelServiceGateway
        """

        self._gateway = gateway

    @property
    def kernel_cluster(self):
        """Gets the kernel_cluster of this OrmModelServiceEdges.  # noqa: E501


        :return: The kernel_cluster of this OrmModelServiceEdges.  # noqa: E501
        :rtype: OrmKernelCluster
        """
        return self._kernel_cluster

    @kernel_cluster.setter
    def kernel_cluster(self, kernel_cluster):
        """Sets the kernel_cluster of this OrmModelServiceEdges.


        :param kernel_cluster: The kernel_cluster of this OrmModelServiceEdges.  # noqa: E501
        :type kernel_cluster: OrmKernelCluster
        """

        self._kernel_cluster = kernel_cluster

    @property
    def last_updated_by(self):
        """Gets the last_updated_by of this OrmModelServiceEdges.  # noqa: E501


        :return: The last_updated_by of this OrmModelServiceEdges.  # noqa: E501
        :rtype: OrmUser
        """
        return self._last_updated_by

    @last_updated_by.setter
    def last_updated_by(self, last_updated_by):
        """Sets the last_updated_by of this OrmModelServiceEdges.


        :param last_updated_by: The last_updated_by of this OrmModelServiceEdges.  # noqa: E501
        :type last_updated_by: OrmUser
        """

        self._last_updated_by = last_updated_by

    @property
    def organization(self):
        """Gets the organization of this OrmModelServiceEdges.  # noqa: E501


        :return: The organization of this OrmModelServiceEdges.  # noqa: E501
        :rtype: OrmOrganization
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this OrmModelServiceEdges.


        :param organization: The organization of this OrmModelServiceEdges.  # noqa: E501
        :type organization: OrmOrganization
        """

        self._organization = organization

    @property
    def revisions(self):
        """Gets the revisions of this OrmModelServiceEdges.  # noqa: E501


        :return: The revisions of this OrmModelServiceEdges.  # noqa: E501
        :rtype: list[OrmModelServiceRevision]
        """
        return self._revisions

    @revisions.setter
    def revisions(self, revisions):
        """Sets the revisions of this OrmModelServiceEdges.


        :param revisions: The revisions of this OrmModelServiceEdges.  # noqa: E501
        :type revisions: list[OrmModelServiceRevision]
        """

        self._revisions = revisions

    @property
    def rollouts(self):
        """Gets the rollouts of this OrmModelServiceEdges.  # noqa: E501


        :return: The rollouts of this OrmModelServiceEdges.  # noqa: E501
        :rtype: list[OrmModelServiceRollout]
        """
        return self._rollouts

    @rollouts.setter
    def rollouts(self, rollouts):
        """Sets the rollouts of this OrmModelServiceEdges.


        :param rollouts: The rollouts of this OrmModelServiceEdges.  # noqa: E501
        :type rollouts: list[OrmModelServiceRollout]
        """

        self._rollouts = rollouts

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
        if not isinstance(other, OrmModelServiceEdges):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrmModelServiceEdges):
            return True

        return self.to_dict() != other.to_dict()
