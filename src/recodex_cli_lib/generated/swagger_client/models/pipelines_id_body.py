# coding: utf-8

"""
    ReCodEx API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PipelinesIdBody(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'version': 'int',
        'description': 'str',
        'pipeline': 'str',
        'parameters': 'list[object]',
        '_global': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'version': 'version',
        'description': 'description',
        'pipeline': 'pipeline',
        'parameters': 'parameters',
        '_global': 'global'
    }

    def __init__(self, name=None, version=None, description=None, pipeline=None, parameters=None, _global=None):  # noqa: E501
        """PipelinesIdBody - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._version = None
        self._description = None
        self._pipeline = None
        self._parameters = None
        self.__global = None
        self.discriminator = None
        self.name = name
        self.version = version
        self.description = description
        if pipeline is not None:
            self.pipeline = pipeline
        if parameters is not None:
            self.parameters = parameters
        if _global is not None:
            self._global = _global

    @property
    def name(self):
        """Gets the name of this PipelinesIdBody.  # noqa: E501

        Name of the pipeline  # noqa: E501

        :return: The name of this PipelinesIdBody.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PipelinesIdBody.

        Name of the pipeline  # noqa: E501

        :param name: The name of this PipelinesIdBody.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def version(self):
        """Gets the version of this PipelinesIdBody.  # noqa: E501

        Version of the edited pipeline  # noqa: E501

        :return: The version of this PipelinesIdBody.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this PipelinesIdBody.

        Version of the edited pipeline  # noqa: E501

        :param version: The version of this PipelinesIdBody.  # noqa: E501
        :type: int
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def description(self):
        """Gets the description of this PipelinesIdBody.  # noqa: E501

        Human readable description of pipeline  # noqa: E501

        :return: The description of this PipelinesIdBody.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PipelinesIdBody.

        Human readable description of pipeline  # noqa: E501

        :param description: The description of this PipelinesIdBody.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def pipeline(self):
        """Gets the pipeline of this PipelinesIdBody.  # noqa: E501

        Pipeline configuration  # noqa: E501

        :return: The pipeline of this PipelinesIdBody.  # noqa: E501
        :rtype: str
        """
        return self._pipeline

    @pipeline.setter
    def pipeline(self, pipeline):
        """Sets the pipeline of this PipelinesIdBody.

        Pipeline configuration  # noqa: E501

        :param pipeline: The pipeline of this PipelinesIdBody.  # noqa: E501
        :type: str
        """

        self._pipeline = pipeline

    @property
    def parameters(self):
        """Gets the parameters of this PipelinesIdBody.  # noqa: E501

        A set of parameters  # noqa: E501

        :return: The parameters of this PipelinesIdBody.  # noqa: E501
        :rtype: list[object]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this PipelinesIdBody.

        A set of parameters  # noqa: E501

        :param parameters: The parameters of this PipelinesIdBody.  # noqa: E501
        :type: list[object]
        """

        self._parameters = parameters

    @property
    def _global(self):
        """Gets the _global of this PipelinesIdBody.  # noqa: E501

        Whether the pipeline is global (has no author, is used in generic runtimes)  # noqa: E501

        :return: The _global of this PipelinesIdBody.  # noqa: E501
        :rtype: bool
        """
        return self.__global

    @_global.setter
    def _global(self, _global):
        """Sets the _global of this PipelinesIdBody.

        Whether the pipeline is global (has no author, is used in generic runtimes)  # noqa: E501

        :param _global: The _global of this PipelinesIdBody.  # noqa: E501
        :type: bool
        """

        self.__global = _global

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(PipelinesIdBody, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PipelinesIdBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
