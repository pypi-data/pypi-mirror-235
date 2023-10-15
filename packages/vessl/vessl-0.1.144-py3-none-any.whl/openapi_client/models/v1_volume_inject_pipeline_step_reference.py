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


class V1VolumeInjectPipelineStepReference(object):
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
        'step_key': 'str',
        'volume_claim_name': 'str'
    }

    attribute_map = {
        'step_key': 'step_key',
        'volume_claim_name': 'volume_claim_name'
    }

    def __init__(self, step_key=None, volume_claim_name=None, local_vars_configuration=None):  # noqa: E501
        """V1VolumeInjectPipelineStepReference - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._step_key = None
        self._volume_claim_name = None
        self.discriminator = None

        self.step_key = step_key
        self.volume_claim_name = volume_claim_name

    @property
    def step_key(self):
        """Gets the step_key of this V1VolumeInjectPipelineStepReference.  # noqa: E501


        :return: The step_key of this V1VolumeInjectPipelineStepReference.  # noqa: E501
        :rtype: str
        """
        return self._step_key

    @step_key.setter
    def step_key(self, step_key):
        """Sets the step_key of this V1VolumeInjectPipelineStepReference.


        :param step_key: The step_key of this V1VolumeInjectPipelineStepReference.  # noqa: E501
        :type step_key: str
        """
        if self.local_vars_configuration.client_side_validation and step_key is None:  # noqa: E501
            raise ValueError("Invalid value for `step_key`, must not be `None`")  # noqa: E501

        self._step_key = step_key

    @property
    def volume_claim_name(self):
        """Gets the volume_claim_name of this V1VolumeInjectPipelineStepReference.  # noqa: E501


        :return: The volume_claim_name of this V1VolumeInjectPipelineStepReference.  # noqa: E501
        :rtype: str
        """
        return self._volume_claim_name

    @volume_claim_name.setter
    def volume_claim_name(self, volume_claim_name):
        """Sets the volume_claim_name of this V1VolumeInjectPipelineStepReference.


        :param volume_claim_name: The volume_claim_name of this V1VolumeInjectPipelineStepReference.  # noqa: E501
        :type volume_claim_name: str
        """
        if self.local_vars_configuration.client_side_validation and volume_claim_name is None:  # noqa: E501
            raise ValueError("Invalid value for `volume_claim_name`, must not be `None`")  # noqa: E501

        self._volume_claim_name = volume_claim_name

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
        if not isinstance(other, V1VolumeInjectPipelineStepReference):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1VolumeInjectPipelineStepReference):
            return True

        return self.to_dict() != other.to_dict()
