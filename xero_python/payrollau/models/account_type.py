# coding: utf-8

"""
    Xero Payroll AU

    This is the Xero Payroll API for orgs in Australia region.  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from enum import Enum


class AccountType(Enum):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    allowed enum values
    """

    BANK = "BANK"
    CURRENT = "CURRENT"
    CURRLIAB = "CURRLIAB"
    DEPRECIATN = "DEPRECIATN"
    DIRECTCOSTS = "DIRECTCOSTS"
    EQUITY = "EQUITY"
    EXPENSE = "EXPENSE"
    FIXED = "FIXED"
    INVENTORY = "INVENTORY"
    LIABILITY = "LIABILITY"
    NONCURRENT = "NONCURRENT"
    OTHERINCOME = "OTHERINCOME"
    OVERHEADS = "OVERHEADS"
    PREPAYMENT = "PREPAYMENT"
    REVENUE = "REVENUE"
    SALES = "SALES"
    TERMLIAB = "TERMLIAB"
    PAYGLIABILITY = "PAYGLIABILITY"
    PAYG = "PAYG"
    SUPERANNUATIONEXPENSE = "SUPERANNUATIONEXPENSE"
    SUPERANNUATIONLIABILITY = "SUPERANNUATIONLIABILITY"
    WAGESEXPENSE = "WAGESEXPENSE"
    WAGESPAYABLELIABILITY = "WAGESPAYABLELIABILITY"
