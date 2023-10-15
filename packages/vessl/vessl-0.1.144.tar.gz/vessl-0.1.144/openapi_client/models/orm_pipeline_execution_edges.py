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


class OrmPipelineExecutionEdges(object):
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
        'pipeline': 'OrmPipeline',
        'source_trigger': 'OrmPipelineTrigger',
        'spec': 'OrmPipelineSpec',
        'step_executions': 'list[OrmPipelineStepExecution]',
        'triggered_pipeline_step_execution': 'OrmPipelineStepExecution',
        'triggered_user': 'OrmUser'
    }

    attribute_map = {
        'pipeline': 'pipeline',
        'source_trigger': 'source_trigger',
        'spec': 'spec',
        'step_executions': 'step_executions',
        'triggered_pipeline_step_execution': 'triggered_pipeline_step_execution',
        'triggered_user': 'triggered_user'
    }

    def __init__(self, pipeline=None, source_trigger=None, spec=None, step_executions=None, triggered_pipeline_step_execution=None, triggered_user=None, local_vars_configuration=None):  # noqa: E501
        """OrmPipelineExecutionEdges - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._pipeline = None
        self._source_trigger = None
        self._spec = None
        self._step_executions = None
        self._triggered_pipeline_step_execution = None
        self._triggered_user = None
        self.discriminator = None

        if pipeline is not None:
            self.pipeline = pipeline
        if source_trigger is not None:
            self.source_trigger = source_trigger
        if spec is not None:
            self.spec = spec
        if step_executions is not None:
            self.step_executions = step_executions
        if triggered_pipeline_step_execution is not None:
            self.triggered_pipeline_step_execution = triggered_pipeline_step_execution
        if triggered_user is not None:
            self.triggered_user = triggered_user

    @property
    def pipeline(self):
        """Gets the pipeline of this OrmPipelineExecutionEdges.  # noqa: E501


        :return: The pipeline of this OrmPipelineExecutionEdges.  # noqa: E501
        :rtype: OrmPipeline
        """
        return self._pipeline

    @pipeline.setter
    def pipeline(self, pipeline):
        """Sets the pipeline of this OrmPipelineExecutionEdges.


        :param pipeline: The pipeline of this OrmPipelineExecutionEdges.  # noqa: E501
        :type pipeline: OrmPipeline
        """

        self._pipeline = pipeline

    @property
    def source_trigger(self):
        """Gets the source_trigger of this OrmPipelineExecutionEdges.  # noqa: E501


        :return: The source_trigger of this OrmPipelineExecutionEdges.  # noqa: E501
        :rtype: OrmPipelineTrigger
        """
        return self._source_trigger

    @source_trigger.setter
    def source_trigger(self, source_trigger):
        """Sets the source_trigger of this OrmPipelineExecutionEdges.


        :param source_trigger: The source_trigger of this OrmPipelineExecutionEdges.  # noqa: E501
        :type source_trigger: OrmPipelineTrigger
        """

        self._source_trigger = source_trigger

    @property
    def spec(self):
        """Gets the spec of this OrmPipelineExecutionEdges.  # noqa: E501


        :return: The spec of this OrmPipelineExecutionEdges.  # noqa: E501
        :rtype: OrmPipelineSpec
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """Sets the spec of this OrmPipelineExecutionEdges.


        :param spec: The spec of this OrmPipelineExecutionEdges.  # noqa: E501
        :type spec: OrmPipelineSpec
        """

        self._spec = spec

    @property
    def step_executions(self):
        """Gets the step_executions of this OrmPipelineExecutionEdges.  # noqa: E501


        :return: The step_executions of this OrmPipelineExecutionEdges.  # noqa: E501
        :rtype: list[OrmPipelineStepExecution]
        """
        return self._step_executions

    @step_executions.setter
    def step_executions(self, step_executions):
        """Sets the step_executions of this OrmPipelineExecutionEdges.


        :param step_executions: The step_executions of this OrmPipelineExecutionEdges.  # noqa: E501
        :type step_executions: list[OrmPipelineStepExecution]
        """

        self._step_executions = step_executions

    @property
    def triggered_pipeline_step_execution(self):
        """Gets the triggered_pipeline_step_execution of this OrmPipelineExecutionEdges.  # noqa: E501


        :return: The triggered_pipeline_step_execution of this OrmPipelineExecutionEdges.  # noqa: E501
        :rtype: OrmPipelineStepExecution
        """
        return self._triggered_pipeline_step_execution

    @triggered_pipeline_step_execution.setter
    def triggered_pipeline_step_execution(self, triggered_pipeline_step_execution):
        """Sets the triggered_pipeline_step_execution of this OrmPipelineExecutionEdges.


        :param triggered_pipeline_step_execution: The triggered_pipeline_step_execution of this OrmPipelineExecutionEdges.  # noqa: E501
        :type triggered_pipeline_step_execution: OrmPipelineStepExecution
        """

        self._triggered_pipeline_step_execution = triggered_pipeline_step_execution

    @property
    def triggered_user(self):
        """Gets the triggered_user of this OrmPipelineExecutionEdges.  # noqa: E501


        :return: The triggered_user of this OrmPipelineExecutionEdges.  # noqa: E501
        :rtype: OrmUser
        """
        return self._triggered_user

    @triggered_user.setter
    def triggered_user(self, triggered_user):
        """Sets the triggered_user of this OrmPipelineExecutionEdges.


        :param triggered_user: The triggered_user of this OrmPipelineExecutionEdges.  # noqa: E501
        :type triggered_user: OrmUser
        """

        self._triggered_user = triggered_user

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
        if not isinstance(other, OrmPipelineExecutionEdges):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrmPipelineExecutionEdges):
            return True

        return self.to_dict() != other.to_dict()
