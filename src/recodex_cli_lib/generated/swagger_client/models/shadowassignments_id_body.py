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

class ShadowassignmentsIdBody(object):
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
        'version': 'int',
        'is_public': 'bool',
        'is_bonus': 'bool',
        'localized_texts': 'list[object]',
        'max_points': 'int',
        'send_notification': 'bool',
        'deadline': 'int'
    }

    attribute_map = {
        'version': 'version',
        'is_public': 'isPublic',
        'is_bonus': 'isBonus',
        'localized_texts': 'localizedTexts',
        'max_points': 'maxPoints',
        'send_notification': 'sendNotification',
        'deadline': 'deadline'
    }

    def __init__(self, version=None, is_public=None, is_bonus=None, localized_texts=None, max_points=None, send_notification=None, deadline=None):  # noqa: E501
        """ShadowassignmentsIdBody - a model defined in Swagger"""  # noqa: E501
        self._version = None
        self._is_public = None
        self._is_bonus = None
        self._localized_texts = None
        self._max_points = None
        self._send_notification = None
        self._deadline = None
        self.discriminator = None
        if version is not None:
            self.version = version
        if is_public is not None:
            self.is_public = is_public
        if is_bonus is not None:
            self.is_bonus = is_bonus
        if localized_texts is not None:
            self.localized_texts = localized_texts
        if max_points is not None:
            self.max_points = max_points
        if send_notification is not None:
            self.send_notification = send_notification
        if deadline is not None:
            self.deadline = deadline

    @property
    def version(self):
        """Gets the version of this ShadowassignmentsIdBody.  # noqa: E501

        Version of the edited assignment  # noqa: E501

        :return: The version of this ShadowassignmentsIdBody.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ShadowassignmentsIdBody.

        Version of the edited assignment  # noqa: E501

        :param version: The version of this ShadowassignmentsIdBody.  # noqa: E501
        :type: int
        """

        self._version = version

    @property
    def is_public(self):
        """Gets the is_public of this ShadowassignmentsIdBody.  # noqa: E501

        Is the assignment ready to be displayed to students?  # noqa: E501

        :return: The is_public of this ShadowassignmentsIdBody.  # noqa: E501
        :rtype: bool
        """
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        """Sets the is_public of this ShadowassignmentsIdBody.

        Is the assignment ready to be displayed to students?  # noqa: E501

        :param is_public: The is_public of this ShadowassignmentsIdBody.  # noqa: E501
        :type: bool
        """

        self._is_public = is_public

    @property
    def is_bonus(self):
        """Gets the is_bonus of this ShadowassignmentsIdBody.  # noqa: E501

        If true, the points from this exercise will not be included in overall score of group  # noqa: E501

        :return: The is_bonus of this ShadowassignmentsIdBody.  # noqa: E501
        :rtype: bool
        """
        return self._is_bonus

    @is_bonus.setter
    def is_bonus(self, is_bonus):
        """Sets the is_bonus of this ShadowassignmentsIdBody.

        If true, the points from this exercise will not be included in overall score of group  # noqa: E501

        :param is_bonus: The is_bonus of this ShadowassignmentsIdBody.  # noqa: E501
        :type: bool
        """

        self._is_bonus = is_bonus

    @property
    def localized_texts(self):
        """Gets the localized_texts of this ShadowassignmentsIdBody.  # noqa: E501

        A description of the assignment  # noqa: E501

        :return: The localized_texts of this ShadowassignmentsIdBody.  # noqa: E501
        :rtype: list[object]
        """
        return self._localized_texts

    @localized_texts.setter
    def localized_texts(self, localized_texts):
        """Sets the localized_texts of this ShadowassignmentsIdBody.

        A description of the assignment  # noqa: E501

        :param localized_texts: The localized_texts of this ShadowassignmentsIdBody.  # noqa: E501
        :type: list[object]
        """

        self._localized_texts = localized_texts

    @property
    def max_points(self):
        """Gets the max_points of this ShadowassignmentsIdBody.  # noqa: E501

        A maximum of points that user can be awarded  # noqa: E501

        :return: The max_points of this ShadowassignmentsIdBody.  # noqa: E501
        :rtype: int
        """
        return self._max_points

    @max_points.setter
    def max_points(self, max_points):
        """Sets the max_points of this ShadowassignmentsIdBody.

        A maximum of points that user can be awarded  # noqa: E501

        :param max_points: The max_points of this ShadowassignmentsIdBody.  # noqa: E501
        :type: int
        """

        self._max_points = max_points

    @property
    def send_notification(self):
        """Gets the send_notification of this ShadowassignmentsIdBody.  # noqa: E501

        If email notification should be sent  # noqa: E501

        :return: The send_notification of this ShadowassignmentsIdBody.  # noqa: E501
        :rtype: bool
        """
        return self._send_notification

    @send_notification.setter
    def send_notification(self, send_notification):
        """Sets the send_notification of this ShadowassignmentsIdBody.

        If email notification should be sent  # noqa: E501

        :param send_notification: The send_notification of this ShadowassignmentsIdBody.  # noqa: E501
        :type: bool
        """

        self._send_notification = send_notification

    @property
    def deadline(self):
        """Gets the deadline of this ShadowassignmentsIdBody.  # noqa: E501

        Deadline (only for visualization), missing value meas no deadline (same as null)  # noqa: E501

        :return: The deadline of this ShadowassignmentsIdBody.  # noqa: E501
        :rtype: int
        """
        return self._deadline

    @deadline.setter
    def deadline(self, deadline):
        """Sets the deadline of this ShadowassignmentsIdBody.

        Deadline (only for visualization), missing value meas no deadline (same as null)  # noqa: E501

        :param deadline: The deadline of this ShadowassignmentsIdBody.  # noqa: E501
        :type: int
        """

        self._deadline = deadline

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
        if issubclass(ShadowassignmentsIdBody, dict):
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
        if not isinstance(other, ShadowassignmentsIdBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
