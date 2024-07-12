# coding: utf-8

"""
    Xero AppStore API

    These endpoints are for Xero Partners to interact with the App Store Billing platform  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""

"""
    OpenAPI spec version: 6.0.0
"""

import importlib
import re  # noqa: F401

from xero_python import exceptions
from xero_python.api_client import ApiClient, ModelFinder

try:
    from .exception_handler import translate_status_exception
except ImportError:
    translate_status_exception = exceptions.translate_status_exception


class empty:
    """empty object to mark optional parameter not set"""


class AppStoreApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    base_url = "https://api.xero.com/appstore/2.0"
    models_module = importlib.import_module("xero_python.appstore.models")

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

    def get_subscription(
        self,
        subscription_id,
        _return_http_data_only=True,
        _preload_content=True,
        _request_timeout=None,
    ):
        """Retrieves a subscription for a given subscriptionId  # noqa: E501
        OAuth2 scope: marketplace.billing
        :param str subscription_id: Unique identifier for Subscription object (required)
        :param bool _return_http_data_only: return received data only
        :param bool _preload_content: load received data in models
        :param bool _request_timeout: maximum wait time for response
        :return: Subscription
        """

        # verify the required parameter 'subscription_id' is set
        if subscription_id is None:
            raise ValueError(
                "Missing the required parameter `subscription_id` "
                "when calling `get_subscription`"
            )

        collection_formats = {}
        path_params = {
            "subscriptionId": subscription_id,
        }

        query_params = []

        header_params = {}

        local_var_files = {}
        form_params = []

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )

        # Authentication setting
        auth_settings = ["OAuth2"]
        url = self.get_resource_url("/subscriptions/{subscriptionId}")

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
                response_type="Subscription",
                response_model_finder=self.get_model_finder(),
                auth_settings=auth_settings,
                _return_http_data_only=_return_http_data_only,
                _preload_content=_preload_content,
                _request_timeout=_request_timeout,
                collection_formats=collection_formats,
            )
        except exceptions.HTTPStatusException as error:
            raise translate_status_exception(error, self, "get_subscription")

    def get_usage_records(
        self,
        subscription_id,
        _return_http_data_only=True,
        _preload_content=True,
        _request_timeout=None,
    ):
        """Gets all usage records related to the subscription  # noqa: E501
        OAuth2 scope: marketplace.billing
        :param str subscription_id: Unique identifier for Subscription object (required)
        :param bool _return_http_data_only: return received data only
        :param bool _preload_content: load received data in models
        :param bool _request_timeout: maximum wait time for response
        :return: UsageRecordsList
        """

        # verify the required parameter 'subscription_id' is set
        if subscription_id is None:
            raise ValueError(
                "Missing the required parameter `subscription_id` "
                "when calling `get_usage_records`"
            )

        collection_formats = {}
        path_params = {
            "subscriptionId": subscription_id,
        }

        query_params = []

        header_params = {}

        local_var_files = {}
        form_params = []

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )

        # Authentication setting
        auth_settings = ["OAuth2"]
        url = self.get_resource_url("/subscriptions/{subscriptionId}/usage-records")

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
                response_type="UsageRecordsList",
                response_model_finder=self.get_model_finder(),
                auth_settings=auth_settings,
                _return_http_data_only=_return_http_data_only,
                _preload_content=_preload_content,
                _request_timeout=_request_timeout,
                collection_formats=collection_formats,
            )
        except exceptions.HTTPStatusException as error:
            raise translate_status_exception(error, self, "get_usage_records")

    def post_usage_records(
        self,
        subscription_id,
        subscription_item_id,
        create_usage_record,
        idempotency_key=empty,
        _return_http_data_only=True,
        _preload_content=True,
        _request_timeout=None,
    ):
        """Send metered usage belonging to this subscription and subscription item  # noqa: E501
        OAuth2 scope: marketplace.billing
        :param str subscription_id: Unique identifier for Subscription object (required)
        :param str subscription_item_id: The unique identifier of the subscriptionItem (required)
        :param CreateUsageRecord create_usage_record: Contains the quantity for the usage record to create (required)
        :param str idempotency_key: This allows you to safely retry requests without the risk of duplicate processing. 128 character max.
        :param bool _return_http_data_only: return received data only
        :param bool _preload_content: load received data in models
        :param bool _request_timeout: maximum wait time for response
        :return: UsageRecord
        """

        # verify the required parameter 'subscription_id' is set
        if subscription_id is None:
            raise ValueError(
                "Missing the required parameter `subscription_id` "
                "when calling `post_usage_records`"
            )
        # verify the required parameter 'subscription_item_id' is set
        if subscription_item_id is None:
            raise ValueError(
                "Missing the required parameter `subscription_item_id` "
                "when calling `post_usage_records`"
            )
        # verify the required parameter 'create_usage_record' is set
        if create_usage_record is None:
            raise ValueError(
                "Missing the required parameter `create_usage_record` "
                "when calling `post_usage_records`"
            )

        collection_formats = {}
        path_params = {
            "subscriptionId": subscription_id,
            "subscriptionItemId": subscription_item_id,
        }

        query_params = []

        header_params = {}

        if idempotency_key is not empty:
            header_params["Idempotency-Key"] = idempotency_key

        local_var_files = {}
        form_params = []

        body_params = create_usage_record
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
        url = self.get_resource_url(
            "/subscriptions/{subscriptionId}/items/{subscriptionItemId}/usage-records"
        )

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
                response_type="UsageRecord",
                response_model_finder=self.get_model_finder(),
                auth_settings=auth_settings,
                _return_http_data_only=_return_http_data_only,
                _preload_content=_preload_content,
                _request_timeout=_request_timeout,
                collection_formats=collection_formats,
            )
        except exceptions.HTTPStatusException as error:
            raise translate_status_exception(error, self, "post_usage_records")

    def put_usage_records(
        self,
        subscription_id,
        subscription_item_id,
        usage_record_id,
        update_usage_record,
        idempotency_key=empty,
        _return_http_data_only=True,
        _preload_content=True,
        _request_timeout=None,
    ):
        """Update and existing metered usage belonging to this subscription and subscription item  # noqa: E501
        OAuth2 scope: marketplace.billing
        :param str subscription_id: Unique identifier for Subscription object (required)
        :param str subscription_item_id: The unique identifier of the subscriptionItem (required)
        :param str usage_record_id: The unique identifier of the usage record (required)
        :param UpdateUsageRecord update_usage_record: Contains the quantity for the usage record to update (required)
        :param str idempotency_key: This allows you to safely retry requests without the risk of duplicate processing. 128 character max.
        :param bool _return_http_data_only: return received data only
        :param bool _preload_content: load received data in models
        :param bool _request_timeout: maximum wait time for response
        :return: UsageRecord
        """

        # verify the required parameter 'subscription_id' is set
        if subscription_id is None:
            raise ValueError(
                "Missing the required parameter `subscription_id` "
                "when calling `put_usage_records`"
            )
        # verify the required parameter 'subscription_item_id' is set
        if subscription_item_id is None:
            raise ValueError(
                "Missing the required parameter `subscription_item_id` "
                "when calling `put_usage_records`"
            )
        # verify the required parameter 'usage_record_id' is set
        if usage_record_id is None:
            raise ValueError(
                "Missing the required parameter `usage_record_id` "
                "when calling `put_usage_records`"
            )
        # verify the required parameter 'update_usage_record' is set
        if update_usage_record is None:
            raise ValueError(
                "Missing the required parameter `update_usage_record` "
                "when calling `put_usage_records`"
            )

        collection_formats = {}
        path_params = {
            "subscriptionId": subscription_id,
            "subscriptionItemId": subscription_item_id,
            "usageRecordId": usage_record_id,
        }

        query_params = []

        header_params = {}

        if idempotency_key is not empty:
            header_params["Idempotency-Key"] = idempotency_key

        local_var_files = {}
        form_params = []

        body_params = update_usage_record
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
        url = self.get_resource_url(
            "/subscriptions/{subscriptionId}/items/{subscriptionItemId}/usage-records/{usageRecordId}"
        )

        try:
            return self.api_client.call_api(
                url,
                "PUT",
                path_params,
                query_params,
                header_params,
                body=body_params,
                post_params=form_params,
                files=local_var_files,
                response_type="UsageRecord",
                response_model_finder=self.get_model_finder(),
                auth_settings=auth_settings,
                _return_http_data_only=_return_http_data_only,
                _preload_content=_preload_content,
                _request_timeout=_request_timeout,
                collection_formats=collection_formats,
            )
        except exceptions.HTTPStatusException as error:
            raise translate_status_exception(error, self, "put_usage_records")
