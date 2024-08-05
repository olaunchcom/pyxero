# coding: utf-8

"""
    Xero Accounting API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class CreditNotes(BaseModel):
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
        "pagination": "Pagination",
        "warnings": "list[ValidationError]",
        "credit_notes": "list[CreditNote]",
    }

    attribute_map = {
        "pagination": "pagination",
        "warnings": "Warnings",
        "credit_notes": "CreditNotes",
    }

    def __init__(self, pagination=None, warnings=None, credit_notes=None):  # noqa: E501
        """CreditNotes - a model defined in OpenAPI"""  # noqa: E501

        self._pagination = None
        self._warnings = None
        self._credit_notes = None
        self.discriminator = None

        if pagination is not None:
            self.pagination = pagination
        if warnings is not None:
            self.warnings = warnings
        if credit_notes is not None:
            self.credit_notes = credit_notes

    @property
    def pagination(self):
        """Gets the pagination of this CreditNotes.  # noqa: E501


        :return: The pagination of this CreditNotes.  # noqa: E501
        :rtype: Pagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this CreditNotes.


        :param pagination: The pagination of this CreditNotes.  # noqa: E501
        :type: Pagination
        """

        self._pagination = pagination

    @property
    def warnings(self):
        """Gets the warnings of this CreditNotes.  # noqa: E501

        Displays array of warning messages from the API  # noqa: E501

        :return: The warnings of this CreditNotes.  # noqa: E501
        :rtype: list[ValidationError]
        """
        return self._warnings

    @warnings.setter
    def warnings(self, warnings):
        """Sets the warnings of this CreditNotes.

        Displays array of warning messages from the API  # noqa: E501

        :param warnings: The warnings of this CreditNotes.  # noqa: E501
        :type: list[ValidationError]
        """

        self._warnings = warnings

    @property
    def credit_notes(self):
        """Gets the credit_notes of this CreditNotes.  # noqa: E501


        :return: The credit_notes of this CreditNotes.  # noqa: E501
        :rtype: list[CreditNote]
        """
        return self._credit_notes

    @credit_notes.setter
    def credit_notes(self, credit_notes):
        """Sets the credit_notes of this CreditNotes.


        :param credit_notes: The credit_notes of this CreditNotes.  # noqa: E501
        :type: list[CreditNote]
        """

        self._credit_notes = credit_notes
