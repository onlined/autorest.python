# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Optional

from azure.core.rest import HttpRequest
from msrest import Serializer

_SERIALIZER = Serializer()


def build_put201_creating_succeeded200_request(*, json: Any = None, content: Any = None, **kwargs: Any) -> HttpRequest:
    """Long running put request, service returns a 500, then a 201 to the initial request, with an
    entity that contains ProvisioningState=’Creating’.  Polls return this value until the last poll
    returns a ‘200’ with ProvisioningState=’Succeeded’.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. Product to put.
    :paramtype json: any
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). Product to put.
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your `json` input.
            json = {
                "properties": {
                    "provisioningState": "str (optional)",
                    "provisioningStateValues": "str (optional)"
                }
            }

            # response body for status code(s): 200, 201
            response.json() == {
                "properties": {
                    "provisioningState": "str (optional)",
                    "provisioningStateValues": "str (optional)"
                }
            }
    """

    content_type = kwargs.pop("content_type", None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", "/lro/retryerror/put/201/creating/succeeded/200")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=url, headers=header_parameters, json=json, content=content, **kwargs)


def build_put_async_relative_retry_succeeded_request(
    *, json: Any = None, content: Any = None, **kwargs: Any
) -> HttpRequest:
    """Long running put request, service returns a 500, then a 200 to the initial request, with an
    entity that contains ProvisioningState=’Creating’. Poll the endpoint indicated in the
    Azure-AsyncOperation header for operation status.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. Product to put.
    :paramtype json: any
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). Product to put.
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your `json` input.
            json = {
                "properties": {
                    "provisioningState": "str (optional)",
                    "provisioningStateValues": "str (optional)"
                }
            }

            # response body for status code(s): 200
            response.json() == {
                "properties": {
                    "provisioningState": "str (optional)",
                    "provisioningStateValues": "str (optional)"
                }
            }
    """

    content_type = kwargs.pop("content_type", None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", "/lro/retryerror/putasync/retry/succeeded")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=url, headers=header_parameters, json=json, content=content, **kwargs)


def build_delete_provisioning202_accepted200_succeeded_request(**kwargs: Any) -> HttpRequest:
    """Long running delete request, service returns a 500, then a  202 to the initial request, with an
    entity that contains ProvisioningState=’Accepted’.  Polls return this value until the last poll
    returns a ‘200’ with ProvisioningState=’Succeeded’.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # response body for status code(s): 200, 202
            response.json() == {
                "properties": {
                    "provisioningState": "str (optional)",
                    "provisioningStateValues": "str (optional)"
                }
            }
    """

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", "/lro/retryerror/delete/provisioning/202/accepted/200/succeeded")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="DELETE", url=url, headers=header_parameters, **kwargs)


def build_delete202_retry200_request(**kwargs: Any) -> HttpRequest:
    """Long running delete request, service returns a 500, then a 202 to the initial request. Polls
    return this value until the last poll returns a ‘200’ with ProvisioningState=’Succeeded’.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", "/lro/retryerror/delete/202/retry/200")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="DELETE", url=url, headers=header_parameters, **kwargs)


def build_delete_async_relative_retry_succeeded_request(**kwargs: Any) -> HttpRequest:
    """Long running delete request, service returns a 500, then a 202 to the initial request. Poll the
    endpoint indicated in the Azure-AsyncOperation header for operation status.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", "/lro/retryerror/deleteasync/retry/succeeded")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="DELETE", url=url, headers=header_parameters, **kwargs)


def build_post202_retry200_request(*, json: Any = None, content: Any = None, **kwargs: Any) -> HttpRequest:
    """Long running post request, service returns a 500, then a 202 to the initial request, with
    'Location' and 'Retry-After' headers, Polls return a 200 with a response body after success.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. Product to put.
    :paramtype json: any
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). Product to put.
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your `json` input.
            json = {
                "properties": {
                    "provisioningState": "str (optional)",
                    "provisioningStateValues": "str (optional)"
                }
            }
    """

    content_type = kwargs.pop("content_type", None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", "/lro/retryerror/post/202/retry/200")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=url, headers=header_parameters, json=json, content=content, **kwargs)


def build_post_async_relative_retry_succeeded_request(
    *, json: Any = None, content: Any = None, **kwargs: Any
) -> HttpRequest:
    """Long running post request, service returns a 500, then a 202 to the initial request, with an
    entity that contains ProvisioningState=’Creating’. Poll the endpoint indicated in the
    Azure-AsyncOperation header for operation status.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. Product to put.
    :paramtype json: any
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). Product to put.
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your `json` input.
            json = {
                "properties": {
                    "provisioningState": "str (optional)",
                    "provisioningStateValues": "str (optional)"
                }
            }
    """

    content_type = kwargs.pop("content_type", None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", "/lro/retryerror/postasync/retry/succeeded")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=url, headers=header_parameters, json=json, content=content, **kwargs)