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


class ResponseModelServiceRevision(object):
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
        'autoscaler_config': 'OrmAutoscalerConfig',
        'available_replicas': 'int',
        'cluster_node_ids': 'list[int]',
        'created_by': 'ResponseUser',
        'created_dt': 'datetime',
        'env_vars': 'OrmEnvVars',
        'id': 'int',
        'kernel_image': 'ResponseKernelImage',
        'kernel_resource_spec': 'ResponseKernelResourceSpec',
        'message': 'str',
        'model_service_name': 'str',
        'number': 'int',
        'ports': 'OrmWorkloadPorts',
        'service_account_name': 'str',
        'start_command': 'str',
        'status': 'str',
        'volume_mount_infos': 'ResponseVolumeMountInfos'
    }

    attribute_map = {
        'autoscaler_config': 'autoscaler_config',
        'available_replicas': 'available_replicas',
        'cluster_node_ids': 'cluster_node_ids',
        'created_by': 'created_by',
        'created_dt': 'created_dt',
        'env_vars': 'env_vars',
        'id': 'id',
        'kernel_image': 'kernel_image',
        'kernel_resource_spec': 'kernel_resource_spec',
        'message': 'message',
        'model_service_name': 'model_service_name',
        'number': 'number',
        'ports': 'ports',
        'service_account_name': 'service_account_name',
        'start_command': 'start_command',
        'status': 'status',
        'volume_mount_infos': 'volume_mount_infos'
    }

    def __init__(self, autoscaler_config=None, available_replicas=None, cluster_node_ids=None, created_by=None, created_dt=None, env_vars=None, id=None, kernel_image=None, kernel_resource_spec=None, message=None, model_service_name=None, number=None, ports=None, service_account_name=None, start_command=None, status=None, volume_mount_infos=None, local_vars_configuration=None):  # noqa: E501
        """ResponseModelServiceRevision - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._autoscaler_config = None
        self._available_replicas = None
        self._cluster_node_ids = None
        self._created_by = None
        self._created_dt = None
        self._env_vars = None
        self._id = None
        self._kernel_image = None
        self._kernel_resource_spec = None
        self._message = None
        self._model_service_name = None
        self._number = None
        self._ports = None
        self._service_account_name = None
        self._start_command = None
        self._status = None
        self._volume_mount_infos = None
        self.discriminator = None

        if autoscaler_config is not None:
            self.autoscaler_config = autoscaler_config
        self.available_replicas = available_replicas
        if cluster_node_ids is not None:
            self.cluster_node_ids = cluster_node_ids
        self.created_by = created_by
        self.created_dt = created_dt
        if env_vars is not None:
            self.env_vars = env_vars
        self.id = id
        if kernel_image is not None:
            self.kernel_image = kernel_image
        if kernel_resource_spec is not None:
            self.kernel_resource_spec = kernel_resource_spec
        self.message = message
        self.model_service_name = model_service_name
        self.number = number
        if ports is not None:
            self.ports = ports
        if service_account_name is not None:
            self.service_account_name = service_account_name
        if start_command is not None:
            self.start_command = start_command
        self.status = status
        if volume_mount_infos is not None:
            self.volume_mount_infos = volume_mount_infos

    @property
    def autoscaler_config(self):
        """Gets the autoscaler_config of this ResponseModelServiceRevision.  # noqa: E501


        :return: The autoscaler_config of this ResponseModelServiceRevision.  # noqa: E501
        :rtype: OrmAutoscalerConfig
        """
        return self._autoscaler_config

    @autoscaler_config.setter
    def autoscaler_config(self, autoscaler_config):
        """Sets the autoscaler_config of this ResponseModelServiceRevision.


        :param autoscaler_config: The autoscaler_config of this ResponseModelServiceRevision.  # noqa: E501
        :type autoscaler_config: OrmAutoscalerConfig
        """

        self._autoscaler_config = autoscaler_config

    @property
    def available_replicas(self):
        """Gets the available_replicas of this ResponseModelServiceRevision.  # noqa: E501


        :return: The available_replicas of this ResponseModelServiceRevision.  # noqa: E501
        :rtype: int
        """
        return self._available_replicas

    @available_replicas.setter
    def available_replicas(self, available_replicas):
        """Sets the available_replicas of this ResponseModelServiceRevision.


        :param available_replicas: The available_replicas of this ResponseModelServiceRevision.  # noqa: E501
        :type available_replicas: int
        """
        if self.local_vars_configuration.client_side_validation and available_replicas is None:  # noqa: E501
            raise ValueError("Invalid value for `available_replicas`, must not be `None`")  # noqa: E501

        self._available_replicas = available_replicas

    @property
    def cluster_node_ids(self):
        """Gets the cluster_node_ids of this ResponseModelServiceRevision.  # noqa: E501


        :return: The cluster_node_ids of this ResponseModelServiceRevision.  # noqa: E501
        :rtype: list[int]
        """
        return self._cluster_node_ids

    @cluster_node_ids.setter
    def cluster_node_ids(self, cluster_node_ids):
        """Sets the cluster_node_ids of this ResponseModelServiceRevision.


        :param cluster_node_ids: The cluster_node_ids of this ResponseModelServiceRevision.  # noqa: E501
        :type cluster_node_ids: list[int]
        """

        self._cluster_node_ids = cluster_node_ids

    @property
    def created_by(self):
        """Gets the created_by of this ResponseModelServiceRevision.  # noqa: E501


        :return: The created_by of this ResponseModelServiceRevision.  # noqa: E501
        :rtype: ResponseUser
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this ResponseModelServiceRevision.


        :param created_by: The created_by of this ResponseModelServiceRevision.  # noqa: E501
        :type created_by: ResponseUser
        """
        if self.local_vars_configuration.client_side_validation and created_by is None:  # noqa: E501
            raise ValueError("Invalid value for `created_by`, must not be `None`")  # noqa: E501

        self._created_by = created_by

    @property
    def created_dt(self):
        """Gets the created_dt of this ResponseModelServiceRevision.  # noqa: E501


        :return: The created_dt of this ResponseModelServiceRevision.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this ResponseModelServiceRevision.


        :param created_dt: The created_dt of this ResponseModelServiceRevision.  # noqa: E501
        :type created_dt: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_dt is None:  # noqa: E501
            raise ValueError("Invalid value for `created_dt`, must not be `None`")  # noqa: E501

        self._created_dt = created_dt

    @property
    def env_vars(self):
        """Gets the env_vars of this ResponseModelServiceRevision.  # noqa: E501


        :return: The env_vars of this ResponseModelServiceRevision.  # noqa: E501
        :rtype: OrmEnvVars
        """
        return self._env_vars

    @env_vars.setter
    def env_vars(self, env_vars):
        """Sets the env_vars of this ResponseModelServiceRevision.


        :param env_vars: The env_vars of this ResponseModelServiceRevision.  # noqa: E501
        :type env_vars: OrmEnvVars
        """

        self._env_vars = env_vars

    @property
    def id(self):
        """Gets the id of this ResponseModelServiceRevision.  # noqa: E501


        :return: The id of this ResponseModelServiceRevision.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ResponseModelServiceRevision.


        :param id: The id of this ResponseModelServiceRevision.  # noqa: E501
        :type id: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def kernel_image(self):
        """Gets the kernel_image of this ResponseModelServiceRevision.  # noqa: E501


        :return: The kernel_image of this ResponseModelServiceRevision.  # noqa: E501
        :rtype: ResponseKernelImage
        """
        return self._kernel_image

    @kernel_image.setter
    def kernel_image(self, kernel_image):
        """Sets the kernel_image of this ResponseModelServiceRevision.


        :param kernel_image: The kernel_image of this ResponseModelServiceRevision.  # noqa: E501
        :type kernel_image: ResponseKernelImage
        """

        self._kernel_image = kernel_image

    @property
    def kernel_resource_spec(self):
        """Gets the kernel_resource_spec of this ResponseModelServiceRevision.  # noqa: E501


        :return: The kernel_resource_spec of this ResponseModelServiceRevision.  # noqa: E501
        :rtype: ResponseKernelResourceSpec
        """
        return self._kernel_resource_spec

    @kernel_resource_spec.setter
    def kernel_resource_spec(self, kernel_resource_spec):
        """Sets the kernel_resource_spec of this ResponseModelServiceRevision.


        :param kernel_resource_spec: The kernel_resource_spec of this ResponseModelServiceRevision.  # noqa: E501
        :type kernel_resource_spec: ResponseKernelResourceSpec
        """

        self._kernel_resource_spec = kernel_resource_spec

    @property
    def message(self):
        """Gets the message of this ResponseModelServiceRevision.  # noqa: E501


        :return: The message of this ResponseModelServiceRevision.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ResponseModelServiceRevision.


        :param message: The message of this ResponseModelServiceRevision.  # noqa: E501
        :type message: str
        """
        if self.local_vars_configuration.client_side_validation and message is None:  # noqa: E501
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    @property
    def model_service_name(self):
        """Gets the model_service_name of this ResponseModelServiceRevision.  # noqa: E501


        :return: The model_service_name of this ResponseModelServiceRevision.  # noqa: E501
        :rtype: str
        """
        return self._model_service_name

    @model_service_name.setter
    def model_service_name(self, model_service_name):
        """Sets the model_service_name of this ResponseModelServiceRevision.


        :param model_service_name: The model_service_name of this ResponseModelServiceRevision.  # noqa: E501
        :type model_service_name: str
        """
        if self.local_vars_configuration.client_side_validation and model_service_name is None:  # noqa: E501
            raise ValueError("Invalid value for `model_service_name`, must not be `None`")  # noqa: E501

        self._model_service_name = model_service_name

    @property
    def number(self):
        """Gets the number of this ResponseModelServiceRevision.  # noqa: E501


        :return: The number of this ResponseModelServiceRevision.  # noqa: E501
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this ResponseModelServiceRevision.


        :param number: The number of this ResponseModelServiceRevision.  # noqa: E501
        :type number: int
        """
        if self.local_vars_configuration.client_side_validation and number is None:  # noqa: E501
            raise ValueError("Invalid value for `number`, must not be `None`")  # noqa: E501

        self._number = number

    @property
    def ports(self):
        """Gets the ports of this ResponseModelServiceRevision.  # noqa: E501


        :return: The ports of this ResponseModelServiceRevision.  # noqa: E501
        :rtype: OrmWorkloadPorts
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """Sets the ports of this ResponseModelServiceRevision.


        :param ports: The ports of this ResponseModelServiceRevision.  # noqa: E501
        :type ports: OrmWorkloadPorts
        """

        self._ports = ports

    @property
    def service_account_name(self):
        """Gets the service_account_name of this ResponseModelServiceRevision.  # noqa: E501


        :return: The service_account_name of this ResponseModelServiceRevision.  # noqa: E501
        :rtype: str
        """
        return self._service_account_name

    @service_account_name.setter
    def service_account_name(self, service_account_name):
        """Sets the service_account_name of this ResponseModelServiceRevision.


        :param service_account_name: The service_account_name of this ResponseModelServiceRevision.  # noqa: E501
        :type service_account_name: str
        """

        self._service_account_name = service_account_name

    @property
    def start_command(self):
        """Gets the start_command of this ResponseModelServiceRevision.  # noqa: E501


        :return: The start_command of this ResponseModelServiceRevision.  # noqa: E501
        :rtype: str
        """
        return self._start_command

    @start_command.setter
    def start_command(self, start_command):
        """Sets the start_command of this ResponseModelServiceRevision.


        :param start_command: The start_command of this ResponseModelServiceRevision.  # noqa: E501
        :type start_command: str
        """

        self._start_command = start_command

    @property
    def status(self):
        """Gets the status of this ResponseModelServiceRevision.  # noqa: E501


        :return: The status of this ResponseModelServiceRevision.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ResponseModelServiceRevision.


        :param status: The status of this ResponseModelServiceRevision.  # noqa: E501
        :type status: str
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def volume_mount_infos(self):
        """Gets the volume_mount_infos of this ResponseModelServiceRevision.  # noqa: E501


        :return: The volume_mount_infos of this ResponseModelServiceRevision.  # noqa: E501
        :rtype: ResponseVolumeMountInfos
        """
        return self._volume_mount_infos

    @volume_mount_infos.setter
    def volume_mount_infos(self, volume_mount_infos):
        """Sets the volume_mount_infos of this ResponseModelServiceRevision.


        :param volume_mount_infos: The volume_mount_infos of this ResponseModelServiceRevision.  # noqa: E501
        :type volume_mount_infos: ResponseVolumeMountInfos
        """

        self._volume_mount_infos = volume_mount_infos

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
        if not isinstance(other, ResponseModelServiceRevision):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResponseModelServiceRevision):
            return True

        return self.to_dict() != other.to_dict()
