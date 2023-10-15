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


class OrmTagEdges(object):
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
        'experiments': 'list[OrmExperiment]',
        'models': 'list[OrmModel]',
        'run_executions': 'list[OrmRunExecution]',
        'tag_group': 'OrmTagGroup'
    }

    attribute_map = {
        'experiments': 'experiments',
        'models': 'models',
        'run_executions': 'run_executions',
        'tag_group': 'tag_group'
    }

    def __init__(self, experiments=None, models=None, run_executions=None, tag_group=None, local_vars_configuration=None):  # noqa: E501
        """OrmTagEdges - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._experiments = None
        self._models = None
        self._run_executions = None
        self._tag_group = None
        self.discriminator = None

        if experiments is not None:
            self.experiments = experiments
        if models is not None:
            self.models = models
        if run_executions is not None:
            self.run_executions = run_executions
        if tag_group is not None:
            self.tag_group = tag_group

    @property
    def experiments(self):
        """Gets the experiments of this OrmTagEdges.  # noqa: E501


        :return: The experiments of this OrmTagEdges.  # noqa: E501
        :rtype: list[OrmExperiment]
        """
        return self._experiments

    @experiments.setter
    def experiments(self, experiments):
        """Sets the experiments of this OrmTagEdges.


        :param experiments: The experiments of this OrmTagEdges.  # noqa: E501
        :type experiments: list[OrmExperiment]
        """

        self._experiments = experiments

    @property
    def models(self):
        """Gets the models of this OrmTagEdges.  # noqa: E501


        :return: The models of this OrmTagEdges.  # noqa: E501
        :rtype: list[OrmModel]
        """
        return self._models

    @models.setter
    def models(self, models):
        """Sets the models of this OrmTagEdges.


        :param models: The models of this OrmTagEdges.  # noqa: E501
        :type models: list[OrmModel]
        """

        self._models = models

    @property
    def run_executions(self):
        """Gets the run_executions of this OrmTagEdges.  # noqa: E501


        :return: The run_executions of this OrmTagEdges.  # noqa: E501
        :rtype: list[OrmRunExecution]
        """
        return self._run_executions

    @run_executions.setter
    def run_executions(self, run_executions):
        """Sets the run_executions of this OrmTagEdges.


        :param run_executions: The run_executions of this OrmTagEdges.  # noqa: E501
        :type run_executions: list[OrmRunExecution]
        """

        self._run_executions = run_executions

    @property
    def tag_group(self):
        """Gets the tag_group of this OrmTagEdges.  # noqa: E501


        :return: The tag_group of this OrmTagEdges.  # noqa: E501
        :rtype: OrmTagGroup
        """
        return self._tag_group

    @tag_group.setter
    def tag_group(self, tag_group):
        """Sets the tag_group of this OrmTagEdges.


        :param tag_group: The tag_group of this OrmTagEdges.  # noqa: E501
        :type tag_group: OrmTagGroup
        """

        self._tag_group = tag_group

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
        if not isinstance(other, OrmTagEdges):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrmTagEdges):
            return True

        return self.to_dict() != other.to_dict()
