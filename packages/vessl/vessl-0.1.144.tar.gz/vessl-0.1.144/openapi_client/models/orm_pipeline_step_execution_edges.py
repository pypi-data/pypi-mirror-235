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


class OrmPipelineStepExecutionEdges(object):
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
        'access_token': 'OrmAccessToken',
        'execution': 'OrmPipelineExecution',
        'judged_user': 'OrmUser',
        'run_execution': 'OrmRunExecution',
        'step_spec': 'OrmPipelineStepSpec',
        'triggering_pipeline_execution': 'OrmPipelineExecution',
        'workload': 'OrmWorkload'
    }

    attribute_map = {
        'access_token': 'access_token',
        'execution': 'execution',
        'judged_user': 'judged_user',
        'run_execution': 'run_execution',
        'step_spec': 'step_spec',
        'triggering_pipeline_execution': 'triggering_pipeline_execution',
        'workload': 'workload'
    }

    def __init__(self, access_token=None, execution=None, judged_user=None, run_execution=None, step_spec=None, triggering_pipeline_execution=None, workload=None, local_vars_configuration=None):  # noqa: E501
        """OrmPipelineStepExecutionEdges - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._access_token = None
        self._execution = None
        self._judged_user = None
        self._run_execution = None
        self._step_spec = None
        self._triggering_pipeline_execution = None
        self._workload = None
        self.discriminator = None

        if access_token is not None:
            self.access_token = access_token
        if execution is not None:
            self.execution = execution
        if judged_user is not None:
            self.judged_user = judged_user
        if run_execution is not None:
            self.run_execution = run_execution
        if step_spec is not None:
            self.step_spec = step_spec
        if triggering_pipeline_execution is not None:
            self.triggering_pipeline_execution = triggering_pipeline_execution
        if workload is not None:
            self.workload = workload

    @property
    def access_token(self):
        """Gets the access_token of this OrmPipelineStepExecutionEdges.  # noqa: E501


        :return: The access_token of this OrmPipelineStepExecutionEdges.  # noqa: E501
        :rtype: OrmAccessToken
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this OrmPipelineStepExecutionEdges.


        :param access_token: The access_token of this OrmPipelineStepExecutionEdges.  # noqa: E501
        :type access_token: OrmAccessToken
        """

        self._access_token = access_token

    @property
    def execution(self):
        """Gets the execution of this OrmPipelineStepExecutionEdges.  # noqa: E501


        :return: The execution of this OrmPipelineStepExecutionEdges.  # noqa: E501
        :rtype: OrmPipelineExecution
        """
        return self._execution

    @execution.setter
    def execution(self, execution):
        """Sets the execution of this OrmPipelineStepExecutionEdges.


        :param execution: The execution of this OrmPipelineStepExecutionEdges.  # noqa: E501
        :type execution: OrmPipelineExecution
        """

        self._execution = execution

    @property
    def judged_user(self):
        """Gets the judged_user of this OrmPipelineStepExecutionEdges.  # noqa: E501


        :return: The judged_user of this OrmPipelineStepExecutionEdges.  # noqa: E501
        :rtype: OrmUser
        """
        return self._judged_user

    @judged_user.setter
    def judged_user(self, judged_user):
        """Sets the judged_user of this OrmPipelineStepExecutionEdges.


        :param judged_user: The judged_user of this OrmPipelineStepExecutionEdges.  # noqa: E501
        :type judged_user: OrmUser
        """

        self._judged_user = judged_user

    @property
    def run_execution(self):
        """Gets the run_execution of this OrmPipelineStepExecutionEdges.  # noqa: E501


        :return: The run_execution of this OrmPipelineStepExecutionEdges.  # noqa: E501
        :rtype: OrmRunExecution
        """
        return self._run_execution

    @run_execution.setter
    def run_execution(self, run_execution):
        """Sets the run_execution of this OrmPipelineStepExecutionEdges.


        :param run_execution: The run_execution of this OrmPipelineStepExecutionEdges.  # noqa: E501
        :type run_execution: OrmRunExecution
        """

        self._run_execution = run_execution

    @property
    def step_spec(self):
        """Gets the step_spec of this OrmPipelineStepExecutionEdges.  # noqa: E501


        :return: The step_spec of this OrmPipelineStepExecutionEdges.  # noqa: E501
        :rtype: OrmPipelineStepSpec
        """
        return self._step_spec

    @step_spec.setter
    def step_spec(self, step_spec):
        """Sets the step_spec of this OrmPipelineStepExecutionEdges.


        :param step_spec: The step_spec of this OrmPipelineStepExecutionEdges.  # noqa: E501
        :type step_spec: OrmPipelineStepSpec
        """

        self._step_spec = step_spec

    @property
    def triggering_pipeline_execution(self):
        """Gets the triggering_pipeline_execution of this OrmPipelineStepExecutionEdges.  # noqa: E501


        :return: The triggering_pipeline_execution of this OrmPipelineStepExecutionEdges.  # noqa: E501
        :rtype: OrmPipelineExecution
        """
        return self._triggering_pipeline_execution

    @triggering_pipeline_execution.setter
    def triggering_pipeline_execution(self, triggering_pipeline_execution):
        """Sets the triggering_pipeline_execution of this OrmPipelineStepExecutionEdges.


        :param triggering_pipeline_execution: The triggering_pipeline_execution of this OrmPipelineStepExecutionEdges.  # noqa: E501
        :type triggering_pipeline_execution: OrmPipelineExecution
        """

        self._triggering_pipeline_execution = triggering_pipeline_execution

    @property
    def workload(self):
        """Gets the workload of this OrmPipelineStepExecutionEdges.  # noqa: E501


        :return: The workload of this OrmPipelineStepExecutionEdges.  # noqa: E501
        :rtype: OrmWorkload
        """
        return self._workload

    @workload.setter
    def workload(self, workload):
        """Sets the workload of this OrmPipelineStepExecutionEdges.


        :param workload: The workload of this OrmPipelineStepExecutionEdges.  # noqa: E501
        :type workload: OrmWorkload
        """

        self._workload = workload

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
        if not isinstance(other, OrmPipelineStepExecutionEdges):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrmPipelineStepExecutionEdges):
            return True

        return self.to_dict() != other.to_dict()
