# coding: utf-8

"""
    Accounting API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class Employee(BaseModel):
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
        "employee_id": "str",
        "status": "str",
        "first_name": "str",
        "last_name": "str",
        "external_link": "ExternalLink",
        "updated_date_utc": "datetime[ms-format]",
        "status_attribute_string": "str",
        "validation_errors": "list[ValidationError]",
    }

    attribute_map = {
        "employee_id": "EmployeeID",
        "status": "Status",
        "first_name": "FirstName",
        "last_name": "LastName",
        "external_link": "ExternalLink",
        "updated_date_utc": "UpdatedDateUTC",
        "status_attribute_string": "StatusAttributeString",
        "validation_errors": "ValidationErrors",
    }

    def __init__(
        self,
        employee_id=None,
        status=None,
        first_name=None,
        last_name=None,
        external_link=None,
        updated_date_utc=None,
        status_attribute_string=None,
        validation_errors=None,
    ):  # noqa: E501
        """Employee - a model defined in OpenAPI"""  # noqa: E501

        self._employee_id = None
        self._status = None
        self._first_name = None
        self._last_name = None
        self._external_link = None
        self._updated_date_utc = None
        self._status_attribute_string = None
        self._validation_errors = None
        self.discriminator = None

        if employee_id is not None:
            self.employee_id = employee_id
        if status is not None:
            self.status = status
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if external_link is not None:
            self.external_link = external_link
        if updated_date_utc is not None:
            self.updated_date_utc = updated_date_utc
        if status_attribute_string is not None:
            self.status_attribute_string = status_attribute_string
        if validation_errors is not None:
            self.validation_errors = validation_errors

    @property
    def employee_id(self):
        """Gets the employee_id of this Employee.  # noqa: E501

        The Xero identifier for an employee e.g. 297c2dc5-cc47-4afd-8ec8-74990b8761e9  # noqa: E501

        :return: The employee_id of this Employee.  # noqa: E501
        :rtype: str
        """
        return self._employee_id

    @employee_id.setter
    def employee_id(self, employee_id):
        """Sets the employee_id of this Employee.

        The Xero identifier for an employee e.g. 297c2dc5-cc47-4afd-8ec8-74990b8761e9  # noqa: E501

        :param employee_id: The employee_id of this Employee.  # noqa: E501
        :type: str
        """

        self._employee_id = employee_id

    @property
    def status(self):
        """Gets the status of this Employee.  # noqa: E501

        Current status of an employee – see contact status types  # noqa: E501

        :return: The status of this Employee.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Employee.

        Current status of an employee – see contact status types  # noqa: E501

        :param status: The status of this Employee.  # noqa: E501
        :type: str
        """
        allowed_values = [
            "ACTIVE",
            "ARCHIVED",
            "GDPRREQUEST",
            "DELETED",
            "None",
        ]  # noqa: E501

        if status:
            if status not in allowed_values:
                raise ValueError(
                    "Invalid value for `status` ({0}), must be one of {1}".format(  # noqa: E501
                        status, allowed_values
                    )
                )

        self._status = status

    @property
    def first_name(self):
        """Gets the first_name of this Employee.  # noqa: E501

        First name of an employee (max length = 255)  # noqa: E501

        :return: The first_name of this Employee.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this Employee.

        First name of an employee (max length = 255)  # noqa: E501

        :param first_name: The first_name of this Employee.  # noqa: E501
        :type: str
        """
        if first_name is not None and len(first_name) > 255:
            raise ValueError(
                "Invalid value for `first_name`, "
                "length must be less than or equal to `255`"
            )  # noqa: E501

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this Employee.  # noqa: E501

        Last name of an employee (max length = 255)  # noqa: E501

        :return: The last_name of this Employee.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this Employee.

        Last name of an employee (max length = 255)  # noqa: E501

        :param last_name: The last_name of this Employee.  # noqa: E501
        :type: str
        """
        if last_name is not None and len(last_name) > 255:
            raise ValueError(
                "Invalid value for `last_name`, "
                "length must be less than or equal to `255`"
            )  # noqa: E501

        self._last_name = last_name

    @property
    def external_link(self):
        """Gets the external_link of this Employee.  # noqa: E501


        :return: The external_link of this Employee.  # noqa: E501
        :rtype: ExternalLink
        """
        return self._external_link

    @external_link.setter
    def external_link(self, external_link):
        """Sets the external_link of this Employee.


        :param external_link: The external_link of this Employee.  # noqa: E501
        :type: ExternalLink
        """

        self._external_link = external_link

    @property
    def updated_date_utc(self):
        """Gets the updated_date_utc of this Employee.  # noqa: E501


        :return: The updated_date_utc of this Employee.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_date_utc

    @updated_date_utc.setter
    def updated_date_utc(self, updated_date_utc):
        """Sets the updated_date_utc of this Employee.


        :param updated_date_utc: The updated_date_utc of this Employee.  # noqa: E501
        :type: datetime
        """

        self._updated_date_utc = updated_date_utc

    @property
    def status_attribute_string(self):
        """Gets the status_attribute_string of this Employee.  # noqa: E501

        A string to indicate if a invoice status  # noqa: E501

        :return: The status_attribute_string of this Employee.  # noqa: E501
        :rtype: str
        """
        return self._status_attribute_string

    @status_attribute_string.setter
    def status_attribute_string(self, status_attribute_string):
        """Sets the status_attribute_string of this Employee.

        A string to indicate if a invoice status  # noqa: E501

        :param status_attribute_string: The status_attribute_string of this Employee.  # noqa: E501
        :type: str
        """

        self._status_attribute_string = status_attribute_string

    @property
    def validation_errors(self):
        """Gets the validation_errors of this Employee.  # noqa: E501

        Displays array of validation error messages from the API  # noqa: E501

        :return: The validation_errors of this Employee.  # noqa: E501
        :rtype: list[ValidationError]
        """
        return self._validation_errors

    @validation_errors.setter
    def validation_errors(self, validation_errors):
        """Sets the validation_errors of this Employee.

        Displays array of validation error messages from the API  # noqa: E501

        :param validation_errors: The validation_errors of this Employee.  # noqa: E501
        :type: list[ValidationError]
        """

        self._validation_errors = validation_errors
