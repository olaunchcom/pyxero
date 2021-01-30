# coding: utf-8

"""
    Xero Payroll AU

    This is the Xero Payroll API for orgs in Australia region.  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class SuperFund(BaseModel):
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
        "super_fund_id": "str",
        "type": "SuperFundType",
        "name": "str",
        "abn": "str",
        "bsb": "str",
        "account_number": "str",
        "account_name": "str",
        "electronic_service_address": "str",
        "employer_number": "str",
        "spin": "str",
        "usi": "str",
        "updated_date_utc": "datetime[ms-format]",
        "validation_errors": "list[ValidationError]",
    }

    attribute_map = {
        "super_fund_id": "SuperFundID",
        "type": "Type",
        "name": "Name",
        "abn": "ABN",
        "bsb": "BSB",
        "account_number": "AccountNumber",
        "account_name": "AccountName",
        "electronic_service_address": "ElectronicServiceAddress",
        "employer_number": "EmployerNumber",
        "spin": "SPIN",
        "usi": "USI",
        "updated_date_utc": "UpdatedDateUTC",
        "validation_errors": "ValidationErrors",
    }

    def __init__(
        self,
        super_fund_id=None,
        type=None,
        name=None,
        abn=None,
        bsb=None,
        account_number=None,
        account_name=None,
        electronic_service_address=None,
        employer_number=None,
        spin=None,
        usi=None,
        updated_date_utc=None,
        validation_errors=None,
    ):  # noqa: E501
        """SuperFund - a model defined in OpenAPI"""  # noqa: E501

        self._super_fund_id = None
        self._type = None
        self._name = None
        self._abn = None
        self._bsb = None
        self._account_number = None
        self._account_name = None
        self._electronic_service_address = None
        self._employer_number = None
        self._spin = None
        self._usi = None
        self._updated_date_utc = None
        self._validation_errors = None
        self.discriminator = None

        if super_fund_id is not None:
            self.super_fund_id = super_fund_id
        self.type = type
        if name is not None:
            self.name = name
        if abn is not None:
            self.abn = abn
        if bsb is not None:
            self.bsb = bsb
        if account_number is not None:
            self.account_number = account_number
        if account_name is not None:
            self.account_name = account_name
        if electronic_service_address is not None:
            self.electronic_service_address = electronic_service_address
        if employer_number is not None:
            self.employer_number = employer_number
        if spin is not None:
            self.spin = spin
        if usi is not None:
            self.usi = usi
        if updated_date_utc is not None:
            self.updated_date_utc = updated_date_utc
        if validation_errors is not None:
            self.validation_errors = validation_errors

    @property
    def super_fund_id(self):
        """Gets the super_fund_id of this SuperFund.  # noqa: E501

        Xero identifier for a super fund  # noqa: E501

        :return: The super_fund_id of this SuperFund.  # noqa: E501
        :rtype: str
        """
        return self._super_fund_id

    @super_fund_id.setter
    def super_fund_id(self, super_fund_id):
        """Sets the super_fund_id of this SuperFund.

        Xero identifier for a super fund  # noqa: E501

        :param super_fund_id: The super_fund_id of this SuperFund.  # noqa: E501
        :type: str
        """

        self._super_fund_id = super_fund_id

    @property
    def type(self):
        """Gets the type of this SuperFund.  # noqa: E501


        :return: The type of this SuperFund.  # noqa: E501
        :rtype: SuperFundType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SuperFund.


        :param type: The type of this SuperFund.  # noqa: E501
        :type: SuperFundType
        """
        if type is None:
            raise ValueError(
                "Invalid value for `type`, must not be `None`"
            )  # noqa: E501

        self._type = type

    @property
    def name(self):
        """Gets the name of this SuperFund.  # noqa: E501

        Name of the super fund  # noqa: E501

        :return: The name of this SuperFund.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SuperFund.

        Name of the super fund  # noqa: E501

        :param name: The name of this SuperFund.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def abn(self):
        """Gets the abn of this SuperFund.  # noqa: E501

        ABN of the self managed super fund  # noqa: E501

        :return: The abn of this SuperFund.  # noqa: E501
        :rtype: str
        """
        return self._abn

    @abn.setter
    def abn(self, abn):
        """Sets the abn of this SuperFund.

        ABN of the self managed super fund  # noqa: E501

        :param abn: The abn of this SuperFund.  # noqa: E501
        :type: str
        """

        self._abn = abn

    @property
    def bsb(self):
        """Gets the bsb of this SuperFund.  # noqa: E501

        BSB of the self managed super fund  # noqa: E501

        :return: The bsb of this SuperFund.  # noqa: E501
        :rtype: str
        """
        return self._bsb

    @bsb.setter
    def bsb(self, bsb):
        """Sets the bsb of this SuperFund.

        BSB of the self managed super fund  # noqa: E501

        :param bsb: The bsb of this SuperFund.  # noqa: E501
        :type: str
        """

        self._bsb = bsb

    @property
    def account_number(self):
        """Gets the account_number of this SuperFund.  # noqa: E501

        The account number for the self managed super fund.  # noqa: E501

        :return: The account_number of this SuperFund.  # noqa: E501
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this SuperFund.

        The account number for the self managed super fund.  # noqa: E501

        :param account_number: The account_number of this SuperFund.  # noqa: E501
        :type: str
        """

        self._account_number = account_number

    @property
    def account_name(self):
        """Gets the account_name of this SuperFund.  # noqa: E501

        The account name for the self managed super fund.  # noqa: E501

        :return: The account_name of this SuperFund.  # noqa: E501
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this SuperFund.

        The account name for the self managed super fund.  # noqa: E501

        :param account_name: The account_name of this SuperFund.  # noqa: E501
        :type: str
        """

        self._account_name = account_name

    @property
    def electronic_service_address(self):
        """Gets the electronic_service_address of this SuperFund.  # noqa: E501

        The electronic service address for the self managed super fund.  # noqa: E501

        :return: The electronic_service_address of this SuperFund.  # noqa: E501
        :rtype: str
        """
        return self._electronic_service_address

    @electronic_service_address.setter
    def electronic_service_address(self, electronic_service_address):
        """Sets the electronic_service_address of this SuperFund.

        The electronic service address for the self managed super fund.  # noqa: E501

        :param electronic_service_address: The electronic_service_address of this SuperFund.  # noqa: E501
        :type: str
        """

        self._electronic_service_address = electronic_service_address

    @property
    def employer_number(self):
        """Gets the employer_number of this SuperFund.  # noqa: E501

        Some funds assign a unique number to each employer  # noqa: E501

        :return: The employer_number of this SuperFund.  # noqa: E501
        :rtype: str
        """
        return self._employer_number

    @employer_number.setter
    def employer_number(self, employer_number):
        """Sets the employer_number of this SuperFund.

        Some funds assign a unique number to each employer  # noqa: E501

        :param employer_number: The employer_number of this SuperFund.  # noqa: E501
        :type: str
        """

        self._employer_number = employer_number

    @property
    def spin(self):
        """Gets the spin of this SuperFund.  # noqa: E501

        The SPIN of the Regulated SuperFund. This field has been deprecated. It will only be present for legacy superfunds. New superfunds will not have a SPIN value. The USI field should be used instead of SPIN.  # noqa: E501

        :return: The spin of this SuperFund.  # noqa: E501
        :rtype: str
        """
        return self._spin

    @spin.setter
    def spin(self, spin):
        """Sets the spin of this SuperFund.

        The SPIN of the Regulated SuperFund. This field has been deprecated. It will only be present for legacy superfunds. New superfunds will not have a SPIN value. The USI field should be used instead of SPIN.  # noqa: E501

        :param spin: The spin of this SuperFund.  # noqa: E501
        :type: str
        """

        self._spin = spin

    @property
    def usi(self):
        """Gets the usi of this SuperFund.  # noqa: E501

        The USI of the Regulated SuperFund  # noqa: E501

        :return: The usi of this SuperFund.  # noqa: E501
        :rtype: str
        """
        return self._usi

    @usi.setter
    def usi(self, usi):
        """Sets the usi of this SuperFund.

        The USI of the Regulated SuperFund  # noqa: E501

        :param usi: The usi of this SuperFund.  # noqa: E501
        :type: str
        """

        self._usi = usi

    @property
    def updated_date_utc(self):
        """Gets the updated_date_utc of this SuperFund.  # noqa: E501

        Last modified timestamp  # noqa: E501

        :return: The updated_date_utc of this SuperFund.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_date_utc

    @updated_date_utc.setter
    def updated_date_utc(self, updated_date_utc):
        """Sets the updated_date_utc of this SuperFund.

        Last modified timestamp  # noqa: E501

        :param updated_date_utc: The updated_date_utc of this SuperFund.  # noqa: E501
        :type: datetime
        """

        self._updated_date_utc = updated_date_utc

    @property
    def validation_errors(self):
        """Gets the validation_errors of this SuperFund.  # noqa: E501

        Displays array of validation error messages from the API  # noqa: E501

        :return: The validation_errors of this SuperFund.  # noqa: E501
        :rtype: list[ValidationError]
        """
        return self._validation_errors

    @validation_errors.setter
    def validation_errors(self, validation_errors):
        """Sets the validation_errors of this SuperFund.

        Displays array of validation error messages from the API  # noqa: E501

        :param validation_errors: The validation_errors of this SuperFund.  # noqa: E501
        :type: list[ValidationError]
        """

        self._validation_errors = validation_errors
