# coding: utf-8

"""
    Xero Payroll AU

    This is the Xero Payroll API for orgs in Australia region.  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class LeaveLines(BaseModel):
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
    openapi_types = {"employee": "list[LeaveLine]"}

    attribute_map = {"employee": "Employee"}

    def __init__(self, employee=None):  # noqa: E501
        """LeaveLines - a model defined in OpenAPI"""  # noqa: E501

        self._employee = None
        self.discriminator = None

        if employee is not None:
            self.employee = employee

    @property
    def employee(self):
        """Gets the employee of this LeaveLines.  # noqa: E501


        :return: The employee of this LeaveLines.  # noqa: E501
        :rtype: list[LeaveLine]
        """
        return self._employee

    @employee.setter
    def employee(self, employee):
        """Sets the employee of this LeaveLines.


        :param employee: The employee of this LeaveLines.  # noqa: E501
        :type: list[LeaveLine]
        """

        self._employee = employee
