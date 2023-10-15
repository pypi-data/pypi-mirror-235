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


class ClusterClusterWorkload(object):
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
        'created_dt': 'datetime',
        'experiment': 'ResponseExperimentListResponse',
        'id': 'int',
        'kernel_cluster_node': 'ResponseKernelClusterNode',
        'kernel_resource_spec': 'ResponseKernelResourceSpec',
        'model_service_revision': 'ResponseModelServiceRevision',
        'run_execution': 'ResponseRunExecution',
        'status': 'str',
        'status_last_updated': 'datetime',
        'system_metrics': 'list[InfluxdbSystemMetricList]',
        'type': 'str',
        'workspace': 'ResponseWorkspaceList'
    }

    attribute_map = {
        'created_dt': 'created_dt',
        'experiment': 'experiment',
        'id': 'id',
        'kernel_cluster_node': 'kernel_cluster_node',
        'kernel_resource_spec': 'kernel_resource_spec',
        'model_service_revision': 'model_service_revision',
        'run_execution': 'run_execution',
        'status': 'status',
        'status_last_updated': 'status_last_updated',
        'system_metrics': 'system_metrics',
        'type': 'type',
        'workspace': 'workspace'
    }

    def __init__(self, created_dt=None, experiment=None, id=None, kernel_cluster_node=None, kernel_resource_spec=None, model_service_revision=None, run_execution=None, status=None, status_last_updated=None, system_metrics=None, type=None, workspace=None, local_vars_configuration=None):  # noqa: E501
        """ClusterClusterWorkload - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._created_dt = None
        self._experiment = None
        self._id = None
        self._kernel_cluster_node = None
        self._kernel_resource_spec = None
        self._model_service_revision = None
        self._run_execution = None
        self._status = None
        self._status_last_updated = None
        self._system_metrics = None
        self._type = None
        self._workspace = None
        self.discriminator = None

        self.created_dt = created_dt
        if experiment is not None:
            self.experiment = experiment
        self.id = id
        if kernel_cluster_node is not None:
            self.kernel_cluster_node = kernel_cluster_node
        if kernel_resource_spec is not None:
            self.kernel_resource_spec = kernel_resource_spec
        if model_service_revision is not None:
            self.model_service_revision = model_service_revision
        if run_execution is not None:
            self.run_execution = run_execution
        self.status = status
        self.status_last_updated = status_last_updated
        if system_metrics is not None:
            self.system_metrics = system_metrics
        self.type = type
        if workspace is not None:
            self.workspace = workspace

    @property
    def created_dt(self):
        """Gets the created_dt of this ClusterClusterWorkload.  # noqa: E501


        :return: The created_dt of this ClusterClusterWorkload.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this ClusterClusterWorkload.


        :param created_dt: The created_dt of this ClusterClusterWorkload.  # noqa: E501
        :type created_dt: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_dt is None:  # noqa: E501
            raise ValueError("Invalid value for `created_dt`, must not be `None`")  # noqa: E501

        self._created_dt = created_dt

    @property
    def experiment(self):
        """Gets the experiment of this ClusterClusterWorkload.  # noqa: E501


        :return: The experiment of this ClusterClusterWorkload.  # noqa: E501
        :rtype: ResponseExperimentListResponse
        """
        return self._experiment

    @experiment.setter
    def experiment(self, experiment):
        """Sets the experiment of this ClusterClusterWorkload.


        :param experiment: The experiment of this ClusterClusterWorkload.  # noqa: E501
        :type experiment: ResponseExperimentListResponse
        """

        self._experiment = experiment

    @property
    def id(self):
        """Gets the id of this ClusterClusterWorkload.  # noqa: E501


        :return: The id of this ClusterClusterWorkload.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ClusterClusterWorkload.


        :param id: The id of this ClusterClusterWorkload.  # noqa: E501
        :type id: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def kernel_cluster_node(self):
        """Gets the kernel_cluster_node of this ClusterClusterWorkload.  # noqa: E501


        :return: The kernel_cluster_node of this ClusterClusterWorkload.  # noqa: E501
        :rtype: ResponseKernelClusterNode
        """
        return self._kernel_cluster_node

    @kernel_cluster_node.setter
    def kernel_cluster_node(self, kernel_cluster_node):
        """Sets the kernel_cluster_node of this ClusterClusterWorkload.


        :param kernel_cluster_node: The kernel_cluster_node of this ClusterClusterWorkload.  # noqa: E501
        :type kernel_cluster_node: ResponseKernelClusterNode
        """

        self._kernel_cluster_node = kernel_cluster_node

    @property
    def kernel_resource_spec(self):
        """Gets the kernel_resource_spec of this ClusterClusterWorkload.  # noqa: E501


        :return: The kernel_resource_spec of this ClusterClusterWorkload.  # noqa: E501
        :rtype: ResponseKernelResourceSpec
        """
        return self._kernel_resource_spec

    @kernel_resource_spec.setter
    def kernel_resource_spec(self, kernel_resource_spec):
        """Sets the kernel_resource_spec of this ClusterClusterWorkload.


        :param kernel_resource_spec: The kernel_resource_spec of this ClusterClusterWorkload.  # noqa: E501
        :type kernel_resource_spec: ResponseKernelResourceSpec
        """

        self._kernel_resource_spec = kernel_resource_spec

    @property
    def model_service_revision(self):
        """Gets the model_service_revision of this ClusterClusterWorkload.  # noqa: E501


        :return: The model_service_revision of this ClusterClusterWorkload.  # noqa: E501
        :rtype: ResponseModelServiceRevision
        """
        return self._model_service_revision

    @model_service_revision.setter
    def model_service_revision(self, model_service_revision):
        """Sets the model_service_revision of this ClusterClusterWorkload.


        :param model_service_revision: The model_service_revision of this ClusterClusterWorkload.  # noqa: E501
        :type model_service_revision: ResponseModelServiceRevision
        """

        self._model_service_revision = model_service_revision

    @property
    def run_execution(self):
        """Gets the run_execution of this ClusterClusterWorkload.  # noqa: E501


        :return: The run_execution of this ClusterClusterWorkload.  # noqa: E501
        :rtype: ResponseRunExecution
        """
        return self._run_execution

    @run_execution.setter
    def run_execution(self, run_execution):
        """Sets the run_execution of this ClusterClusterWorkload.


        :param run_execution: The run_execution of this ClusterClusterWorkload.  # noqa: E501
        :type run_execution: ResponseRunExecution
        """

        self._run_execution = run_execution

    @property
    def status(self):
        """Gets the status of this ClusterClusterWorkload.  # noqa: E501


        :return: The status of this ClusterClusterWorkload.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ClusterClusterWorkload.


        :param status: The status of this ClusterClusterWorkload.  # noqa: E501
        :type status: str
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def status_last_updated(self):
        """Gets the status_last_updated of this ClusterClusterWorkload.  # noqa: E501


        :return: The status_last_updated of this ClusterClusterWorkload.  # noqa: E501
        :rtype: datetime
        """
        return self._status_last_updated

    @status_last_updated.setter
    def status_last_updated(self, status_last_updated):
        """Sets the status_last_updated of this ClusterClusterWorkload.


        :param status_last_updated: The status_last_updated of this ClusterClusterWorkload.  # noqa: E501
        :type status_last_updated: datetime
        """
        if self.local_vars_configuration.client_side_validation and status_last_updated is None:  # noqa: E501
            raise ValueError("Invalid value for `status_last_updated`, must not be `None`")  # noqa: E501

        self._status_last_updated = status_last_updated

    @property
    def system_metrics(self):
        """Gets the system_metrics of this ClusterClusterWorkload.  # noqa: E501


        :return: The system_metrics of this ClusterClusterWorkload.  # noqa: E501
        :rtype: list[InfluxdbSystemMetricList]
        """
        return self._system_metrics

    @system_metrics.setter
    def system_metrics(self, system_metrics):
        """Sets the system_metrics of this ClusterClusterWorkload.


        :param system_metrics: The system_metrics of this ClusterClusterWorkload.  # noqa: E501
        :type system_metrics: list[InfluxdbSystemMetricList]
        """

        self._system_metrics = system_metrics

    @property
    def type(self):
        """Gets the type of this ClusterClusterWorkload.  # noqa: E501


        :return: The type of this ClusterClusterWorkload.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ClusterClusterWorkload.


        :param type: The type of this ClusterClusterWorkload.  # noqa: E501
        :type type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def workspace(self):
        """Gets the workspace of this ClusterClusterWorkload.  # noqa: E501


        :return: The workspace of this ClusterClusterWorkload.  # noqa: E501
        :rtype: ResponseWorkspaceList
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this ClusterClusterWorkload.


        :param workspace: The workspace of this ClusterClusterWorkload.  # noqa: E501
        :type workspace: ResponseWorkspaceList
        """

        self._workspace = workspace

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
        if not isinstance(other, ClusterClusterWorkload):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ClusterClusterWorkload):
            return True

        return self.to_dict() != other.to_dict()
