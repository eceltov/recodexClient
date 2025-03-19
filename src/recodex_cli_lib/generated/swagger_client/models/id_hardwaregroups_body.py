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

class IdHardwaregroupsBody(object):
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
        'hw_groups': 'list[object]'
    }

    attribute_map = {
        'hw_groups': 'hwGroups'
    }

    def __init__(self, hw_groups=None):  # noqa: E501
        """IdHardwaregroupsBody - a model defined in Swagger"""  # noqa: E501
        self._hw_groups = None
        self.discriminator = None
        if hw_groups is not None:
            self.hw_groups = hw_groups

    @property
    def hw_groups(self):
        """Gets the hw_groups of this IdHardwaregroupsBody.  # noqa: E501

        List of hardware groups identifications to which exercise belongs to  # noqa: E501

        :return: The hw_groups of this IdHardwaregroupsBody.  # noqa: E501
        :rtype: list[object]
        """
        return self._hw_groups

    @hw_groups.setter
    def hw_groups(self, hw_groups):
        """Sets the hw_groups of this IdHardwaregroupsBody.

        List of hardware groups identifications to which exercise belongs to  # noqa: E501

        :param hw_groups: The hw_groups of this IdHardwaregroupsBody.  # noqa: E501
        :type: list[object]
        """

        self._hw_groups = hw_groups

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
        if issubclass(IdHardwaregroupsBody, dict):
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
        if not isinstance(other, IdHardwaregroupsBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
