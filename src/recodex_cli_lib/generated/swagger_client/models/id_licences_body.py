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

class IdLicencesBody(object):
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
        'note': 'str',
        'valid_until': 'int'
    }

    attribute_map = {
        'note': 'note',
        'valid_until': 'validUntil'
    }

    def __init__(self, note=None, valid_until=None):  # noqa: E501
        """IdLicencesBody - a model defined in Swagger"""  # noqa: E501
        self._note = None
        self._valid_until = None
        self.discriminator = None
        self.note = note
        self.valid_until = valid_until

    @property
    def note(self):
        """Gets the note of this IdLicencesBody.  # noqa: E501

        A note for users or administrators  # noqa: E501

        :return: The note of this IdLicencesBody.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this IdLicencesBody.

        A note for users or administrators  # noqa: E501

        :param note: The note of this IdLicencesBody.  # noqa: E501
        :type: str
        """
        if note is None:
            raise ValueError("Invalid value for `note`, must not be `None`")  # noqa: E501

        self._note = note

    @property
    def valid_until(self):
        """Gets the valid_until of this IdLicencesBody.  # noqa: E501

        Expiration date of the license  # noqa: E501

        :return: The valid_until of this IdLicencesBody.  # noqa: E501
        :rtype: int
        """
        return self._valid_until

    @valid_until.setter
    def valid_until(self, valid_until):
        """Sets the valid_until of this IdLicencesBody.

        Expiration date of the license  # noqa: E501

        :param valid_until: The valid_until of this IdLicencesBody.  # noqa: E501
        :type: int
        """
        if valid_until is None:
            raise ValueError("Invalid value for `valid_until`, must not be `None`")  # noqa: E501

        self._valid_until = valid_until

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
        if issubclass(IdLicencesBody, dict):
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
        if not isinstance(other, IdLicencesBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
