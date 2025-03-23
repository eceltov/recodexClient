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

class IdSolutionIdBody(object):
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
        'solution_file_id': 'str',
        'file_entry': 'str',
        'author_id': 'str',
        'similarity': 'float',
        'files': 'list[object]'
    }

    attribute_map = {
        'solution_file_id': 'solutionFileId',
        'file_entry': 'fileEntry',
        'author_id': 'authorId',
        'similarity': 'similarity',
        'files': 'files'
    }

    def __init__(self, solution_file_id=None, file_entry=None, author_id=None, similarity=None, files=None):  # noqa: E501
        """IdSolutionIdBody - a model defined in Swagger"""  # noqa: E501
        self._solution_file_id = None
        self._file_entry = None
        self._author_id = None
        self._similarity = None
        self._files = None
        self.discriminator = None
        self.solution_file_id = solution_file_id
        if file_entry is not None:
            self.file_entry = file_entry
        self.author_id = author_id
        self.similarity = similarity
        self.files = files

    @property
    def solution_file_id(self):
        """Gets the solution_file_id of this IdSolutionIdBody.  # noqa: E501

        Id of the uploaded solution file.  # noqa: E501

        :return: The solution_file_id of this IdSolutionIdBody.  # noqa: E501
        :rtype: str
        """
        return self._solution_file_id

    @solution_file_id.setter
    def solution_file_id(self, solution_file_id):
        """Sets the solution_file_id of this IdSolutionIdBody.

        Id of the uploaded solution file.  # noqa: E501

        :param solution_file_id: The solution_file_id of this IdSolutionIdBody.  # noqa: E501
        :type: str
        """
        if solution_file_id is None:
            raise ValueError("Invalid value for `solution_file_id`, must not be `None`")  # noqa: E501

        self._solution_file_id = solution_file_id

    @property
    def file_entry(self):
        """Gets the file_entry of this IdSolutionIdBody.  # noqa: E501

        Entry (relative path) within a ZIP package (if the uploaded file is a ZIP).  # noqa: E501

        :return: The file_entry of this IdSolutionIdBody.  # noqa: E501
        :rtype: str
        """
        return self._file_entry

    @file_entry.setter
    def file_entry(self, file_entry):
        """Sets the file_entry of this IdSolutionIdBody.

        Entry (relative path) within a ZIP package (if the uploaded file is a ZIP).  # noqa: E501

        :param file_entry: The file_entry of this IdSolutionIdBody.  # noqa: E501
        :type: str
        """

        self._file_entry = file_entry

    @property
    def author_id(self):
        """Gets the author_id of this IdSolutionIdBody.  # noqa: E501

        Id of the author of the similar solutions/files.  # noqa: E501

        :return: The author_id of this IdSolutionIdBody.  # noqa: E501
        :rtype: str
        """
        return self._author_id

    @author_id.setter
    def author_id(self, author_id):
        """Sets the author_id of this IdSolutionIdBody.

        Id of the author of the similar solutions/files.  # noqa: E501

        :param author_id: The author_id of this IdSolutionIdBody.  # noqa: E501
        :type: str
        """
        if author_id is None:
            raise ValueError("Invalid value for `author_id`, must not be `None`")  # noqa: E501

        self._author_id = author_id

    @property
    def similarity(self):
        """Gets the similarity of this IdSolutionIdBody.  # noqa: E501

        Relative similarity of the records associated with selected author [0-1].  # noqa: E501

        :return: The similarity of this IdSolutionIdBody.  # noqa: E501
        :rtype: float
        """
        return self._similarity

    @similarity.setter
    def similarity(self, similarity):
        """Sets the similarity of this IdSolutionIdBody.

        Relative similarity of the records associated with selected author [0-1].  # noqa: E501

        :param similarity: The similarity of this IdSolutionIdBody.  # noqa: E501
        :type: float
        """
        if similarity is None:
            raise ValueError("Invalid value for `similarity`, must not be `None`")  # noqa: E501

        self._similarity = similarity

    @property
    def files(self):
        """Gets the files of this IdSolutionIdBody.  # noqa: E501

        List of similar files and their records.  # noqa: E501

        :return: The files of this IdSolutionIdBody.  # noqa: E501
        :rtype: list[object]
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this IdSolutionIdBody.

        List of similar files and their records.  # noqa: E501

        :param files: The files of this IdSolutionIdBody.  # noqa: E501
        :type: list[object]
        """
        if files is None:
            raise ValueError("Invalid value for `files`, must not be `None`")  # noqa: E501

        self._files = files

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
        if issubclass(IdSolutionIdBody, dict):
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
        if not isinstance(other, IdSolutionIdBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
