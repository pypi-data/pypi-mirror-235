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


class WorkspaceCreateAPIInput(object):
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
        'cluster_id': 'int',
        'cluster_node_ids': 'list[int]',
        'docker_credentials_id': 'int',
        'idle_shutdown_minutes': 'int',
        'image_url': 'str',
        'init_script': 'str',
        'max_hours': 'int',
        'name': 'str',
        'ports': 'list[OrmWorkspacePort]',
        'resource_spec': 'OrmKernelResourceSpecField',
        'resource_spec_id': 'int',
        'service_account_name': 'str',
        'start_command': 'str',
        'volumes': 'OrmVolumeMountRequests'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'cluster_node_ids': 'cluster_node_ids',
        'docker_credentials_id': 'docker_credentials_id',
        'idle_shutdown_minutes': 'idle_shutdown_minutes',
        'image_url': 'image_url',
        'init_script': 'init_script',
        'max_hours': 'max_hours',
        'name': 'name',
        'ports': 'ports',
        'resource_spec': 'resource_spec',
        'resource_spec_id': 'resource_spec_id',
        'service_account_name': 'service_account_name',
        'start_command': 'start_command',
        'volumes': 'volumes'
    }

    def __init__(self, cluster_id=None, cluster_node_ids=None, docker_credentials_id=None, idle_shutdown_minutes=None, image_url=None, init_script=None, max_hours=None, name=None, ports=None, resource_spec=None, resource_spec_id=None, service_account_name=None, start_command=None, volumes=None, local_vars_configuration=None):  # noqa: E501
        """WorkspaceCreateAPIInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._cluster_id = None
        self._cluster_node_ids = None
        self._docker_credentials_id = None
        self._idle_shutdown_minutes = None
        self._image_url = None
        self._init_script = None
        self._max_hours = None
        self._name = None
        self._ports = None
        self._resource_spec = None
        self._resource_spec_id = None
        self._service_account_name = None
        self._start_command = None
        self._volumes = None
        self.discriminator = None

        self.cluster_id = cluster_id
        if cluster_node_ids is not None:
            self.cluster_node_ids = cluster_node_ids
        self.docker_credentials_id = docker_credentials_id
        if idle_shutdown_minutes is not None:
            self.idle_shutdown_minutes = idle_shutdown_minutes
        self.image_url = image_url
        self.init_script = init_script
        if max_hours is not None:
            self.max_hours = max_hours
        self.name = name
        self.ports = ports
        if resource_spec is not None:
            self.resource_spec = resource_spec
        self.resource_spec_id = resource_spec_id
        if service_account_name is not None:
            self.service_account_name = service_account_name
        self.start_command = start_command
        self.volumes = volumes

    @property
    def cluster_id(self):
        """Gets the cluster_id of this WorkspaceCreateAPIInput.  # noqa: E501


        :return: The cluster_id of this WorkspaceCreateAPIInput.  # noqa: E501
        :rtype: int
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this WorkspaceCreateAPIInput.


        :param cluster_id: The cluster_id of this WorkspaceCreateAPIInput.  # noqa: E501
        :type cluster_id: int
        """
        if self.local_vars_configuration.client_side_validation and cluster_id is None:  # noqa: E501
            raise ValueError("Invalid value for `cluster_id`, must not be `None`")  # noqa: E501

        self._cluster_id = cluster_id

    @property
    def cluster_node_ids(self):
        """Gets the cluster_node_ids of this WorkspaceCreateAPIInput.  # noqa: E501


        :return: The cluster_node_ids of this WorkspaceCreateAPIInput.  # noqa: E501
        :rtype: list[int]
        """
        return self._cluster_node_ids

    @cluster_node_ids.setter
    def cluster_node_ids(self, cluster_node_ids):
        """Sets the cluster_node_ids of this WorkspaceCreateAPIInput.


        :param cluster_node_ids: The cluster_node_ids of this WorkspaceCreateAPIInput.  # noqa: E501
        :type cluster_node_ids: list[int]
        """

        self._cluster_node_ids = cluster_node_ids

    @property
    def docker_credentials_id(self):
        """Gets the docker_credentials_id of this WorkspaceCreateAPIInput.  # noqa: E501


        :return: The docker_credentials_id of this WorkspaceCreateAPIInput.  # noqa: E501
        :rtype: int
        """
        return self._docker_credentials_id

    @docker_credentials_id.setter
    def docker_credentials_id(self, docker_credentials_id):
        """Sets the docker_credentials_id of this WorkspaceCreateAPIInput.


        :param docker_credentials_id: The docker_credentials_id of this WorkspaceCreateAPIInput.  # noqa: E501
        :type docker_credentials_id: int
        """

        self._docker_credentials_id = docker_credentials_id

    @property
    def idle_shutdown_minutes(self):
        """Gets the idle_shutdown_minutes of this WorkspaceCreateAPIInput.  # noqa: E501


        :return: The idle_shutdown_minutes of this WorkspaceCreateAPIInput.  # noqa: E501
        :rtype: int
        """
        return self._idle_shutdown_minutes

    @idle_shutdown_minutes.setter
    def idle_shutdown_minutes(self, idle_shutdown_minutes):
        """Sets the idle_shutdown_minutes of this WorkspaceCreateAPIInput.


        :param idle_shutdown_minutes: The idle_shutdown_minutes of this WorkspaceCreateAPIInput.  # noqa: E501
        :type idle_shutdown_minutes: int
        """

        self._idle_shutdown_minutes = idle_shutdown_minutes

    @property
    def image_url(self):
        """Gets the image_url of this WorkspaceCreateAPIInput.  # noqa: E501


        :return: The image_url of this WorkspaceCreateAPIInput.  # noqa: E501
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """Sets the image_url of this WorkspaceCreateAPIInput.


        :param image_url: The image_url of this WorkspaceCreateAPIInput.  # noqa: E501
        :type image_url: str
        """
        if self.local_vars_configuration.client_side_validation and image_url is None:  # noqa: E501
            raise ValueError("Invalid value for `image_url`, must not be `None`")  # noqa: E501

        self._image_url = image_url

    @property
    def init_script(self):
        """Gets the init_script of this WorkspaceCreateAPIInput.  # noqa: E501


        :return: The init_script of this WorkspaceCreateAPIInput.  # noqa: E501
        :rtype: str
        """
        return self._init_script

    @init_script.setter
    def init_script(self, init_script):
        """Sets the init_script of this WorkspaceCreateAPIInput.


        :param init_script: The init_script of this WorkspaceCreateAPIInput.  # noqa: E501
        :type init_script: str
        """

        self._init_script = init_script

    @property
    def max_hours(self):
        """Gets the max_hours of this WorkspaceCreateAPIInput.  # noqa: E501


        :return: The max_hours of this WorkspaceCreateAPIInput.  # noqa: E501
        :rtype: int
        """
        return self._max_hours

    @max_hours.setter
    def max_hours(self, max_hours):
        """Sets the max_hours of this WorkspaceCreateAPIInput.


        :param max_hours: The max_hours of this WorkspaceCreateAPIInput.  # noqa: E501
        :type max_hours: int
        """

        self._max_hours = max_hours

    @property
    def name(self):
        """Gets the name of this WorkspaceCreateAPIInput.  # noqa: E501


        :return: The name of this WorkspaceCreateAPIInput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WorkspaceCreateAPIInput.


        :param name: The name of this WorkspaceCreateAPIInput.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 255):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501

        self._name = name

    @property
    def ports(self):
        """Gets the ports of this WorkspaceCreateAPIInput.  # noqa: E501


        :return: The ports of this WorkspaceCreateAPIInput.  # noqa: E501
        :rtype: list[OrmWorkspacePort]
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """Sets the ports of this WorkspaceCreateAPIInput.


        :param ports: The ports of this WorkspaceCreateAPIInput.  # noqa: E501
        :type ports: list[OrmWorkspacePort]
        """
        if self.local_vars_configuration.client_side_validation and ports is None:  # noqa: E501
            raise ValueError("Invalid value for `ports`, must not be `None`")  # noqa: E501

        self._ports = ports

    @property
    def resource_spec(self):
        """Gets the resource_spec of this WorkspaceCreateAPIInput.  # noqa: E501


        :return: The resource_spec of this WorkspaceCreateAPIInput.  # noqa: E501
        :rtype: OrmKernelResourceSpecField
        """
        return self._resource_spec

    @resource_spec.setter
    def resource_spec(self, resource_spec):
        """Sets the resource_spec of this WorkspaceCreateAPIInput.


        :param resource_spec: The resource_spec of this WorkspaceCreateAPIInput.  # noqa: E501
        :type resource_spec: OrmKernelResourceSpecField
        """

        self._resource_spec = resource_spec

    @property
    def resource_spec_id(self):
        """Gets the resource_spec_id of this WorkspaceCreateAPIInput.  # noqa: E501


        :return: The resource_spec_id of this WorkspaceCreateAPIInput.  # noqa: E501
        :rtype: int
        """
        return self._resource_spec_id

    @resource_spec_id.setter
    def resource_spec_id(self, resource_spec_id):
        """Sets the resource_spec_id of this WorkspaceCreateAPIInput.


        :param resource_spec_id: The resource_spec_id of this WorkspaceCreateAPIInput.  # noqa: E501
        :type resource_spec_id: int
        """

        self._resource_spec_id = resource_spec_id

    @property
    def service_account_name(self):
        """Gets the service_account_name of this WorkspaceCreateAPIInput.  # noqa: E501


        :return: The service_account_name of this WorkspaceCreateAPIInput.  # noqa: E501
        :rtype: str
        """
        return self._service_account_name

    @service_account_name.setter
    def service_account_name(self, service_account_name):
        """Sets the service_account_name of this WorkspaceCreateAPIInput.


        :param service_account_name: The service_account_name of this WorkspaceCreateAPIInput.  # noqa: E501
        :type service_account_name: str
        """

        self._service_account_name = service_account_name

    @property
    def start_command(self):
        """Gets the start_command of this WorkspaceCreateAPIInput.  # noqa: E501


        :return: The start_command of this WorkspaceCreateAPIInput.  # noqa: E501
        :rtype: str
        """
        return self._start_command

    @start_command.setter
    def start_command(self, start_command):
        """Sets the start_command of this WorkspaceCreateAPIInput.


        :param start_command: The start_command of this WorkspaceCreateAPIInput.  # noqa: E501
        :type start_command: str
        """

        self._start_command = start_command

    @property
    def volumes(self):
        """Gets the volumes of this WorkspaceCreateAPIInput.  # noqa: E501


        :return: The volumes of this WorkspaceCreateAPIInput.  # noqa: E501
        :rtype: OrmVolumeMountRequests
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        """Sets the volumes of this WorkspaceCreateAPIInput.


        :param volumes: The volumes of this WorkspaceCreateAPIInput.  # noqa: E501
        :type volumes: OrmVolumeMountRequests
        """
        if self.local_vars_configuration.client_side_validation and volumes is None:  # noqa: E501
            raise ValueError("Invalid value for `volumes`, must not be `None`")  # noqa: E501

        self._volumes = volumes

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
        if not isinstance(other, WorkspaceCreateAPIInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WorkspaceCreateAPIInput):
            return True

        return self.to_dict() != other.to_dict()
