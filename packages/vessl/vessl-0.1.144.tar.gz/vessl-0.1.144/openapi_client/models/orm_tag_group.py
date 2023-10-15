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


class OrmTagGroup(object):
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
        'edges': 'OrmTagGroupEdges',
        'id': 'int',
        'owner_id': 'int',
        'tag_group_organization': 'int',
        'type': 'str',
        'updated_dt': 'datetime'
    }

    attribute_map = {
        'created_dt': 'created_dt',
        'edges': 'edges',
        'id': 'id',
        'owner_id': 'owner_id',
        'tag_group_organization': 'tag_group_organization',
        'type': 'type',
        'updated_dt': 'updated_dt'
    }

    def __init__(self, created_dt=None, edges=None, id=None, owner_id=None, tag_group_organization=None, type=None, updated_dt=None, local_vars_configuration=None):  # noqa: E501
        """OrmTagGroup - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._created_dt = None
        self._edges = None
        self._id = None
        self._owner_id = None
        self._tag_group_organization = None
        self._type = None
        self._updated_dt = None
        self.discriminator = None

        if created_dt is not None:
            self.created_dt = created_dt
        if edges is not None:
            self.edges = edges
        if id is not None:
            self.id = id
        if owner_id is not None:
            self.owner_id = owner_id
        if tag_group_organization is not None:
            self.tag_group_organization = tag_group_organization
        if type is not None:
            self.type = type
        if updated_dt is not None:
            self.updated_dt = updated_dt

    @property
    def created_dt(self):
        """Gets the created_dt of this OrmTagGroup.  # noqa: E501


        :return: The created_dt of this OrmTagGroup.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this OrmTagGroup.


        :param created_dt: The created_dt of this OrmTagGroup.  # noqa: E501
        :type created_dt: datetime
        """

        self._created_dt = created_dt

    @property
    def edges(self):
        """Gets the edges of this OrmTagGroup.  # noqa: E501


        :return: The edges of this OrmTagGroup.  # noqa: E501
        :rtype: OrmTagGroupEdges
        """
        return self._edges

    @edges.setter
    def edges(self, edges):
        """Sets the edges of this OrmTagGroup.


        :param edges: The edges of this OrmTagGroup.  # noqa: E501
        :type edges: OrmTagGroupEdges
        """

        self._edges = edges

    @property
    def id(self):
        """Gets the id of this OrmTagGroup.  # noqa: E501


        :return: The id of this OrmTagGroup.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OrmTagGroup.


        :param id: The id of this OrmTagGroup.  # noqa: E501
        :type id: int
        """

        self._id = id

    @property
    def owner_id(self):
        """Gets the owner_id of this OrmTagGroup.  # noqa: E501


        :return: The owner_id of this OrmTagGroup.  # noqa: E501
        :rtype: int
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this OrmTagGroup.


        :param owner_id: The owner_id of this OrmTagGroup.  # noqa: E501
        :type owner_id: int
        """

        self._owner_id = owner_id

    @property
    def tag_group_organization(self):
        """Gets the tag_group_organization of this OrmTagGroup.  # noqa: E501


        :return: The tag_group_organization of this OrmTagGroup.  # noqa: E501
        :rtype: int
        """
        return self._tag_group_organization

    @tag_group_organization.setter
    def tag_group_organization(self, tag_group_organization):
        """Sets the tag_group_organization of this OrmTagGroup.


        :param tag_group_organization: The tag_group_organization of this OrmTagGroup.  # noqa: E501
        :type tag_group_organization: int
        """

        self._tag_group_organization = tag_group_organization

    @property
    def type(self):
        """Gets the type of this OrmTagGroup.  # noqa: E501


        :return: The type of this OrmTagGroup.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OrmTagGroup.


        :param type: The type of this OrmTagGroup.  # noqa: E501
        :type type: str
        """

        self._type = type

    @property
    def updated_dt(self):
        """Gets the updated_dt of this OrmTagGroup.  # noqa: E501


        :return: The updated_dt of this OrmTagGroup.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_dt

    @updated_dt.setter
    def updated_dt(self, updated_dt):
        """Sets the updated_dt of this OrmTagGroup.


        :param updated_dt: The updated_dt of this OrmTagGroup.  # noqa: E501
        :type updated_dt: datetime
        """

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
        if not isinstance(other, OrmTagGroup):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrmTagGroup):
            return True

        return self.to_dict() != other.to_dict()
