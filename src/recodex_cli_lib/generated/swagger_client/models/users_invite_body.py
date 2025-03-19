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

class UsersInviteBody(object):
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
        'email': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'instance_id': 'str',
        'titles_before_name': 'str',
        'titles_after_name': 'str',
        'groups': 'list[object]',
        'locale': 'str',
        'test': 'V1usersinviteTest'
    }

    attribute_map = {
        'email': 'email',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'instance_id': 'instanceId',
        'titles_before_name': 'titlesBeforeName',
        'titles_after_name': 'titlesAfterName',
        'groups': 'groups',
        'locale': 'locale',
        'test': 'test'
    }

    def __init__(self, email=None, first_name=None, last_name=None, instance_id=None, titles_before_name=None, titles_after_name=None, groups=None, locale=None, test=None):  # noqa: E501
        """UsersInviteBody - a model defined in Swagger"""  # noqa: E501
        self._email = None
        self._first_name = None
        self._last_name = None
        self._instance_id = None
        self._titles_before_name = None
        self._titles_after_name = None
        self._groups = None
        self._locale = None
        self._test = None
        self.discriminator = None
        if email is not None:
            self.email = email
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if instance_id is not None:
            self.instance_id = instance_id
        if titles_before_name is not None:
            self.titles_before_name = titles_before_name
        if titles_after_name is not None:
            self.titles_after_name = titles_after_name
        if groups is not None:
            self.groups = groups
        if locale is not None:
            self.locale = locale
        if test is not None:
            self.test = test

    @property
    def email(self):
        """Gets the email of this UsersInviteBody.  # noqa: E501

        An email that will serve as a login name  # noqa: E501

        :return: The email of this UsersInviteBody.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UsersInviteBody.

        An email that will serve as a login name  # noqa: E501

        :param email: The email of this UsersInviteBody.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def first_name(self):
        """Gets the first_name of this UsersInviteBody.  # noqa: E501

        First name  # noqa: E501

        :return: The first_name of this UsersInviteBody.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this UsersInviteBody.

        First name  # noqa: E501

        :param first_name: The first_name of this UsersInviteBody.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this UsersInviteBody.  # noqa: E501

        Last name  # noqa: E501

        :return: The last_name of this UsersInviteBody.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this UsersInviteBody.

        Last name  # noqa: E501

        :param last_name: The last_name of this UsersInviteBody.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def instance_id(self):
        """Gets the instance_id of this UsersInviteBody.  # noqa: E501

        Identifier of the instance to register in  # noqa: E501

        :return: The instance_id of this UsersInviteBody.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this UsersInviteBody.

        Identifier of the instance to register in  # noqa: E501

        :param instance_id: The instance_id of this UsersInviteBody.  # noqa: E501
        :type: str
        """

        self._instance_id = instance_id

    @property
    def titles_before_name(self):
        """Gets the titles_before_name of this UsersInviteBody.  # noqa: E501

        Titles that are placed before user name  # noqa: E501

        :return: The titles_before_name of this UsersInviteBody.  # noqa: E501
        :rtype: str
        """
        return self._titles_before_name

    @titles_before_name.setter
    def titles_before_name(self, titles_before_name):
        """Sets the titles_before_name of this UsersInviteBody.

        Titles that are placed before user name  # noqa: E501

        :param titles_before_name: The titles_before_name of this UsersInviteBody.  # noqa: E501
        :type: str
        """

        self._titles_before_name = titles_before_name

    @property
    def titles_after_name(self):
        """Gets the titles_after_name of this UsersInviteBody.  # noqa: E501

        Titles that are placed after user name  # noqa: E501

        :return: The titles_after_name of this UsersInviteBody.  # noqa: E501
        :rtype: str
        """
        return self._titles_after_name

    @titles_after_name.setter
    def titles_after_name(self, titles_after_name):
        """Sets the titles_after_name of this UsersInviteBody.

        Titles that are placed after user name  # noqa: E501

        :param titles_after_name: The titles_after_name of this UsersInviteBody.  # noqa: E501
        :type: str
        """

        self._titles_after_name = titles_after_name

    @property
    def groups(self):
        """Gets the groups of this UsersInviteBody.  # noqa: E501

        List of group IDs in which the user is added right after registration  # noqa: E501

        :return: The groups of this UsersInviteBody.  # noqa: E501
        :rtype: list[object]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this UsersInviteBody.

        List of group IDs in which the user is added right after registration  # noqa: E501

        :param groups: The groups of this UsersInviteBody.  # noqa: E501
        :type: list[object]
        """

        self._groups = groups

    @property
    def locale(self):
        """Gets the locale of this UsersInviteBody.  # noqa: E501

        Language used in the invitation email (en by default).  # noqa: E501

        :return: The locale of this UsersInviteBody.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this UsersInviteBody.

        Language used in the invitation email (en by default).  # noqa: E501

        :param locale: The locale of this UsersInviteBody.  # noqa: E501
        :type: str
        """

        self._locale = locale

    @property
    def test(self):
        """Gets the test of this UsersInviteBody.  # noqa: E501


        :return: The test of this UsersInviteBody.  # noqa: E501
        :rtype: V1usersinviteTest
        """
        return self._test

    @test.setter
    def test(self, test):
        """Sets the test of this UsersInviteBody.


        :param test: The test of this UsersInviteBody.  # noqa: E501
        :type: V1usersinviteTest
        """

        self._test = test

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
        if issubclass(UsersInviteBody, dict):
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
        if not isinstance(other, UsersInviteBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
