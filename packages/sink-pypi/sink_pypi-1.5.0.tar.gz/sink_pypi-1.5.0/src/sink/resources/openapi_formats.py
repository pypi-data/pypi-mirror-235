# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional

from ..types import (
    OpenapiFormatArrayTypeOneEntryResponse,
    OpenapiFormatArrayTypeOneEntryWithNullResponse,
    openapi_format_array_type_one_entry_params,
    openapi_format_array_type_one_entry_with_null_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from .._base_client import make_request_options

__all__ = ["OpenapiFormats", "AsyncOpenapiFormats"]


class OpenapiFormats(SyncAPIResource):
    def array_type_one_entry(
        self,
        *,
        enable_debug_logging: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> OpenapiFormatArrayTypeOneEntryResponse:
        """
        See https://linear.app/stainless/issue/STA-569/support-for-type-[object-null]

        Args:
          enable_debug_logging

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/openapi_formats/array_type_one_entry",
            body=maybe_transform(
                {"enable_debug_logging": enable_debug_logging},
                openapi_format_array_type_one_entry_params.OpenapiFormatArrayTypeOneEntryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=OpenapiFormatArrayTypeOneEntryResponse,
        )

    def array_type_one_entry_with_null(
        self,
        *,
        enable_debug_logging: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Optional[OpenapiFormatArrayTypeOneEntryWithNullResponse]:
        """
        The `type` property being set to [T, null] should result in an optional response
        return type in generated SDKs.

        See https://linear.app/stainless/issue/STA-569/support-for-type-[object-null]

        Args:
          enable_debug_logging

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/openapi_formats/array_type_one_entry_with_null",
            body=maybe_transform(
                {"enable_debug_logging": enable_debug_logging},
                openapi_format_array_type_one_entry_with_null_params.OpenapiFormatArrayTypeOneEntryWithNullParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=OpenapiFormatArrayTypeOneEntryWithNullResponse,
        )


class AsyncOpenapiFormats(AsyncAPIResource):
    async def array_type_one_entry(
        self,
        *,
        enable_debug_logging: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> OpenapiFormatArrayTypeOneEntryResponse:
        """
        See https://linear.app/stainless/issue/STA-569/support-for-type-[object-null]

        Args:
          enable_debug_logging

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/openapi_formats/array_type_one_entry",
            body=maybe_transform(
                {"enable_debug_logging": enable_debug_logging},
                openapi_format_array_type_one_entry_params.OpenapiFormatArrayTypeOneEntryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=OpenapiFormatArrayTypeOneEntryResponse,
        )

    async def array_type_one_entry_with_null(
        self,
        *,
        enable_debug_logging: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Optional[OpenapiFormatArrayTypeOneEntryWithNullResponse]:
        """
        The `type` property being set to [T, null] should result in an optional response
        return type in generated SDKs.

        See https://linear.app/stainless/issue/STA-569/support-for-type-[object-null]

        Args:
          enable_debug_logging

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/openapi_formats/array_type_one_entry_with_null",
            body=maybe_transform(
                {"enable_debug_logging": enable_debug_logging},
                openapi_format_array_type_one_entry_with_null_params.OpenapiFormatArrayTypeOneEntryWithNullParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=OpenapiFormatArrayTypeOneEntryWithNullResponse,
        )
