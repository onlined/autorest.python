# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Optional, TypeVar

from msrest import Serializer

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace

from .._vendor import _format_url_section

T = TypeVar("T")
JSONType = Any
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_formdataurlencoded_update_pet_with_form_request(
    pet_id: int, *, data: Optional[Dict[str, Any]] = None, content: Any = None, **kwargs: Any
) -> HttpRequest:
    content_type = kwargs.pop("content_type", None)  # type: Optional[str]

    # Construct URL
    _url = "/formsdataurlencoded/pet/add/{petId}"
    path_format_arguments = {
        "petId": _SERIALIZER.url("pet_id", pet_id, "int"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        _header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="POST", url=_url, headers=_header_parameters, data=data, content=content, **kwargs)


def build_formdataurlencoded_partial_constant_body_request(
    *, data: Optional[Dict[str, Any]] = None, content: Any = None, **kwargs: Any
) -> HttpRequest:
    content_type = kwargs.pop("content_type", None)  # type: Optional[str]

    # Construct URL
    _url = "/formsdataurlencoded/partialConstantBody"

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        _header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="POST", url=_url, headers=_header_parameters, data=data, content=content, **kwargs)


class FormdataurlencodedOperations(object):
    """FormdataurlencodedOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace
    def update_pet_with_form(  # pylint: disable=inconsistent-return-statements
        self, pet_id: int, data: Dict[str, Any], **kwargs: Any
    ) -> None:
        """Updates a pet in the store with form data.

        Updates a pet in the store with form data.

        :param pet_id: ID of pet that needs to be updated.
        :type pet_id: int
        :param data: Form-encoded input for data. See the template in our example to find the input
         shape.
        :type data: dict[str, any]
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # form-encoded input template you can fill out and use as your `data` input.
                data = {
                    "name": "str",  # Optional. Updated name of the pet.
                    "pet_age": 0,  # How many years is it old?.
                    "pet_food": "str",  # Can take a value of meat, or fish, or plant. Possible
                      values are: "meat", "fish", and "plant".
                    "pet_type": "str",  # Can take a value of dog, or cat, or fish. Possible
                      values are: "dog", "cat", and "fish".
                    "status": "str"  # Optional. Updated status of the pet.
                }
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/x-www-form-urlencoded")  # type: Optional[str]

        request = build_formdataurlencoded_update_pet_with_form_request(
            pet_id=pet_id,
            content_type=content_type,
            data=data,
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200, 405]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace
    def partial_constant_body(  # pylint: disable=inconsistent-return-statements
        self, data: Dict[str, Any], **kwargs: Any
    ) -> None:
        """Test a partially constant formdata body. Pass in { grant_type: 'access_token', access_token:
        'foo', service: 'bar' } to pass the test.

        :param data: Form-encoded input for data. See the template in our example to find the input
         shape.
        :type data: dict[str, any]
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # form-encoded input template you can fill out and use as your `data` input.
                data = {
                    "access_token": "str",  # AAD access token, mandatory when grant_type is
                      access_token_refresh_token or access_token.
                    "grant_type": "access_token",  # Default value is "access_token". Constant
                      part of a formdata body. The default value is "access_token". Note that
                      overriding this default value may result in unsupported behavior.
                    "service": "str"  # Indicates the name of your Azure container registry.
                }
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/x-www-form-urlencoded")  # type: Optional[str]

        request = build_formdataurlencoded_partial_constant_body_request(
            content_type=content_type,
            data=data,
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})