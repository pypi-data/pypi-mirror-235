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


class OrmPipelineStepExecution(object):
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
        'assignee_email_addresses': 'dict[str, object]',
        'context': 'dict[str, object]',
        'created_dt': 'datetime',
        'edges': 'OrmPipelineStepExecutionEdges',
        'external_service_endpoint': 'str',
        'id': 'int',
        'immutable_slug': 'str',
        'judged_user_id': 'int',
        'judgment_dt': 'datetime',
        'pipeline_execution_id': 'int',
        'status': 'str',
        'step_id': 'int',
        'step_spec_id': 'int',
        'triggering_pipeline_execution_id': 'int',
        'updated_dt': 'datetime',
        'variables': 'dict[str, object]'
    }

    attribute_map = {
        'assignee_email_addresses': 'assignee_email_addresses',
        'context': 'context',
        'created_dt': 'created_dt',
        'edges': 'edges',
        'external_service_endpoint': 'external_service_endpoint',
        'id': 'id',
        'immutable_slug': 'immutable_slug',
        'judged_user_id': 'judged_user_id',
        'judgment_dt': 'judgment_dt',
        'pipeline_execution_id': 'pipeline_execution_id',
        'status': 'status',
        'step_id': 'step_id',
        'step_spec_id': 'step_spec_id',
        'triggering_pipeline_execution_id': 'triggering_pipeline_execution_id',
        'updated_dt': 'updated_dt',
        'variables': 'variables'
    }

    def __init__(self, assignee_email_addresses=None, context=None, created_dt=None, edges=None, external_service_endpoint=None, id=None, immutable_slug=None, judged_user_id=None, judgment_dt=None, pipeline_execution_id=None, status=None, step_id=None, step_spec_id=None, triggering_pipeline_execution_id=None, updated_dt=None, variables=None, local_vars_configuration=None):  # noqa: E501
        """OrmPipelineStepExecution - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._assignee_email_addresses = None
        self._context = None
        self._created_dt = None
        self._edges = None
        self._external_service_endpoint = None
        self._id = None
        self._immutable_slug = None
        self._judged_user_id = None
        self._judgment_dt = None
        self._pipeline_execution_id = None
        self._status = None
        self._step_id = None
        self._step_spec_id = None
        self._triggering_pipeline_execution_id = None
        self._updated_dt = None
        self._variables = None
        self.discriminator = None

        if assignee_email_addresses is not None:
            self.assignee_email_addresses = assignee_email_addresses
        if context is not None:
            self.context = context
        if created_dt is not None:
            self.created_dt = created_dt
        if edges is not None:
            self.edges = edges
        self.external_service_endpoint = external_service_endpoint
        if id is not None:
            self.id = id
        if immutable_slug is not None:
            self.immutable_slug = immutable_slug
        self.judged_user_id = judged_user_id
        self.judgment_dt = judgment_dt
        if pipeline_execution_id is not None:
            self.pipeline_execution_id = pipeline_execution_id
        if status is not None:
            self.status = status
        self.step_id = step_id
        self.step_spec_id = step_spec_id
        self.triggering_pipeline_execution_id = triggering_pipeline_execution_id
        if updated_dt is not None:
            self.updated_dt = updated_dt
        if variables is not None:
            self.variables = variables

    @property
    def assignee_email_addresses(self):
        """Gets the assignee_email_addresses of this OrmPipelineStepExecution.  # noqa: E501


        :return: The assignee_email_addresses of this OrmPipelineStepExecution.  # noqa: E501
        :rtype: dict[str, object]
        """
        return self._assignee_email_addresses

    @assignee_email_addresses.setter
    def assignee_email_addresses(self, assignee_email_addresses):
        """Sets the assignee_email_addresses of this OrmPipelineStepExecution.


        :param assignee_email_addresses: The assignee_email_addresses of this OrmPipelineStepExecution.  # noqa: E501
        :type assignee_email_addresses: dict[str, object]
        """

        self._assignee_email_addresses = assignee_email_addresses

    @property
    def context(self):
        """Gets the context of this OrmPipelineStepExecution.  # noqa: E501


        :return: The context of this OrmPipelineStepExecution.  # noqa: E501
        :rtype: dict[str, object]
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this OrmPipelineStepExecution.


        :param context: The context of this OrmPipelineStepExecution.  # noqa: E501
        :type context: dict[str, object]
        """

        self._context = context

    @property
    def created_dt(self):
        """Gets the created_dt of this OrmPipelineStepExecution.  # noqa: E501


        :return: The created_dt of this OrmPipelineStepExecution.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this OrmPipelineStepExecution.


        :param created_dt: The created_dt of this OrmPipelineStepExecution.  # noqa: E501
        :type created_dt: datetime
        """

        self._created_dt = created_dt

    @property
    def edges(self):
        """Gets the edges of this OrmPipelineStepExecution.  # noqa: E501


        :return: The edges of this OrmPipelineStepExecution.  # noqa: E501
        :rtype: OrmPipelineStepExecutionEdges
        """
        return self._edges

    @edges.setter
    def edges(self, edges):
        """Sets the edges of this OrmPipelineStepExecution.


        :param edges: The edges of this OrmPipelineStepExecution.  # noqa: E501
        :type edges: OrmPipelineStepExecutionEdges
        """

        self._edges = edges

    @property
    def external_service_endpoint(self):
        """Gets the external_service_endpoint of this OrmPipelineStepExecution.  # noqa: E501


        :return: The external_service_endpoint of this OrmPipelineStepExecution.  # noqa: E501
        :rtype: str
        """
        return self._external_service_endpoint

    @external_service_endpoint.setter
    def external_service_endpoint(self, external_service_endpoint):
        """Sets the external_service_endpoint of this OrmPipelineStepExecution.


        :param external_service_endpoint: The external_service_endpoint of this OrmPipelineStepExecution.  # noqa: E501
        :type external_service_endpoint: str
        """

        self._external_service_endpoint = external_service_endpoint

    @property
    def id(self):
        """Gets the id of this OrmPipelineStepExecution.  # noqa: E501


        :return: The id of this OrmPipelineStepExecution.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OrmPipelineStepExecution.


        :param id: The id of this OrmPipelineStepExecution.  # noqa: E501
        :type id: int
        """

        self._id = id

    @property
    def immutable_slug(self):
        """Gets the immutable_slug of this OrmPipelineStepExecution.  # noqa: E501


        :return: The immutable_slug of this OrmPipelineStepExecution.  # noqa: E501
        :rtype: str
        """
        return self._immutable_slug

    @immutable_slug.setter
    def immutable_slug(self, immutable_slug):
        """Sets the immutable_slug of this OrmPipelineStepExecution.


        :param immutable_slug: The immutable_slug of this OrmPipelineStepExecution.  # noqa: E501
        :type immutable_slug: str
        """

        self._immutable_slug = immutable_slug

    @property
    def judged_user_id(self):
        """Gets the judged_user_id of this OrmPipelineStepExecution.  # noqa: E501


        :return: The judged_user_id of this OrmPipelineStepExecution.  # noqa: E501
        :rtype: int
        """
        return self._judged_user_id

    @judged_user_id.setter
    def judged_user_id(self, judged_user_id):
        """Sets the judged_user_id of this OrmPipelineStepExecution.


        :param judged_user_id: The judged_user_id of this OrmPipelineStepExecution.  # noqa: E501
        :type judged_user_id: int
        """

        self._judged_user_id = judged_user_id

    @property
    def judgment_dt(self):
        """Gets the judgment_dt of this OrmPipelineStepExecution.  # noqa: E501


        :return: The judgment_dt of this OrmPipelineStepExecution.  # noqa: E501
        :rtype: datetime
        """
        return self._judgment_dt

    @judgment_dt.setter
    def judgment_dt(self, judgment_dt):
        """Sets the judgment_dt of this OrmPipelineStepExecution.


        :param judgment_dt: The judgment_dt of this OrmPipelineStepExecution.  # noqa: E501
        :type judgment_dt: datetime
        """

        self._judgment_dt = judgment_dt

    @property
    def pipeline_execution_id(self):
        """Gets the pipeline_execution_id of this OrmPipelineStepExecution.  # noqa: E501


        :return: The pipeline_execution_id of this OrmPipelineStepExecution.  # noqa: E501
        :rtype: int
        """
        return self._pipeline_execution_id

    @pipeline_execution_id.setter
    def pipeline_execution_id(self, pipeline_execution_id):
        """Sets the pipeline_execution_id of this OrmPipelineStepExecution.


        :param pipeline_execution_id: The pipeline_execution_id of this OrmPipelineStepExecution.  # noqa: E501
        :type pipeline_execution_id: int
        """

        self._pipeline_execution_id = pipeline_execution_id

    @property
    def status(self):
        """Gets the status of this OrmPipelineStepExecution.  # noqa: E501


        :return: The status of this OrmPipelineStepExecution.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this OrmPipelineStepExecution.


        :param status: The status of this OrmPipelineStepExecution.  # noqa: E501
        :type status: str
        """

        self._status = status

    @property
    def step_id(self):
        """Gets the step_id of this OrmPipelineStepExecution.  # noqa: E501


        :return: The step_id of this OrmPipelineStepExecution.  # noqa: E501
        :rtype: int
        """
        return self._step_id

    @step_id.setter
    def step_id(self, step_id):
        """Sets the step_id of this OrmPipelineStepExecution.


        :param step_id: The step_id of this OrmPipelineStepExecution.  # noqa: E501
        :type step_id: int
        """

        self._step_id = step_id

    @property
    def step_spec_id(self):
        """Gets the step_spec_id of this OrmPipelineStepExecution.  # noqa: E501


        :return: The step_spec_id of this OrmPipelineStepExecution.  # noqa: E501
        :rtype: int
        """
        return self._step_spec_id

    @step_spec_id.setter
    def step_spec_id(self, step_spec_id):
        """Sets the step_spec_id of this OrmPipelineStepExecution.


        :param step_spec_id: The step_spec_id of this OrmPipelineStepExecution.  # noqa: E501
        :type step_spec_id: int
        """

        self._step_spec_id = step_spec_id

    @property
    def triggering_pipeline_execution_id(self):
        """Gets the triggering_pipeline_execution_id of this OrmPipelineStepExecution.  # noqa: E501


        :return: The triggering_pipeline_execution_id of this OrmPipelineStepExecution.  # noqa: E501
        :rtype: int
        """
        return self._triggering_pipeline_execution_id

    @triggering_pipeline_execution_id.setter
    def triggering_pipeline_execution_id(self, triggering_pipeline_execution_id):
        """Sets the triggering_pipeline_execution_id of this OrmPipelineStepExecution.


        :param triggering_pipeline_execution_id: The triggering_pipeline_execution_id of this OrmPipelineStepExecution.  # noqa: E501
        :type triggering_pipeline_execution_id: int
        """

        self._triggering_pipeline_execution_id = triggering_pipeline_execution_id

    @property
    def updated_dt(self):
        """Gets the updated_dt of this OrmPipelineStepExecution.  # noqa: E501


        :return: The updated_dt of this OrmPipelineStepExecution.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_dt

    @updated_dt.setter
    def updated_dt(self, updated_dt):
        """Sets the updated_dt of this OrmPipelineStepExecution.


        :param updated_dt: The updated_dt of this OrmPipelineStepExecution.  # noqa: E501
        :type updated_dt: datetime
        """

        self._updated_dt = updated_dt

    @property
    def variables(self):
        """Gets the variables of this OrmPipelineStepExecution.  # noqa: E501


        :return: The variables of this OrmPipelineStepExecution.  # noqa: E501
        :rtype: dict[str, object]
        """
        return self._variables

    @variables.setter
    def variables(self, variables):
        """Sets the variables of this OrmPipelineStepExecution.


        :param variables: The variables of this OrmPipelineStepExecution.  # noqa: E501
        :type variables: dict[str, object]
        """

        self._variables = variables

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
        if not isinstance(other, OrmPipelineStepExecution):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrmPipelineStepExecution):
            return True

        return self.to_dict() != other.to_dict()
