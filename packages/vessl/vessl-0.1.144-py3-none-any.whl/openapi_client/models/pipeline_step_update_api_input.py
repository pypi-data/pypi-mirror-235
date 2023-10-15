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


class PipelineStepUpdateAPIInput(object):
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
        'external_service_spec_input': 'PipelineExternalServiceSpecInput',
        'fail_spec_input': 'object',
        'if_spec_input': 'PipelineIfSpecInput',
        'manual_input_spec_input': 'PipelineManualInputSpecInput',
        'manual_judgment_spec_input': 'PipelineManualJudgmentSpecInput',
        'notification_spec_input': 'PipelineNotificationSpecInput',
        'run_spec_input': 'PipelineRunSpecInput',
        'step_key': 'str',
        'title': 'str',
        'trigger_dispatch_input': 'PipelineTriggerDispatchInput'
    }

    attribute_map = {
        'description': 'description',
        'external_service_spec_input': 'external_service_spec_input',
        'fail_spec_input': 'fail_spec_input',
        'if_spec_input': 'if_spec_input',
        'manual_input_spec_input': 'manual_input_spec_input',
        'manual_judgment_spec_input': 'manual_judgment_spec_input',
        'notification_spec_input': 'notification_spec_input',
        'run_spec_input': 'run_spec_input',
        'step_key': 'step_key',
        'title': 'title',
        'trigger_dispatch_input': 'trigger_dispatch_input'
    }

    def __init__(self, description=None, external_service_spec_input=None, fail_spec_input=None, if_spec_input=None, manual_input_spec_input=None, manual_judgment_spec_input=None, notification_spec_input=None, run_spec_input=None, step_key=None, title=None, trigger_dispatch_input=None, local_vars_configuration=None):  # noqa: E501
        """PipelineStepUpdateAPIInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._description = None
        self._external_service_spec_input = None
        self._fail_spec_input = None
        self._if_spec_input = None
        self._manual_input_spec_input = None
        self._manual_judgment_spec_input = None
        self._notification_spec_input = None
        self._run_spec_input = None
        self._step_key = None
        self._title = None
        self._trigger_dispatch_input = None
        self.discriminator = None

        self.description = description
        if external_service_spec_input is not None:
            self.external_service_spec_input = external_service_spec_input
        if fail_spec_input is not None:
            self.fail_spec_input = fail_spec_input
        if if_spec_input is not None:
            self.if_spec_input = if_spec_input
        if manual_input_spec_input is not None:
            self.manual_input_spec_input = manual_input_spec_input
        if manual_judgment_spec_input is not None:
            self.manual_judgment_spec_input = manual_judgment_spec_input
        if notification_spec_input is not None:
            self.notification_spec_input = notification_spec_input
        if run_spec_input is not None:
            self.run_spec_input = run_spec_input
        self.step_key = step_key
        self.title = title
        if trigger_dispatch_input is not None:
            self.trigger_dispatch_input = trigger_dispatch_input

    @property
    def description(self):
        """Gets the description of this PipelineStepUpdateAPIInput.  # noqa: E501


        :return: The description of this PipelineStepUpdateAPIInput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PipelineStepUpdateAPIInput.


        :param description: The description of this PipelineStepUpdateAPIInput.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def external_service_spec_input(self):
        """Gets the external_service_spec_input of this PipelineStepUpdateAPIInput.  # noqa: E501


        :return: The external_service_spec_input of this PipelineStepUpdateAPIInput.  # noqa: E501
        :rtype: PipelineExternalServiceSpecInput
        """
        return self._external_service_spec_input

    @external_service_spec_input.setter
    def external_service_spec_input(self, external_service_spec_input):
        """Sets the external_service_spec_input of this PipelineStepUpdateAPIInput.


        :param external_service_spec_input: The external_service_spec_input of this PipelineStepUpdateAPIInput.  # noqa: E501
        :type external_service_spec_input: PipelineExternalServiceSpecInput
        """

        self._external_service_spec_input = external_service_spec_input

    @property
    def fail_spec_input(self):
        """Gets the fail_spec_input of this PipelineStepUpdateAPIInput.  # noqa: E501


        :return: The fail_spec_input of this PipelineStepUpdateAPIInput.  # noqa: E501
        :rtype: object
        """
        return self._fail_spec_input

    @fail_spec_input.setter
    def fail_spec_input(self, fail_spec_input):
        """Sets the fail_spec_input of this PipelineStepUpdateAPIInput.


        :param fail_spec_input: The fail_spec_input of this PipelineStepUpdateAPIInput.  # noqa: E501
        :type fail_spec_input: object
        """

        self._fail_spec_input = fail_spec_input

    @property
    def if_spec_input(self):
        """Gets the if_spec_input of this PipelineStepUpdateAPIInput.  # noqa: E501


        :return: The if_spec_input of this PipelineStepUpdateAPIInput.  # noqa: E501
        :rtype: PipelineIfSpecInput
        """
        return self._if_spec_input

    @if_spec_input.setter
    def if_spec_input(self, if_spec_input):
        """Sets the if_spec_input of this PipelineStepUpdateAPIInput.


        :param if_spec_input: The if_spec_input of this PipelineStepUpdateAPIInput.  # noqa: E501
        :type if_spec_input: PipelineIfSpecInput
        """

        self._if_spec_input = if_spec_input

    @property
    def manual_input_spec_input(self):
        """Gets the manual_input_spec_input of this PipelineStepUpdateAPIInput.  # noqa: E501


        :return: The manual_input_spec_input of this PipelineStepUpdateAPIInput.  # noqa: E501
        :rtype: PipelineManualInputSpecInput
        """
        return self._manual_input_spec_input

    @manual_input_spec_input.setter
    def manual_input_spec_input(self, manual_input_spec_input):
        """Sets the manual_input_spec_input of this PipelineStepUpdateAPIInput.


        :param manual_input_spec_input: The manual_input_spec_input of this PipelineStepUpdateAPIInput.  # noqa: E501
        :type manual_input_spec_input: PipelineManualInputSpecInput
        """

        self._manual_input_spec_input = manual_input_spec_input

    @property
    def manual_judgment_spec_input(self):
        """Gets the manual_judgment_spec_input of this PipelineStepUpdateAPIInput.  # noqa: E501


        :return: The manual_judgment_spec_input of this PipelineStepUpdateAPIInput.  # noqa: E501
        :rtype: PipelineManualJudgmentSpecInput
        """
        return self._manual_judgment_spec_input

    @manual_judgment_spec_input.setter
    def manual_judgment_spec_input(self, manual_judgment_spec_input):
        """Sets the manual_judgment_spec_input of this PipelineStepUpdateAPIInput.


        :param manual_judgment_spec_input: The manual_judgment_spec_input of this PipelineStepUpdateAPIInput.  # noqa: E501
        :type manual_judgment_spec_input: PipelineManualJudgmentSpecInput
        """

        self._manual_judgment_spec_input = manual_judgment_spec_input

    @property
    def notification_spec_input(self):
        """Gets the notification_spec_input of this PipelineStepUpdateAPIInput.  # noqa: E501


        :return: The notification_spec_input of this PipelineStepUpdateAPIInput.  # noqa: E501
        :rtype: PipelineNotificationSpecInput
        """
        return self._notification_spec_input

    @notification_spec_input.setter
    def notification_spec_input(self, notification_spec_input):
        """Sets the notification_spec_input of this PipelineStepUpdateAPIInput.


        :param notification_spec_input: The notification_spec_input of this PipelineStepUpdateAPIInput.  # noqa: E501
        :type notification_spec_input: PipelineNotificationSpecInput
        """

        self._notification_spec_input = notification_spec_input

    @property
    def run_spec_input(self):
        """Gets the run_spec_input of this PipelineStepUpdateAPIInput.  # noqa: E501


        :return: The run_spec_input of this PipelineStepUpdateAPIInput.  # noqa: E501
        :rtype: PipelineRunSpecInput
        """
        return self._run_spec_input

    @run_spec_input.setter
    def run_spec_input(self, run_spec_input):
        """Sets the run_spec_input of this PipelineStepUpdateAPIInput.


        :param run_spec_input: The run_spec_input of this PipelineStepUpdateAPIInput.  # noqa: E501
        :type run_spec_input: PipelineRunSpecInput
        """

        self._run_spec_input = run_spec_input

    @property
    def step_key(self):
        """Gets the step_key of this PipelineStepUpdateAPIInput.  # noqa: E501


        :return: The step_key of this PipelineStepUpdateAPIInput.  # noqa: E501
        :rtype: str
        """
        return self._step_key

    @step_key.setter
    def step_key(self, step_key):
        """Sets the step_key of this PipelineStepUpdateAPIInput.


        :param step_key: The step_key of this PipelineStepUpdateAPIInput.  # noqa: E501
        :type step_key: str
        """
        if self.local_vars_configuration.client_side_validation and step_key is None:  # noqa: E501
            raise ValueError("Invalid value for `step_key`, must not be `None`")  # noqa: E501

        self._step_key = step_key

    @property
    def title(self):
        """Gets the title of this PipelineStepUpdateAPIInput.  # noqa: E501


        :return: The title of this PipelineStepUpdateAPIInput.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this PipelineStepUpdateAPIInput.


        :param title: The title of this PipelineStepUpdateAPIInput.  # noqa: E501
        :type title: str
        """
        if self.local_vars_configuration.client_side_validation and title is None:  # noqa: E501
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def trigger_dispatch_input(self):
        """Gets the trigger_dispatch_input of this PipelineStepUpdateAPIInput.  # noqa: E501


        :return: The trigger_dispatch_input of this PipelineStepUpdateAPIInput.  # noqa: E501
        :rtype: PipelineTriggerDispatchInput
        """
        return self._trigger_dispatch_input

    @trigger_dispatch_input.setter
    def trigger_dispatch_input(self, trigger_dispatch_input):
        """Sets the trigger_dispatch_input of this PipelineStepUpdateAPIInput.


        :param trigger_dispatch_input: The trigger_dispatch_input of this PipelineStepUpdateAPIInput.  # noqa: E501
        :type trigger_dispatch_input: PipelineTriggerDispatchInput
        """

        self._trigger_dispatch_input = trigger_dispatch_input

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
        if not isinstance(other, PipelineStepUpdateAPIInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PipelineStepUpdateAPIInput):
            return True

        return self.to_dict() != other.to_dict()
