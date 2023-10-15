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


class OrmVolumeMountRequestSourceDatasetVersion(object):
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
        'dataset_id': 'int',
        'dataset_name': 'str',
        'dataset_version_hash': 'str'
    }

    attribute_map = {
        'dataset_id': 'dataset_id',
        'dataset_name': 'dataset_name',
        'dataset_version_hash': 'dataset_version_hash'
    }

    def __init__(self, dataset_id=None, dataset_name=None, dataset_version_hash=None, local_vars_configuration=None):  # noqa: E501
        """OrmVolumeMountRequestSourceDatasetVersion - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._dataset_id = None
        self._dataset_name = None
        self._dataset_version_hash = None
        self.discriminator = None

        if dataset_id is not None:
            self.dataset_id = dataset_id
        if dataset_name is not None:
            self.dataset_name = dataset_name
        if dataset_version_hash is not None:
            self.dataset_version_hash = dataset_version_hash

    @property
    def dataset_id(self):
        """Gets the dataset_id of this OrmVolumeMountRequestSourceDatasetVersion.  # noqa: E501


        :return: The dataset_id of this OrmVolumeMountRequestSourceDatasetVersion.  # noqa: E501
        :rtype: int
        """
        return self._dataset_id

    @dataset_id.setter
    def dataset_id(self, dataset_id):
        """Sets the dataset_id of this OrmVolumeMountRequestSourceDatasetVersion.


        :param dataset_id: The dataset_id of this OrmVolumeMountRequestSourceDatasetVersion.  # noqa: E501
        :type dataset_id: int
        """

        self._dataset_id = dataset_id

    @property
    def dataset_name(self):
        """Gets the dataset_name of this OrmVolumeMountRequestSourceDatasetVersion.  # noqa: E501


        :return: The dataset_name of this OrmVolumeMountRequestSourceDatasetVersion.  # noqa: E501
        :rtype: str
        """
        return self._dataset_name

    @dataset_name.setter
    def dataset_name(self, dataset_name):
        """Sets the dataset_name of this OrmVolumeMountRequestSourceDatasetVersion.


        :param dataset_name: The dataset_name of this OrmVolumeMountRequestSourceDatasetVersion.  # noqa: E501
        :type dataset_name: str
        """

        self._dataset_name = dataset_name

    @property
    def dataset_version_hash(self):
        """Gets the dataset_version_hash of this OrmVolumeMountRequestSourceDatasetVersion.  # noqa: E501


        :return: The dataset_version_hash of this OrmVolumeMountRequestSourceDatasetVersion.  # noqa: E501
        :rtype: str
        """
        return self._dataset_version_hash

    @dataset_version_hash.setter
    def dataset_version_hash(self, dataset_version_hash):
        """Sets the dataset_version_hash of this OrmVolumeMountRequestSourceDatasetVersion.


        :param dataset_version_hash: The dataset_version_hash of this OrmVolumeMountRequestSourceDatasetVersion.  # noqa: E501
        :type dataset_version_hash: str
        """

        self._dataset_version_hash = dataset_version_hash

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
        if not isinstance(other, OrmVolumeMountRequestSourceDatasetVersion):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrmVolumeMountRequestSourceDatasetVersion):
            return True

        return self.to_dict() != other.to_dict()
