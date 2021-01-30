# coding: utf-8

"""
    Xero Payroll UK

    This is the Xero Payroll API for orgs in the UK region.  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class Employment(BaseModel):
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
        "payroll_calendar_id": "str",
        "start_date": "date",
        "employee_number": "str",
        "ni_category": "str",
    }

    attribute_map = {
        "payroll_calendar_id": "payrollCalendarID",
        "start_date": "startDate",
        "employee_number": "employeeNumber",
        "ni_category": "niCategory",
    }

    def __init__(
        self,
        payroll_calendar_id=None,
        start_date=None,
        employee_number=None,
        ni_category=None,
    ):  # noqa: E501
        """Employment - a model defined in OpenAPI"""  # noqa: E501

        self._payroll_calendar_id = None
        self._start_date = None
        self._employee_number = None
        self._ni_category = None
        self.discriminator = None

        if payroll_calendar_id is not None:
            self.payroll_calendar_id = payroll_calendar_id
        if start_date is not None:
            self.start_date = start_date
        if employee_number is not None:
            self.employee_number = employee_number
        if ni_category is not None:
            self.ni_category = ni_category

    @property
    def payroll_calendar_id(self):
        """Gets the payroll_calendar_id of this Employment.  # noqa: E501

        Xero unique identifier for the payroll calendar of the employee  # noqa: E501

        :return: The payroll_calendar_id of this Employment.  # noqa: E501
        :rtype: str
        """
        return self._payroll_calendar_id

    @payroll_calendar_id.setter
    def payroll_calendar_id(self, payroll_calendar_id):
        """Sets the payroll_calendar_id of this Employment.

        Xero unique identifier for the payroll calendar of the employee  # noqa: E501

        :param payroll_calendar_id: The payroll_calendar_id of this Employment.  # noqa: E501
        :type: str
        """

        self._payroll_calendar_id = payroll_calendar_id

    @property
    def start_date(self):
        """Gets the start_date of this Employment.  # noqa: E501

        Start date of the employment (YYYY-MM-DD)  # noqa: E501

        :return: The start_date of this Employment.  # noqa: E501
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this Employment.

        Start date of the employment (YYYY-MM-DD)  # noqa: E501

        :param start_date: The start_date of this Employment.  # noqa: E501
        :type: date
        """

        self._start_date = start_date

    @property
    def employee_number(self):
        """Gets the employee_number of this Employment.  # noqa: E501

        The employment number of the employee  # noqa: E501

        :return: The employee_number of this Employment.  # noqa: E501
        :rtype: str
        """
        return self._employee_number

    @employee_number.setter
    def employee_number(self, employee_number):
        """Sets the employee_number of this Employment.

        The employment number of the employee  # noqa: E501

        :param employee_number: The employee_number of this Employment.  # noqa: E501
        :type: str
        """

        self._employee_number = employee_number

    @property
    def ni_category(self):
        """Gets the ni_category of this Employment.  # noqa: E501

        The NI Category of the employee  # noqa: E501

        :return: The ni_category of this Employment.  # noqa: E501
        :rtype: str
        """
        return self._ni_category

    @ni_category.setter
    def ni_category(self, ni_category):
        """Sets the ni_category of this Employment.

        The NI Category of the employee  # noqa: E501

        :param ni_category: The ni_category of this Employment.  # noqa: E501
        :type: str
        """
        allowed_values = ["A", "B", "C", "H", "J", "M", "Z", "X", "None"]  # noqa: E501

        if ni_category:
            if ni_category not in allowed_values:
                raise ValueError(
                    "Invalid value for `ni_category` ({0}), must be one of {1}".format(  # noqa: E501
                        ni_category, allowed_values
                    )
                )

        self._ni_category = ni_category
