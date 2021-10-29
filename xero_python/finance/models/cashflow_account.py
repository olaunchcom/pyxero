# coding: utf-8

"""
    Xero Finance API

    The Finance API is a collection of endpoints which customers can use in the course of a loan application, which may assist lenders to gain the confidence they need to provide capital.  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class CashflowAccount(BaseModel):
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
        "account_id": "str",
        "account_type": "str",
        "account_class": "str",
        "code": "str",
        "name": "str",
        "reporting_code": "str",
        "total": "float",
    }

    attribute_map = {
        "account_id": "accountId",
        "account_type": "accountType",
        "account_class": "accountClass",
        "code": "code",
        "name": "name",
        "reporting_code": "reportingCode",
        "total": "total",
    }

    def __init__(
        self,
        account_id=None,
        account_type=None,
        account_class=None,
        code=None,
        name=None,
        reporting_code=None,
        total=None,
    ):  # noqa: E501
        """CashflowAccount - a model defined in OpenAPI"""  # noqa: E501

        self._account_id = None
        self._account_type = None
        self._account_class = None
        self._code = None
        self._name = None
        self._reporting_code = None
        self._total = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if account_type is not None:
            self.account_type = account_type
        if account_class is not None:
            self.account_class = account_class
        if code is not None:
            self.code = code
        if name is not None:
            self.name = name
        if reporting_code is not None:
            self.reporting_code = reporting_code
        if total is not None:
            self.total = total

    @property
    def account_id(self):
        """Gets the account_id of this CashflowAccount.  # noqa: E501

        ID of the account  # noqa: E501

        :return: The account_id of this CashflowAccount.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this CashflowAccount.

        ID of the account  # noqa: E501

        :param account_id: The account_id of this CashflowAccount.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def account_type(self):
        """Gets the account_type of this CashflowAccount.  # noqa: E501

        The type of the account. See <a href='https://developer.xero.com/documentation/api/types#AccountTypes'>Account Types</a>  # noqa: E501

        :return: The account_type of this CashflowAccount.  # noqa: E501
        :rtype: str
        """
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        """Sets the account_type of this CashflowAccount.

        The type of the account. See <a href='https://developer.xero.com/documentation/api/types#AccountTypes'>Account Types</a>  # noqa: E501

        :param account_type: The account_type of this CashflowAccount.  # noqa: E501
        :type: str
        """

        self._account_type = account_type

    @property
    def account_class(self):
        """Gets the account_class of this CashflowAccount.  # noqa: E501

        The class of the account. See <a href='https://developer.xero.com/documentation/api/types#AccountClassTypes'>Account Class Types</a>  # noqa: E501

        :return: The account_class of this CashflowAccount.  # noqa: E501
        :rtype: str
        """
        return self._account_class

    @account_class.setter
    def account_class(self, account_class):
        """Sets the account_class of this CashflowAccount.

        The class of the account. See <a href='https://developer.xero.com/documentation/api/types#AccountClassTypes'>Account Class Types</a>  # noqa: E501

        :param account_class: The account_class of this CashflowAccount.  # noqa: E501
        :type: str
        """

        self._account_class = account_class

    @property
    def code(self):
        """Gets the code of this CashflowAccount.  # noqa: E501

        Account code  # noqa: E501

        :return: The code of this CashflowAccount.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this CashflowAccount.

        Account code  # noqa: E501

        :param code: The code of this CashflowAccount.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def name(self):
        """Gets the name of this CashflowAccount.  # noqa: E501

        Account name  # noqa: E501

        :return: The name of this CashflowAccount.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CashflowAccount.

        Account name  # noqa: E501

        :param name: The name of this CashflowAccount.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def reporting_code(self):
        """Gets the reporting_code of this CashflowAccount.  # noqa: E501

        Reporting code used for cash flow classification  # noqa: E501

        :return: The reporting_code of this CashflowAccount.  # noqa: E501
        :rtype: str
        """
        return self._reporting_code

    @reporting_code.setter
    def reporting_code(self, reporting_code):
        """Sets the reporting_code of this CashflowAccount.

        Reporting code used for cash flow classification  # noqa: E501

        :param reporting_code: The reporting_code of this CashflowAccount.  # noqa: E501
        :type: str
        """

        self._reporting_code = reporting_code

    @property
    def total(self):
        """Gets the total of this CashflowAccount.  # noqa: E501

        Total amount for the account  # noqa: E501

        :return: The total of this CashflowAccount.  # noqa: E501
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this CashflowAccount.

        Total amount for the account  # noqa: E501

        :param total: The total of this CashflowAccount.  # noqa: E501
        :type: float
        """

        self._total = total
