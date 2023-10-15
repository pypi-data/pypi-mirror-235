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


class OrmProjectDashboardChartEdges(object):
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
        'experiment_fields': 'list[OrmProjectExperimentField]',
        'section': 'OrmProjectDashboardChartSection'
    }

    attribute_map = {
        'experiment_fields': 'experiment_fields',
        'section': 'section'
    }

    def __init__(self, experiment_fields=None, section=None, local_vars_configuration=None):  # noqa: E501
        """OrmProjectDashboardChartEdges - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._experiment_fields = None
        self._section = None
        self.discriminator = None

        if experiment_fields is not None:
            self.experiment_fields = experiment_fields
        if section is not None:
            self.section = section

    @property
    def experiment_fields(self):
        """Gets the experiment_fields of this OrmProjectDashboardChartEdges.  # noqa: E501


        :return: The experiment_fields of this OrmProjectDashboardChartEdges.  # noqa: E501
        :rtype: list[OrmProjectExperimentField]
        """
        return self._experiment_fields

    @experiment_fields.setter
    def experiment_fields(self, experiment_fields):
        """Sets the experiment_fields of this OrmProjectDashboardChartEdges.


        :param experiment_fields: The experiment_fields of this OrmProjectDashboardChartEdges.  # noqa: E501
        :type experiment_fields: list[OrmProjectExperimentField]
        """

        self._experiment_fields = experiment_fields

    @property
    def section(self):
        """Gets the section of this OrmProjectDashboardChartEdges.  # noqa: E501


        :return: The section of this OrmProjectDashboardChartEdges.  # noqa: E501
        :rtype: OrmProjectDashboardChartSection
        """
        return self._section

    @section.setter
    def section(self, section):
        """Sets the section of this OrmProjectDashboardChartEdges.


        :param section: The section of this OrmProjectDashboardChartEdges.  # noqa: E501
        :type section: OrmProjectDashboardChartSection
        """

        self._section = section

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
        if not isinstance(other, OrmProjectDashboardChartEdges):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrmProjectDashboardChartEdges):
            return True

        return self.to_dict() != other.to_dict()
