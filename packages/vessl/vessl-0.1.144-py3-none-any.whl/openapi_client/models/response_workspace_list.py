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


class ResponseWorkspaceList(object):
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
        'created_by': 'ResponseSimpleUser',
        'created_dt': 'datetime',
        'end_dt': 'datetime',
        'endpoints': 'ResponseWorkloadEndpoints',
        'histories': 'list[ResponseWorkloadHistoryInfo]',
        'id': 'int',
        'kernel_cluster': 'ResponseKernelCluster',
        'kernel_cluster_node': 'ResponseKernelClusterNode',
        'kernel_cluster_select_policies': 'OrmKernelClusterSelectPolicies',
        'kernel_resource_spec': 'ResponseKernelResourceSpec',
        'name': 'str',
        'organization': 'ResponseOrganization',
        'status': 'str',
        'status_last_updated': 'datetime',
        'status_reason': 'str',
        'updated_dt': 'datetime'
    }

    attribute_map = {
        'created_by': 'created_by',
        'created_dt': 'created_dt',
        'end_dt': 'end_dt',
        'endpoints': 'endpoints',
        'histories': 'histories',
        'id': 'id',
        'kernel_cluster': 'kernel_cluster',
        'kernel_cluster_node': 'kernel_cluster_node',
        'kernel_cluster_select_policies': 'kernel_cluster_select_policies',
        'kernel_resource_spec': 'kernel_resource_spec',
        'name': 'name',
        'organization': 'organization',
        'status': 'status',
        'status_last_updated': 'status_last_updated',
        'status_reason': 'status_reason',
        'updated_dt': 'updated_dt'
    }

    def __init__(self, created_by=None, created_dt=None, end_dt=None, endpoints=None, histories=None, id=None, kernel_cluster=None, kernel_cluster_node=None, kernel_cluster_select_policies=None, kernel_resource_spec=None, name=None, organization=None, status=None, status_last_updated=None, status_reason=None, updated_dt=None, local_vars_configuration=None):  # noqa: E501
        """ResponseWorkspaceList - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._created_by = None
        self._created_dt = None
        self._end_dt = None
        self._endpoints = None
        self._histories = None
        self._id = None
        self._kernel_cluster = None
        self._kernel_cluster_node = None
        self._kernel_cluster_select_policies = None
        self._kernel_resource_spec = None
        self._name = None
        self._organization = None
        self._status = None
        self._status_last_updated = None
        self._status_reason = None
        self._updated_dt = None
        self.discriminator = None

        self.created_by = created_by
        self.created_dt = created_dt
        self.end_dt = end_dt
        self.endpoints = endpoints
        self.histories = histories
        self.id = id
        if kernel_cluster is not None:
            self.kernel_cluster = kernel_cluster
        if kernel_cluster_node is not None:
            self.kernel_cluster_node = kernel_cluster_node
        self.kernel_cluster_select_policies = kernel_cluster_select_policies
        self.kernel_resource_spec = kernel_resource_spec
        self.name = name
        if organization is not None:
            self.organization = organization
        self.status = status
        self.status_last_updated = status_last_updated
        self.status_reason = status_reason
        self.updated_dt = updated_dt

    @property
    def created_by(self):
        """Gets the created_by of this ResponseWorkspaceList.  # noqa: E501


        :return: The created_by of this ResponseWorkspaceList.  # noqa: E501
        :rtype: ResponseSimpleUser
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this ResponseWorkspaceList.


        :param created_by: The created_by of this ResponseWorkspaceList.  # noqa: E501
        :type created_by: ResponseSimpleUser
        """
        if self.local_vars_configuration.client_side_validation and created_by is None:  # noqa: E501
            raise ValueError("Invalid value for `created_by`, must not be `None`")  # noqa: E501

        self._created_by = created_by

    @property
    def created_dt(self):
        """Gets the created_dt of this ResponseWorkspaceList.  # noqa: E501


        :return: The created_dt of this ResponseWorkspaceList.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this ResponseWorkspaceList.


        :param created_dt: The created_dt of this ResponseWorkspaceList.  # noqa: E501
        :type created_dt: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_dt is None:  # noqa: E501
            raise ValueError("Invalid value for `created_dt`, must not be `None`")  # noqa: E501

        self._created_dt = created_dt

    @property
    def end_dt(self):
        """Gets the end_dt of this ResponseWorkspaceList.  # noqa: E501


        :return: The end_dt of this ResponseWorkspaceList.  # noqa: E501
        :rtype: datetime
        """
        return self._end_dt

    @end_dt.setter
    def end_dt(self, end_dt):
        """Sets the end_dt of this ResponseWorkspaceList.


        :param end_dt: The end_dt of this ResponseWorkspaceList.  # noqa: E501
        :type end_dt: datetime
        """

        self._end_dt = end_dt

    @property
    def endpoints(self):
        """Gets the endpoints of this ResponseWorkspaceList.  # noqa: E501


        :return: The endpoints of this ResponseWorkspaceList.  # noqa: E501
        :rtype: ResponseWorkloadEndpoints
        """
        return self._endpoints

    @endpoints.setter
    def endpoints(self, endpoints):
        """Sets the endpoints of this ResponseWorkspaceList.


        :param endpoints: The endpoints of this ResponseWorkspaceList.  # noqa: E501
        :type endpoints: ResponseWorkloadEndpoints
        """
        if self.local_vars_configuration.client_side_validation and endpoints is None:  # noqa: E501
            raise ValueError("Invalid value for `endpoints`, must not be `None`")  # noqa: E501

        self._endpoints = endpoints

    @property
    def histories(self):
        """Gets the histories of this ResponseWorkspaceList.  # noqa: E501


        :return: The histories of this ResponseWorkspaceList.  # noqa: E501
        :rtype: list[ResponseWorkloadHistoryInfo]
        """
        return self._histories

    @histories.setter
    def histories(self, histories):
        """Sets the histories of this ResponseWorkspaceList.


        :param histories: The histories of this ResponseWorkspaceList.  # noqa: E501
        :type histories: list[ResponseWorkloadHistoryInfo]
        """
        if self.local_vars_configuration.client_side_validation and histories is None:  # noqa: E501
            raise ValueError("Invalid value for `histories`, must not be `None`")  # noqa: E501

        self._histories = histories

    @property
    def id(self):
        """Gets the id of this ResponseWorkspaceList.  # noqa: E501


        :return: The id of this ResponseWorkspaceList.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ResponseWorkspaceList.


        :param id: The id of this ResponseWorkspaceList.  # noqa: E501
        :type id: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def kernel_cluster(self):
        """Gets the kernel_cluster of this ResponseWorkspaceList.  # noqa: E501


        :return: The kernel_cluster of this ResponseWorkspaceList.  # noqa: E501
        :rtype: ResponseKernelCluster
        """
        return self._kernel_cluster

    @kernel_cluster.setter
    def kernel_cluster(self, kernel_cluster):
        """Sets the kernel_cluster of this ResponseWorkspaceList.


        :param kernel_cluster: The kernel_cluster of this ResponseWorkspaceList.  # noqa: E501
        :type kernel_cluster: ResponseKernelCluster
        """

        self._kernel_cluster = kernel_cluster

    @property
    def kernel_cluster_node(self):
        """Gets the kernel_cluster_node of this ResponseWorkspaceList.  # noqa: E501


        :return: The kernel_cluster_node of this ResponseWorkspaceList.  # noqa: E501
        :rtype: ResponseKernelClusterNode
        """
        return self._kernel_cluster_node

    @kernel_cluster_node.setter
    def kernel_cluster_node(self, kernel_cluster_node):
        """Sets the kernel_cluster_node of this ResponseWorkspaceList.


        :param kernel_cluster_node: The kernel_cluster_node of this ResponseWorkspaceList.  # noqa: E501
        :type kernel_cluster_node: ResponseKernelClusterNode
        """

        self._kernel_cluster_node = kernel_cluster_node

    @property
    def kernel_cluster_select_policies(self):
        """Gets the kernel_cluster_select_policies of this ResponseWorkspaceList.  # noqa: E501


        :return: The kernel_cluster_select_policies of this ResponseWorkspaceList.  # noqa: E501
        :rtype: OrmKernelClusterSelectPolicies
        """
        return self._kernel_cluster_select_policies

    @kernel_cluster_select_policies.setter
    def kernel_cluster_select_policies(self, kernel_cluster_select_policies):
        """Sets the kernel_cluster_select_policies of this ResponseWorkspaceList.


        :param kernel_cluster_select_policies: The kernel_cluster_select_policies of this ResponseWorkspaceList.  # noqa: E501
        :type kernel_cluster_select_policies: OrmKernelClusterSelectPolicies
        """
        if self.local_vars_configuration.client_side_validation and kernel_cluster_select_policies is None:  # noqa: E501
            raise ValueError("Invalid value for `kernel_cluster_select_policies`, must not be `None`")  # noqa: E501

        self._kernel_cluster_select_policies = kernel_cluster_select_policies

    @property
    def kernel_resource_spec(self):
        """Gets the kernel_resource_spec of this ResponseWorkspaceList.  # noqa: E501


        :return: The kernel_resource_spec of this ResponseWorkspaceList.  # noqa: E501
        :rtype: ResponseKernelResourceSpec
        """
        return self._kernel_resource_spec

    @kernel_resource_spec.setter
    def kernel_resource_spec(self, kernel_resource_spec):
        """Sets the kernel_resource_spec of this ResponseWorkspaceList.


        :param kernel_resource_spec: The kernel_resource_spec of this ResponseWorkspaceList.  # noqa: E501
        :type kernel_resource_spec: ResponseKernelResourceSpec
        """
        if self.local_vars_configuration.client_side_validation and kernel_resource_spec is None:  # noqa: E501
            raise ValueError("Invalid value for `kernel_resource_spec`, must not be `None`")  # noqa: E501

        self._kernel_resource_spec = kernel_resource_spec

    @property
    def name(self):
        """Gets the name of this ResponseWorkspaceList.  # noqa: E501


        :return: The name of this ResponseWorkspaceList.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ResponseWorkspaceList.


        :param name: The name of this ResponseWorkspaceList.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def organization(self):
        """Gets the organization of this ResponseWorkspaceList.  # noqa: E501


        :return: The organization of this ResponseWorkspaceList.  # noqa: E501
        :rtype: ResponseOrganization
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this ResponseWorkspaceList.


        :param organization: The organization of this ResponseWorkspaceList.  # noqa: E501
        :type organization: ResponseOrganization
        """

        self._organization = organization

    @property
    def status(self):
        """Gets the status of this ResponseWorkspaceList.  # noqa: E501


        :return: The status of this ResponseWorkspaceList.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ResponseWorkspaceList.


        :param status: The status of this ResponseWorkspaceList.  # noqa: E501
        :type status: str
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def status_last_updated(self):
        """Gets the status_last_updated of this ResponseWorkspaceList.  # noqa: E501


        :return: The status_last_updated of this ResponseWorkspaceList.  # noqa: E501
        :rtype: datetime
        """
        return self._status_last_updated

    @status_last_updated.setter
    def status_last_updated(self, status_last_updated):
        """Sets the status_last_updated of this ResponseWorkspaceList.


        :param status_last_updated: The status_last_updated of this ResponseWorkspaceList.  # noqa: E501
        :type status_last_updated: datetime
        """
        if self.local_vars_configuration.client_side_validation and status_last_updated is None:  # noqa: E501
            raise ValueError("Invalid value for `status_last_updated`, must not be `None`")  # noqa: E501

        self._status_last_updated = status_last_updated

    @property
    def status_reason(self):
        """Gets the status_reason of this ResponseWorkspaceList.  # noqa: E501


        :return: The status_reason of this ResponseWorkspaceList.  # noqa: E501
        :rtype: str
        """
        return self._status_reason

    @status_reason.setter
    def status_reason(self, status_reason):
        """Sets the status_reason of this ResponseWorkspaceList.


        :param status_reason: The status_reason of this ResponseWorkspaceList.  # noqa: E501
        :type status_reason: str
        """
        if self.local_vars_configuration.client_side_validation and status_reason is None:  # noqa: E501
            raise ValueError("Invalid value for `status_reason`, must not be `None`")  # noqa: E501

        self._status_reason = status_reason

    @property
    def updated_dt(self):
        """Gets the updated_dt of this ResponseWorkspaceList.  # noqa: E501


        :return: The updated_dt of this ResponseWorkspaceList.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_dt

    @updated_dt.setter
    def updated_dt(self, updated_dt):
        """Sets the updated_dt of this ResponseWorkspaceList.


        :param updated_dt: The updated_dt of this ResponseWorkspaceList.  # noqa: E501
        :type updated_dt: datetime
        """
        if self.local_vars_configuration.client_side_validation and updated_dt is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_dt`, must not be `None`")  # noqa: E501

        self._updated_dt = updated_dt

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
        if not isinstance(other, ResponseWorkspaceList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResponseWorkspaceList):
            return True

        return self.to_dict() != other.to_dict()
