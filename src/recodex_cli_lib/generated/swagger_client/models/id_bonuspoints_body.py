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

class IdBonuspointsBody(object):
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
        'bonus_points': 'int',
        'overridden_points': 'str'
    }

    attribute_map = {
        'bonus_points': 'bonusPoints',
        'overridden_points': 'overriddenPoints'
    }

    def __init__(self, bonus_points=None, overridden_points=None):  # noqa: E501
        """IdBonuspointsBody - a model defined in Swagger"""  # noqa: E501
        self._bonus_points = None
        self._overridden_points = None
        self.discriminator = None
        if bonus_points is not None:
            self.bonus_points = bonus_points
        if overridden_points is not None:
            self.overridden_points = overridden_points

    @property
    def bonus_points(self):
        """Gets the bonus_points of this IdBonuspointsBody.  # noqa: E501

        New amount of bonus points, can be negative number  # noqa: E501

        :return: The bonus_points of this IdBonuspointsBody.  # noqa: E501
        :rtype: int
        """
        return self._bonus_points

    @bonus_points.setter
    def bonus_points(self, bonus_points):
        """Sets the bonus_points of this IdBonuspointsBody.

        New amount of bonus points, can be negative number  # noqa: E501

        :param bonus_points: The bonus_points of this IdBonuspointsBody.  # noqa: E501
        :type: int
        """

        self._bonus_points = bonus_points

    @property
    def overridden_points(self):
        """Gets the overridden_points of this IdBonuspointsBody.  # noqa: E501

        Overrides points assigned to solution by the system  # noqa: E501

        :return: The overridden_points of this IdBonuspointsBody.  # noqa: E501
        :rtype: str
        """
        return self._overridden_points

    @overridden_points.setter
    def overridden_points(self, overridden_points):
        """Sets the overridden_points of this IdBonuspointsBody.

        Overrides points assigned to solution by the system  # noqa: E501

        :param overridden_points: The overridden_points of this IdBonuspointsBody.  # noqa: E501
        :type: str
        """

        self._overridden_points = overridden_points

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
        if issubclass(IdBonuspointsBody, dict):
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
        if not isinstance(other, IdBonuspointsBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
