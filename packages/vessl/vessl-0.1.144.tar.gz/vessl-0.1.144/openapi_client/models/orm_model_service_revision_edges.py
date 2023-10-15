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


class OrmModelServiceRevisionEdges(object):
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
        'created_by': 'OrmUser',
        'kernel_image': 'OrmKernelImage',
        'model': 'OrmModel',
        'model_service': 'OrmModelService',
        'workload': 'OrmWorkload'
    }

    attribute_map = {
        'access_token': 'access_token',
        'created_by': 'created_by',
        'kernel_image': 'kernel_image',
        'model': 'model',
        'model_service': 'model_service',
        'workload': 'workload'
    }

    def __init__(self, access_token=None, created_by=None, kernel_image=None, model=None, model_service=None, workload=None, local_vars_configuration=None):  # noqa: E501
        """OrmModelServiceRevisionEdges - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._access_token = None
        self._created_by = None
        self._kernel_image = None
        self._model = None
        self._model_service = None
        self._workload = None
        self.discriminator = None

        if access_token is not None:
            self.access_token = access_token
        if created_by is not None:
            self.created_by = created_by
        if kernel_image is not None:
            self.kernel_image = kernel_image
        if model is not None:
            self.model = model
        if model_service is not None:
            self.model_service = model_service
        if workload is not None:
            self.workload = workload

    @property
    def access_token(self):
        """Gets the access_token of this OrmModelServiceRevisionEdges.  # noqa: E501


        :return: The access_token of this OrmModelServiceRevisionEdges.  # noqa: E501
        :rtype: OrmAccessToken
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this OrmModelServiceRevisionEdges.


        :param access_token: The access_token of this OrmModelServiceRevisionEdges.  # noqa: E501
        :type access_token: OrmAccessToken
        """

        self._access_token = access_token

    @property
    def created_by(self):
        """Gets the created_by of this OrmModelServiceRevisionEdges.  # noqa: E501


        :return: The created_by of this OrmModelServiceRevisionEdges.  # noqa: E501
        :rtype: OrmUser
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this OrmModelServiceRevisionEdges.


        :param created_by: The created_by of this OrmModelServiceRevisionEdges.  # noqa: E501
        :type created_by: OrmUser
        """

        self._created_by = created_by

    @property
    def kernel_image(self):
        """Gets the kernel_image of this OrmModelServiceRevisionEdges.  # noqa: E501


        :return: The kernel_image of this OrmModelServiceRevisionEdges.  # noqa: E501
        :rtype: OrmKernelImage
        """
        return self._kernel_image

    @kernel_image.setter
    def kernel_image(self, kernel_image):
        """Sets the kernel_image of this OrmModelServiceRevisionEdges.


        :param kernel_image: The kernel_image of this OrmModelServiceRevisionEdges.  # noqa: E501
        :type kernel_image: OrmKernelImage
        """

        self._kernel_image = kernel_image

    @property
    def model(self):
        """Gets the model of this OrmModelServiceRevisionEdges.  # noqa: E501


        :return: The model of this OrmModelServiceRevisionEdges.  # noqa: E501
        :rtype: OrmModel
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this OrmModelServiceRevisionEdges.


        :param model: The model of this OrmModelServiceRevisionEdges.  # noqa: E501
        :type model: OrmModel
        """

        self._model = model

    @property
    def model_service(self):
        """Gets the model_service of this OrmModelServiceRevisionEdges.  # noqa: E501


        :return: The model_service of this OrmModelServiceRevisionEdges.  # noqa: E501
        :rtype: OrmModelService
        """
        return self._model_service

    @model_service.setter
    def model_service(self, model_service):
        """Sets the model_service of this OrmModelServiceRevisionEdges.


        :param model_service: The model_service of this OrmModelServiceRevisionEdges.  # noqa: E501
        :type model_service: OrmModelService
        """

        self._model_service = model_service

    @property
    def workload(self):
        """Gets the workload of this OrmModelServiceRevisionEdges.  # noqa: E501


        :return: The workload of this OrmModelServiceRevisionEdges.  # noqa: E501
        :rtype: OrmWorkload
        """
        return self._workload

    @workload.setter
    def workload(self, workload):
        """Sets the workload of this OrmModelServiceRevisionEdges.


        :param workload: The workload of this OrmModelServiceRevisionEdges.  # noqa: E501
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
        if not isinstance(other, OrmModelServiceRevisionEdges):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrmModelServiceRevisionEdges):
            return True

        return self.to_dict() != other.to_dict()
