# coding: utf-8

"""
    Xero Finance API

    The Finance API is a collection of endpoints which customers can use in the course of a loan application, which may assist lenders to gain the confidence they need to provide capital.  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class CurrentStatementResponse(BaseModel):
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
        "start_date": "date",
        "end_date": "date",
        "start_balance": "float",
        "end_balance": "float",
        "imported_date_time_utc": "datetime",
        "import_source_type": "str",
    }

    attribute_map = {
        "start_date": "startDate",
        "end_date": "endDate",
        "start_balance": "startBalance",
        "end_balance": "endBalance",
        "imported_date_time_utc": "importedDateTimeUtc",
        "import_source_type": "importSourceType",
    }

    def __init__(
        self,
        start_date=None,
        end_date=None,
        start_balance=None,
        end_balance=None,
        imported_date_time_utc=None,
        import_source_type=None,
    ):  # noqa: E501
        """CurrentStatementResponse - a model defined in OpenAPI"""  # noqa: E501

        self._start_date = None
        self._end_date = None
        self._start_balance = None
        self._end_balance = None
        self._imported_date_time_utc = None
        self._import_source_type = None
        self.discriminator = None

        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if start_balance is not None:
            self.start_balance = start_balance
        if end_balance is not None:
            self.end_balance = end_balance
        if imported_date_time_utc is not None:
            self.imported_date_time_utc = imported_date_time_utc
        if import_source_type is not None:
            self.import_source_type = import_source_type

    @property
    def start_date(self):
        """Gets the start_date of this CurrentStatementResponse.  # noqa: E501

        Looking at the most recent bank statement, this field indicates the first date which transactions on this statement pertain to. This date is represented in ISO 8601 format.  # noqa: E501

        :return: The start_date of this CurrentStatementResponse.  # noqa: E501
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this CurrentStatementResponse.

        Looking at the most recent bank statement, this field indicates the first date which transactions on this statement pertain to. This date is represented in ISO 8601 format.  # noqa: E501

        :param start_date: The start_date of this CurrentStatementResponse.  # noqa: E501
        :type: date
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this CurrentStatementResponse.  # noqa: E501

        Looking at the most recent bank statement, this field indicates the last date which transactions on this statement pertain to. This date is represented in ISO 8601 format.  # noqa: E501

        :return: The end_date of this CurrentStatementResponse.  # noqa: E501
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this CurrentStatementResponse.

        Looking at the most recent bank statement, this field indicates the last date which transactions on this statement pertain to. This date is represented in ISO 8601 format.  # noqa: E501

        :param end_date: The end_date of this CurrentStatementResponse.  # noqa: E501
        :type: date
        """

        self._end_date = end_date

    @property
    def start_balance(self):
        """Gets the start_balance of this CurrentStatementResponse.  # noqa: E501

        Looking at the most recent bank statement, this field indicates the balance before the transactions on the statement are applied (note, this is not always populated by the bank in every single instance (~10%)).  # noqa: E501

        :return: The start_balance of this CurrentStatementResponse.  # noqa: E501
        :rtype: float
        """
        return self._start_balance

    @start_balance.setter
    def start_balance(self, start_balance):
        """Sets the start_balance of this CurrentStatementResponse.

        Looking at the most recent bank statement, this field indicates the balance before the transactions on the statement are applied (note, this is not always populated by the bank in every single instance (~10%)).  # noqa: E501

        :param start_balance: The start_balance of this CurrentStatementResponse.  # noqa: E501
        :type: float
        """

        self._start_balance = start_balance

    @property
    def end_balance(self):
        """Gets the end_balance of this CurrentStatementResponse.  # noqa: E501

        Looking at the most recent bank statement, this field indicates the balance after the transactions on the statement are applied (note, this is not always populated by the bank in every single instance (~10%)).  # noqa: E501

        :return: The end_balance of this CurrentStatementResponse.  # noqa: E501
        :rtype: float
        """
        return self._end_balance

    @end_balance.setter
    def end_balance(self, end_balance):
        """Sets the end_balance of this CurrentStatementResponse.

        Looking at the most recent bank statement, this field indicates the balance after the transactions on the statement are applied (note, this is not always populated by the bank in every single instance (~10%)).  # noqa: E501

        :param end_balance: The end_balance of this CurrentStatementResponse.  # noqa: E501
        :type: float
        """

        self._end_balance = end_balance

    @property
    def imported_date_time_utc(self):
        """Gets the imported_date_time_utc of this CurrentStatementResponse.  # noqa: E501

        Looking at the most recent bank statement, this field indicates when the document was imported into Xero.  This date is represented in ISO 8601 format.  # noqa: E501

        :return: The imported_date_time_utc of this CurrentStatementResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._imported_date_time_utc

    @imported_date_time_utc.setter
    def imported_date_time_utc(self, imported_date_time_utc):
        """Sets the imported_date_time_utc of this CurrentStatementResponse.

        Looking at the most recent bank statement, this field indicates when the document was imported into Xero.  This date is represented in ISO 8601 format.  # noqa: E501

        :param imported_date_time_utc: The imported_date_time_utc of this CurrentStatementResponse.  # noqa: E501
        :type: datetime
        """

        self._imported_date_time_utc = imported_date_time_utc

    @property
    def import_source_type(self):
        """Gets the import_source_type of this CurrentStatementResponse.  # noqa: E501

        Looking at the most recent bank statement, this field indicates the source of the data (direct bank feed, indirect bank feed, file upload, or manual keying).  # noqa: E501

        :return: The import_source_type of this CurrentStatementResponse.  # noqa: E501
        :rtype: str
        """
        return self._import_source_type

    @import_source_type.setter
    def import_source_type(self, import_source_type):
        """Sets the import_source_type of this CurrentStatementResponse.

        Looking at the most recent bank statement, this field indicates the source of the data (direct bank feed, indirect bank feed, file upload, or manual keying).  # noqa: E501

        :param import_source_type: The import_source_type of this CurrentStatementResponse.  # noqa: E501
        :type: str
        """

        self._import_source_type = import_source_type
