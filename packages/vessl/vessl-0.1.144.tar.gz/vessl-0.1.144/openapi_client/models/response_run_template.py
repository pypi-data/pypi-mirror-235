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


class ResponseRunTemplate(object):
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
        'description': 'str',
        'files': 'dict[str, list[ResponseRunTemplateFile]]',
        'id': 'int',
        'tags': 'list[str]',
        'title': 'str',
        'yaml_spec': 'str'
    }

    attribute_map = {
        'description': 'description',
        'files': 'files',
        'id': 'id',
        'tags': 'tags',
        'title': 'title',
        'yaml_spec': 'yaml_spec'
    }

    def __init__(self, description=None, files=None, id=None, tags=None, title=None, yaml_spec=None, local_vars_configuration=None):  # noqa: E501
        """ResponseRunTemplate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._description = None
        self._files = None
        self._id = None
        self._tags = None
        self._title = None
        self._yaml_spec = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if files is not None:
            self.files = files
        if id is not None:
            self.id = id
        if tags is not None:
            self.tags = tags
        if title is not None:
            self.title = title
        if yaml_spec is not None:
            self.yaml_spec = yaml_spec

    @property
    def description(self):
        """Gets the description of this ResponseRunTemplate.  # noqa: E501


        :return: The description of this ResponseRunTemplate.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ResponseRunTemplate.


        :param description: The description of this ResponseRunTemplate.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def files(self):
        """Gets the files of this ResponseRunTemplate.  # noqa: E501


        :return: The files of this ResponseRunTemplate.  # noqa: E501
        :rtype: dict[str, list[ResponseRunTemplateFile]]
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this ResponseRunTemplate.


        :param files: The files of this ResponseRunTemplate.  # noqa: E501
        :type files: dict[str, list[ResponseRunTemplateFile]]
        """

        self._files = files

    @property
    def id(self):
        """Gets the id of this ResponseRunTemplate.  # noqa: E501


        :return: The id of this ResponseRunTemplate.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ResponseRunTemplate.


        :param id: The id of this ResponseRunTemplate.  # noqa: E501
        :type id: int
        """

        self._id = id

    @property
    def tags(self):
        """Gets the tags of this ResponseRunTemplate.  # noqa: E501


        :return: The tags of this ResponseRunTemplate.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ResponseRunTemplate.


        :param tags: The tags of this ResponseRunTemplate.  # noqa: E501
        :type tags: list[str]
        """

        self._tags = tags

    @property
    def title(self):
        """Gets the title of this ResponseRunTemplate.  # noqa: E501


        :return: The title of this ResponseRunTemplate.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ResponseRunTemplate.


        :param title: The title of this ResponseRunTemplate.  # noqa: E501
        :type title: str
        """

        self._title = title

    @property
    def yaml_spec(self):
        """Gets the yaml_spec of this ResponseRunTemplate.  # noqa: E501


        :return: The yaml_spec of this ResponseRunTemplate.  # noqa: E501
        :rtype: str
        """
        return self._yaml_spec

    @yaml_spec.setter
    def yaml_spec(self, yaml_spec):
        """Sets the yaml_spec of this ResponseRunTemplate.


        :param yaml_spec: The yaml_spec of this ResponseRunTemplate.  # noqa: E501
        :type yaml_spec: str
        """

        self._yaml_spec = yaml_spec

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
        if not isinstance(other, ResponseRunTemplate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResponseRunTemplate):
            return True

        return self.to_dict() != other.to_dict()
