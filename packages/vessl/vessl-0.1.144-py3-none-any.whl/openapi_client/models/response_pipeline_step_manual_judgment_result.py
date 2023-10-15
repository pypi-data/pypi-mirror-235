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


class ResponsePipelineStepManualJudgmentResult(object):
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
        'assignee_email_addresses': 'list[str]',
        'judged_by': 'str',
        'judgment_dt': 'datetime',
        'result': 'str'
    }

    attribute_map = {
        'assignee_email_addresses': 'assignee_email_addresses',
        'judged_by': 'judged_by',
        'judgment_dt': 'judgment_dt',
        'result': 'result'
    }

    def __init__(self, assignee_email_addresses=None, judged_by=None, judgment_dt=None, result=None, local_vars_configuration=None):  # noqa: E501
        """ResponsePipelineStepManualJudgmentResult - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._assignee_email_addresses = None
        self._judged_by = None
        self._judgment_dt = None
        self._result = None
        self.discriminator = None

        if assignee_email_addresses is not None:
            self.assignee_email_addresses = assignee_email_addresses
        self.judged_by = judged_by
        self.judgment_dt = judgment_dt
        self.result = result

    @property
    def assignee_email_addresses(self):
        """Gets the assignee_email_addresses of this ResponsePipelineStepManualJudgmentResult.  # noqa: E501


        :return: The assignee_email_addresses of this ResponsePipelineStepManualJudgmentResult.  # noqa: E501
        :rtype: list[str]
        """
        return self._assignee_email_addresses

    @assignee_email_addresses.setter
    def assignee_email_addresses(self, assignee_email_addresses):
        """Sets the assignee_email_addresses of this ResponsePipelineStepManualJudgmentResult.


        :param assignee_email_addresses: The assignee_email_addresses of this ResponsePipelineStepManualJudgmentResult.  # noqa: E501
        :type assignee_email_addresses: list[str]
        """

        self._assignee_email_addresses = assignee_email_addresses

    @property
    def judged_by(self):
        """Gets the judged_by of this ResponsePipelineStepManualJudgmentResult.  # noqa: E501


        :return: The judged_by of this ResponsePipelineStepManualJudgmentResult.  # noqa: E501
        :rtype: str
        """
        return self._judged_by

    @judged_by.setter
    def judged_by(self, judged_by):
        """Sets the judged_by of this ResponsePipelineStepManualJudgmentResult.


        :param judged_by: The judged_by of this ResponsePipelineStepManualJudgmentResult.  # noqa: E501
        :type judged_by: str
        """

        self._judged_by = judged_by

    @property
    def judgment_dt(self):
        """Gets the judgment_dt of this ResponsePipelineStepManualJudgmentResult.  # noqa: E501


        :return: The judgment_dt of this ResponsePipelineStepManualJudgmentResult.  # noqa: E501
        :rtype: datetime
        """
        return self._judgment_dt

    @judgment_dt.setter
    def judgment_dt(self, judgment_dt):
        """Sets the judgment_dt of this ResponsePipelineStepManualJudgmentResult.


        :param judgment_dt: The judgment_dt of this ResponsePipelineStepManualJudgmentResult.  # noqa: E501
        :type judgment_dt: datetime
        """

        self._judgment_dt = judgment_dt

    @property
    def result(self):
        """Gets the result of this ResponsePipelineStepManualJudgmentResult.  # noqa: E501


        :return: The result of this ResponsePipelineStepManualJudgmentResult.  # noqa: E501
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this ResponsePipelineStepManualJudgmentResult.


        :param result: The result of this ResponsePipelineStepManualJudgmentResult.  # noqa: E501
        :type result: str
        """

        self._result = result

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
        if not isinstance(other, ResponsePipelineStepManualJudgmentResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResponsePipelineStepManualJudgmentResult):
            return True

        return self.to_dict() != other.to_dict()
