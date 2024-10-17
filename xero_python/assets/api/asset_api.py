# coding: utf-8

import importlib
import re  # noqa: F401

from xero_python import exceptions
from xero_python.api_client import ApiClient, ModelFinder

try:
    from .exception_handler import translate_status_exception
except ImportError:
    translate_status_exception = exceptions.translate_status_exception

"""
    Xero Assets API

    The Assets API exposes fixed asset related functions of the Xero Accounting application and can be used for a variety of purposes such as creating assets, retrieving asset valuations etc.  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""

"""
    OpenAPI spec version: 6.3.0
"""


class empty:
    """empty object to mark optional parameter not set"""


class AssetApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    base_url = "https://api.xero.com/assets.xro/1.0"
    models_module = importlib.import_module("xero_python.assets.models")

    def __init__(self, api_client=None, base_url=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.base_url = base_url or self.base_url

    def get_resource_url(self, resource_path):
        """
        Combine API base url with resource specific path
        :param str resource_path: API endpoint specific path
        :return: str full resource path
        """
        return self.base_url + resource_path

    def get_model_finder(self):
        return ModelFinder(self.models_module)

    def create_asset(
        self,
        xero_tenant_id,
        asset,
        idempotency_key=empty,
        _return_http_data_only=True,
        _preload_content=True,
        _request_timeout=None,
    ):
        """adds a fixed asset  # noqa: E501
        OAuth2 scope: assets
        Adds an asset to the system  # noqa: E501
        :param str xero_tenant_id: Xero identifier for Tenant (required)
        :param Asset asset: Fixed asset you are creating (required)
        :param str idempotency_key: This allows you to safely retry requests without the risk of duplicate processing. 128 character max.
        :param bool _return_http_data_only: return received data only
        :param bool _preload_content: load received data in models
        :param bool _request_timeout: maximum wait time for response
        :return: Asset
        """

        # verify the required parameter 'xero_tenant_id' is set
        if xero_tenant_id is None:
            raise ValueError(
                "Missing the required parameter `xero_tenant_id` "
                "when calling `create_asset`"
            )
        # verify the required parameter 'asset' is set
        if asset is None:
            raise ValueError(
                "Missing the required parameter `asset` " "when calling `create_asset`"
            )

        collection_formats = {}
        path_params = {}

        query_params = []

        header_params = {
            "xero-tenant-id": xero_tenant_id,
        }

        if idempotency_key is not empty:
            header_params["Idempotency-Key"] = idempotency_key

        local_var_files = {}
        form_params = []

        body_params = asset
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )

        # HTTP header `Content-Type`
        header_params["Content-Type"] = self.api_client.select_header_content_type(
            ["application/json"]
        )

        # Authentication setting
        auth_settings = ["OAuth2"]
        url = self.get_resource_url("/Assets")

        try:
            return self.api_client.call_api(
                url,
                "POST",
                path_params,
                query_params,
                header_params,
                body=body_params,
                post_params=form_params,
                files=local_var_files,
                response_type="Asset",
                response_model_finder=self.get_model_finder(),
                auth_settings=auth_settings,
                _return_http_data_only=_return_http_data_only,
                _preload_content=_preload_content,
                _request_timeout=_request_timeout,
                collection_formats=collection_formats,
            )
        except exceptions.HTTPStatusException as error:
            raise translate_status_exception(error, self, "create_asset")

    def create_asset_type(
        self,
        xero_tenant_id,
        asset_type,
        idempotency_key=empty,
        _return_http_data_only=True,
        _preload_content=True,
        _request_timeout=None,
    ):
        """adds a fixed asset type  # noqa: E501
        OAuth2 scope: assets
        Adds an fixed asset type to the system  # noqa: E501
        :param str xero_tenant_id: Xero identifier for Tenant (required)
        :param AssetType asset_type: Asset type to add (required)
        :param str idempotency_key: This allows you to safely retry requests without the risk of duplicate processing. 128 character max.
        :param bool _return_http_data_only: return received data only
        :param bool _preload_content: load received data in models
        :param bool _request_timeout: maximum wait time for response
        :return: AssetType
        """

        # verify the required parameter 'xero_tenant_id' is set
        if xero_tenant_id is None:
            raise ValueError(
                "Missing the required parameter `xero_tenant_id` "
                "when calling `create_asset_type`"
            )
        # verify the required parameter 'asset_type' is set
        if asset_type is None:
            raise ValueError(
                "Missing the required parameter `asset_type` "
                "when calling `create_asset_type`"
            )

        collection_formats = {}
        path_params = {}

        query_params = []

        header_params = {
            "xero-tenant-id": xero_tenant_id,
        }

        if idempotency_key is not empty:
            header_params["Idempotency-Key"] = idempotency_key

        local_var_files = {}
        form_params = []

        body_params = asset_type
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )

        # HTTP header `Content-Type`
        header_params["Content-Type"] = self.api_client.select_header_content_type(
            ["application/json"]
        )

        # Authentication setting
        auth_settings = ["OAuth2"]
        url = self.get_resource_url("/AssetTypes")

        try:
            return self.api_client.call_api(
                url,
                "POST",
                path_params,
                query_params,
                header_params,
                body=body_params,
                post_params=form_params,
                files=local_var_files,
                response_type="AssetType",
                response_model_finder=self.get_model_finder(),
                auth_settings=auth_settings,
                _return_http_data_only=_return_http_data_only,
                _preload_content=_preload_content,
                _request_timeout=_request_timeout,
                collection_formats=collection_formats,
            )
        except exceptions.HTTPStatusException as error:
            raise translate_status_exception(error, self, "create_asset_type")

    def get_asset_by_id(
        self,
        xero_tenant_id,
        id,
        _return_http_data_only=True,
        _preload_content=True,
        _request_timeout=None,
    ):
        """Retrieves fixed asset by id  # noqa: E501
        OAuth2 scope: assets, assets.read
        By passing in the appropriate asset id, you can search for a specific fixed asset in the system   # noqa: E501
        :param str xero_tenant_id: Xero identifier for Tenant (required)
        :param str id: fixed asset id for single object (required)
        :param bool _return_http_data_only: return received data only
        :param bool _preload_content: load received data in models
        :param bool _request_timeout: maximum wait time for response
        :return: Asset
        """

        # verify the required parameter 'xero_tenant_id' is set
        if xero_tenant_id is None:
            raise ValueError(
                "Missing the required parameter `xero_tenant_id` "
                "when calling `get_asset_by_id`"
            )
        # verify the required parameter 'id' is set
        if id is None:
            raise ValueError(
                "Missing the required parameter `id` " "when calling `get_asset_by_id`"
            )

        collection_formats = {}
        path_params = {
            "id": id,
        }

        query_params = []

        header_params = {
            "xero-tenant-id": xero_tenant_id,
        }

        local_var_files = {}
        form_params = []

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )

        # Authentication setting
        auth_settings = ["OAuth2"]
        url = self.get_resource_url("/Assets/{id}")

        try:
            return self.api_client.call_api(
                url,
                "GET",
                path_params,
                query_params,
                header_params,
                body=body_params,
                post_params=form_params,
                files=local_var_files,
                response_type="Asset",
                response_model_finder=self.get_model_finder(),
                auth_settings=auth_settings,
                _return_http_data_only=_return_http_data_only,
                _preload_content=_preload_content,
                _request_timeout=_request_timeout,
                collection_formats=collection_formats,
            )
        except exceptions.HTTPStatusException as error:
            raise translate_status_exception(error, self, "get_asset_by_id")

    def get_asset_settings(
        self,
        xero_tenant_id,
        _return_http_data_only=True,
        _preload_content=True,
        _request_timeout=None,
    ):
        """searches fixed asset settings  # noqa: E501
        OAuth2 scope: assets, assets.read
        By passing in the appropriate options, you can search for available fixed asset types in the system  # noqa: E501
        :param str xero_tenant_id: Xero identifier for Tenant (required)
        :param bool _return_http_data_only: return received data only
        :param bool _preload_content: load received data in models
        :param bool _request_timeout: maximum wait time for response
        :return: Setting
        """

        # verify the required parameter 'xero_tenant_id' is set
        if xero_tenant_id is None:
            raise ValueError(
                "Missing the required parameter `xero_tenant_id` "
                "when calling `get_asset_settings`"
            )

        collection_formats = {}
        path_params = {}

        query_params = []

        header_params = {
            "xero-tenant-id": xero_tenant_id,
        }

        local_var_files = {}
        form_params = []

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )

        # Authentication setting
        auth_settings = ["OAuth2"]
        url = self.get_resource_url("/Settings")

        try:
            return self.api_client.call_api(
                url,
                "GET",
                path_params,
                query_params,
                header_params,
                body=body_params,
                post_params=form_params,
                files=local_var_files,
                response_type="Setting",
                response_model_finder=self.get_model_finder(),
                auth_settings=auth_settings,
                _return_http_data_only=_return_http_data_only,
                _preload_content=_preload_content,
                _request_timeout=_request_timeout,
                collection_formats=collection_formats,
            )
        except exceptions.HTTPStatusException as error:
            raise translate_status_exception(error, self, "get_asset_settings")

    def get_asset_types(
        self,
        xero_tenant_id,
        _return_http_data_only=True,
        _preload_content=True,
        _request_timeout=None,
    ):
        """searches fixed asset types  # noqa: E501
        OAuth2 scope: assets, assets.read
        By passing in the appropriate options, you can search for available fixed asset types in the system  # noqa: E501
        :param str xero_tenant_id: Xero identifier for Tenant (required)
        :param bool _return_http_data_only: return received data only
        :param bool _preload_content: load received data in models
        :param bool _request_timeout: maximum wait time for response
        :return: list[AssetType]
        """

        # verify the required parameter 'xero_tenant_id' is set
        if xero_tenant_id is None:
            raise ValueError(
                "Missing the required parameter `xero_tenant_id` "
                "when calling `get_asset_types`"
            )

        collection_formats = {}
        path_params = {}

        query_params = []

        header_params = {
            "xero-tenant-id": xero_tenant_id,
        }

        local_var_files = {}
        form_params = []

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )

        # Authentication setting
        auth_settings = ["OAuth2"]
        url = self.get_resource_url("/AssetTypes")

        try:
            return self.api_client.call_api(
                url,
                "GET",
                path_params,
                query_params,
                header_params,
                body=body_params,
                post_params=form_params,
                files=local_var_files,
                response_type="list[AssetType]",
                response_model_finder=self.get_model_finder(),
                auth_settings=auth_settings,
                _return_http_data_only=_return_http_data_only,
                _preload_content=_preload_content,
                _request_timeout=_request_timeout,
                collection_formats=collection_formats,
            )
        except exceptions.HTTPStatusException as error:
            raise translate_status_exception(error, self, "get_asset_types")

    def get_assets(
        self,
        xero_tenant_id,
        status,
        page=empty,
        page_size=empty,
        order_by=empty,
        sort_direction=empty,
        filter_by=empty,
        _return_http_data_only=True,
        _preload_content=True,
        _request_timeout=None,
    ):
        """searches fixed asset  # noqa: E501
        OAuth2 scope: assets, assets.read
        By passing in the appropriate options, you can search for available fixed asset in the system  # noqa: E501
        :param str xero_tenant_id: Xero identifier for Tenant (required)
        :param AssetStatusQueryParam status: Required when retrieving a collection of assets. See Asset Status Codes (required)
        :param int page: Results are paged. This specifies which page of the results to return. The default page is 1.
        :param int page_size: The number of records returned per page. By default the number of records returned is 10.
        :param str order_by: Requests can be ordered by AssetType, AssetName, AssetNumber, PurchaseDate and PurchasePrice. If the asset status is DISPOSED it also allows DisposalDate and DisposalPrice.
        :param str sort_direction: ASC or DESC
        :param str filter_by: A string that can be used to filter the list to only return assets containing the text. Checks it against the AssetName, AssetNumber, Description and AssetTypeName fields.
        :param bool _return_http_data_only: return received data only
        :param bool _preload_content: load received data in models
        :param bool _request_timeout: maximum wait time for response
        :return: Assets
        """

        # verify the required parameter 'xero_tenant_id' is set
        if xero_tenant_id is None:
            raise ValueError(
                "Missing the required parameter `xero_tenant_id` "
                "when calling `get_assets`"
            )
        # verify the required parameter 'status' is set
        if status is None:
            raise ValueError(
                "Missing the required parameter `status` " "when calling `get_assets`"
            )

        collection_formats = {}
        path_params = {}

        query_params = [
            ("status", status),
        ]

        if page is not empty:
            query_params.append(("page", page))

        if page_size is not empty:
            query_params.append(("pageSize", page_size))

        if order_by is not empty:
            query_params.append(("orderBy", order_by))

        if sort_direction is not empty:
            query_params.append(("sortDirection", sort_direction))

        if filter_by is not empty:
            query_params.append(("filterBy", filter_by))

        header_params = {
            "xero-tenant-id": xero_tenant_id,
        }

        local_var_files = {}
        form_params = []

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )

        # Authentication setting
        auth_settings = ["OAuth2"]
        url = self.get_resource_url("/Assets")

        try:
            return self.api_client.call_api(
                url,
                "GET",
                path_params,
                query_params,
                header_params,
                body=body_params,
                post_params=form_params,
                files=local_var_files,
                response_type="Assets",
                response_model_finder=self.get_model_finder(),
                auth_settings=auth_settings,
                _return_http_data_only=_return_http_data_only,
                _preload_content=_preload_content,
                _request_timeout=_request_timeout,
                collection_formats=collection_formats,
            )
        except exceptions.HTTPStatusException as error:
            raise translate_status_exception(error, self, "get_assets")
