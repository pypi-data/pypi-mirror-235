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


class OrmWorkspace(object):
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
        'edges': 'OrmWorkspaceEdges',
        'end_dt': 'datetime',
        'id': 'int',
        'idle_shutdown_minutes': 'int',
        'immutable_slug': 'str',
        'init_script': 'str',
        'last_backup_succeeded': 'bool',
        'max_running_hours': 'int',
        'name': 'str',
        'ports': 'dict[str, object]',
        'updated_dt': 'datetime',
        'workspace_backup_volume': 'int',
        'workspace_created_by': 'int',
        'workspace_organization': 'int'
    }

    attribute_map = {
        'created_dt': 'created_dt',
        'edges': 'edges',
        'end_dt': 'end_dt',
        'id': 'id',
        'idle_shutdown_minutes': 'idle_shutdown_minutes',
        'immutable_slug': 'immutable_slug',
        'init_script': 'init_script',
        'last_backup_succeeded': 'last_backup_succeeded',
        'max_running_hours': 'max_running_hours',
        'name': 'name',
        'ports': 'ports',
        'updated_dt': 'updated_dt',
        'workspace_backup_volume': 'workspace_backup_volume',
        'workspace_created_by': 'workspace_created_by',
        'workspace_organization': 'workspace_organization'
    }

    def __init__(self, created_dt=None, edges=None, end_dt=None, id=None, idle_shutdown_minutes=None, immutable_slug=None, init_script=None, last_backup_succeeded=None, max_running_hours=None, name=None, ports=None, updated_dt=None, workspace_backup_volume=None, workspace_created_by=None, workspace_organization=None, local_vars_configuration=None):  # noqa: E501
        """OrmWorkspace - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._created_dt = None
        self._edges = None
        self._end_dt = None
        self._id = None
        self._idle_shutdown_minutes = None
        self._immutable_slug = None
        self._init_script = None
        self._last_backup_succeeded = None
        self._max_running_hours = None
        self._name = None
        self._ports = None
        self._updated_dt = None
        self._workspace_backup_volume = None
        self._workspace_created_by = None
        self._workspace_organization = None
        self.discriminator = None

        if created_dt is not None:
            self.created_dt = created_dt
        if edges is not None:
            self.edges = edges
        self.end_dt = end_dt
        if id is not None:
            self.id = id
        if idle_shutdown_minutes is not None:
            self.idle_shutdown_minutes = idle_shutdown_minutes
        if immutable_slug is not None:
            self.immutable_slug = immutable_slug
        self.init_script = init_script
        self.last_backup_succeeded = last_backup_succeeded
        if max_running_hours is not None:
            self.max_running_hours = max_running_hours
        if name is not None:
            self.name = name
        if ports is not None:
            self.ports = ports
        if updated_dt is not None:
            self.updated_dt = updated_dt
        if workspace_backup_volume is not None:
            self.workspace_backup_volume = workspace_backup_volume
        if workspace_created_by is not None:
            self.workspace_created_by = workspace_created_by
        if workspace_organization is not None:
            self.workspace_organization = workspace_organization

    @property
    def created_dt(self):
        """Gets the created_dt of this OrmWorkspace.  # noqa: E501


        :return: The created_dt of this OrmWorkspace.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this OrmWorkspace.


        :param created_dt: The created_dt of this OrmWorkspace.  # noqa: E501
        :type created_dt: datetime
        """

        self._created_dt = created_dt

    @property
    def edges(self):
        """Gets the edges of this OrmWorkspace.  # noqa: E501


        :return: The edges of this OrmWorkspace.  # noqa: E501
        :rtype: OrmWorkspaceEdges
        """
        return self._edges

    @edges.setter
    def edges(self, edges):
        """Sets the edges of this OrmWorkspace.


        :param edges: The edges of this OrmWorkspace.  # noqa: E501
        :type edges: OrmWorkspaceEdges
        """

        self._edges = edges

    @property
    def end_dt(self):
        """Gets the end_dt of this OrmWorkspace.  # noqa: E501


        :return: The end_dt of this OrmWorkspace.  # noqa: E501
        :rtype: datetime
        """
        return self._end_dt

    @end_dt.setter
    def end_dt(self, end_dt):
        """Sets the end_dt of this OrmWorkspace.


        :param end_dt: The end_dt of this OrmWorkspace.  # noqa: E501
        :type end_dt: datetime
        """

        self._end_dt = end_dt

    @property
    def id(self):
        """Gets the id of this OrmWorkspace.  # noqa: E501


        :return: The id of this OrmWorkspace.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OrmWorkspace.


        :param id: The id of this OrmWorkspace.  # noqa: E501
        :type id: int
        """

        self._id = id

    @property
    def idle_shutdown_minutes(self):
        """Gets the idle_shutdown_minutes of this OrmWorkspace.  # noqa: E501


        :return: The idle_shutdown_minutes of this OrmWorkspace.  # noqa: E501
        :rtype: int
        """
        return self._idle_shutdown_minutes

    @idle_shutdown_minutes.setter
    def idle_shutdown_minutes(self, idle_shutdown_minutes):
        """Sets the idle_shutdown_minutes of this OrmWorkspace.


        :param idle_shutdown_minutes: The idle_shutdown_minutes of this OrmWorkspace.  # noqa: E501
        :type idle_shutdown_minutes: int
        """

        self._idle_shutdown_minutes = idle_shutdown_minutes

    @property
    def immutable_slug(self):
        """Gets the immutable_slug of this OrmWorkspace.  # noqa: E501


        :return: The immutable_slug of this OrmWorkspace.  # noqa: E501
        :rtype: str
        """
        return self._immutable_slug

    @immutable_slug.setter
    def immutable_slug(self, immutable_slug):
        """Sets the immutable_slug of this OrmWorkspace.


        :param immutable_slug: The immutable_slug of this OrmWorkspace.  # noqa: E501
        :type immutable_slug: str
        """

        self._immutable_slug = immutable_slug

    @property
    def init_script(self):
        """Gets the init_script of this OrmWorkspace.  # noqa: E501


        :return: The init_script of this OrmWorkspace.  # noqa: E501
        :rtype: str
        """
        return self._init_script

    @init_script.setter
    def init_script(self, init_script):
        """Sets the init_script of this OrmWorkspace.


        :param init_script: The init_script of this OrmWorkspace.  # noqa: E501
        :type init_script: str
        """

        self._init_script = init_script

    @property
    def last_backup_succeeded(self):
        """Gets the last_backup_succeeded of this OrmWorkspace.  # noqa: E501


        :return: The last_backup_succeeded of this OrmWorkspace.  # noqa: E501
        :rtype: bool
        """
        return self._last_backup_succeeded

    @last_backup_succeeded.setter
    def last_backup_succeeded(self, last_backup_succeeded):
        """Sets the last_backup_succeeded of this OrmWorkspace.


        :param last_backup_succeeded: The last_backup_succeeded of this OrmWorkspace.  # noqa: E501
        :type last_backup_succeeded: bool
        """

        self._last_backup_succeeded = last_backup_succeeded

    @property
    def max_running_hours(self):
        """Gets the max_running_hours of this OrmWorkspace.  # noqa: E501


        :return: The max_running_hours of this OrmWorkspace.  # noqa: E501
        :rtype: int
        """
        return self._max_running_hours

    @max_running_hours.setter
    def max_running_hours(self, max_running_hours):
        """Sets the max_running_hours of this OrmWorkspace.


        :param max_running_hours: The max_running_hours of this OrmWorkspace.  # noqa: E501
        :type max_running_hours: int
        """

        self._max_running_hours = max_running_hours

    @property
    def name(self):
        """Gets the name of this OrmWorkspace.  # noqa: E501


        :return: The name of this OrmWorkspace.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OrmWorkspace.


        :param name: The name of this OrmWorkspace.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def ports(self):
        """Gets the ports of this OrmWorkspace.  # noqa: E501


        :return: The ports of this OrmWorkspace.  # noqa: E501
        :rtype: dict[str, object]
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """Sets the ports of this OrmWorkspace.


        :param ports: The ports of this OrmWorkspace.  # noqa: E501
        :type ports: dict[str, object]
        """

        self._ports = ports

    @property
    def updated_dt(self):
        """Gets the updated_dt of this OrmWorkspace.  # noqa: E501


        :return: The updated_dt of this OrmWorkspace.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_dt

    @updated_dt.setter
    def updated_dt(self, updated_dt):
        """Sets the updated_dt of this OrmWorkspace.


        :param updated_dt: The updated_dt of this OrmWorkspace.  # noqa: E501
        :type updated_dt: datetime
        """

        self._updated_dt = updated_dt

    @property
    def workspace_backup_volume(self):
        """Gets the workspace_backup_volume of this OrmWorkspace.  # noqa: E501


        :return: The workspace_backup_volume of this OrmWorkspace.  # noqa: E501
        :rtype: int
        """
        return self._workspace_backup_volume

    @workspace_backup_volume.setter
    def workspace_backup_volume(self, workspace_backup_volume):
        """Sets the workspace_backup_volume of this OrmWorkspace.


        :param workspace_backup_volume: The workspace_backup_volume of this OrmWorkspace.  # noqa: E501
        :type workspace_backup_volume: int
        """

        self._workspace_backup_volume = workspace_backup_volume

    @property
    def workspace_created_by(self):
        """Gets the workspace_created_by of this OrmWorkspace.  # noqa: E501


        :return: The workspace_created_by of this OrmWorkspace.  # noqa: E501
        :rtype: int
        """
        return self._workspace_created_by

    @workspace_created_by.setter
    def workspace_created_by(self, workspace_created_by):
        """Sets the workspace_created_by of this OrmWorkspace.


        :param workspace_created_by: The workspace_created_by of this OrmWorkspace.  # noqa: E501
        :type workspace_created_by: int
        """

        self._workspace_created_by = workspace_created_by

    @property
    def workspace_organization(self):
        """Gets the workspace_organization of this OrmWorkspace.  # noqa: E501


        :return: The workspace_organization of this OrmWorkspace.  # noqa: E501
        :rtype: int
        """
        return self._workspace_organization

    @workspace_organization.setter
    def workspace_organization(self, workspace_organization):
        """Sets the workspace_organization of this OrmWorkspace.


        :param workspace_organization: The workspace_organization of this OrmWorkspace.  # noqa: E501
        :type workspace_organization: int
        """

        self._workspace_organization = workspace_organization

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
        if not isinstance(other, OrmWorkspace):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrmWorkspace):
            return True

        return self.to_dict() != other.to_dict()
