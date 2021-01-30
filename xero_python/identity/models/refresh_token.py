# coding: utf-8

"""
    Xero oAuth 2 identity service

    This specifing endpoints related to managing authentication tokens and identity for Xero API  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class RefreshToken(BaseModel):
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
        "grant_type": "str",
        "refresh_token": "str",
        "client_id": "str",
        "client_secret": "str",
    }

    attribute_map = {
        "grant_type": "grant_type",
        "refresh_token": "refresh_token",
        "client_id": "client_id",
        "client_secret": "client_secret",
    }

    def __init__(
        self, grant_type=None, refresh_token=None, client_id=None, client_secret=None
    ):  # noqa: E501
        """RefreshToken - a model defined in OpenAPI"""  # noqa: E501

        self._grant_type = None
        self._refresh_token = None
        self._client_id = None
        self._client_secret = None
        self.discriminator = None

        if grant_type is not None:
            self.grant_type = grant_type
        if refresh_token is not None:
            self.refresh_token = refresh_token
        if client_id is not None:
            self.client_id = client_id
        if client_secret is not None:
            self.client_secret = client_secret

    @property
    def grant_type(self):
        """Gets the grant_type of this RefreshToken.  # noqa: E501

        Xero grant type  # noqa: E501

        :return: The grant_type of this RefreshToken.  # noqa: E501
        :rtype: str
        """
        return self._grant_type

    @grant_type.setter
    def grant_type(self, grant_type):
        """Sets the grant_type of this RefreshToken.

        Xero grant type  # noqa: E501

        :param grant_type: The grant_type of this RefreshToken.  # noqa: E501
        :type: str
        """

        self._grant_type = grant_type

    @property
    def refresh_token(self):
        """Gets the refresh_token of this RefreshToken.  # noqa: E501

        refresh token provided during authentication flow  # noqa: E501

        :return: The refresh_token of this RefreshToken.  # noqa: E501
        :rtype: str
        """
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, refresh_token):
        """Sets the refresh_token of this RefreshToken.

        refresh token provided during authentication flow  # noqa: E501

        :param refresh_token: The refresh_token of this RefreshToken.  # noqa: E501
        :type: str
        """

        self._refresh_token = refresh_token

    @property
    def client_id(self):
        """Gets the client_id of this RefreshToken.  # noqa: E501

        client id for Xero app  # noqa: E501

        :return: The client_id of this RefreshToken.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this RefreshToken.

        client id for Xero app  # noqa: E501

        :param client_id: The client_id of this RefreshToken.  # noqa: E501
        :type: str
        """

        self._client_id = client_id

    @property
    def client_secret(self):
        """Gets the client_secret of this RefreshToken.  # noqa: E501

        client secret for Xero app 2  # noqa: E501

        :return: The client_secret of this RefreshToken.  # noqa: E501
        :rtype: str
        """
        return self._client_secret

    @client_secret.setter
    def client_secret(self, client_secret):
        """Sets the client_secret of this RefreshToken.

        client secret for Xero app 2  # noqa: E501

        :param client_secret: The client_secret of this RefreshToken.  # noqa: E501
        :type: str
        """

        self._client_secret = client_secret
