# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import abc
from typing import Any, Callable, Dict, IO, Iterator, Optional, TypeVar, cast

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
from azure.core.utils import case_insensitive_dict

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_formdata_upload_file_request(*args, **kwargs) -> HttpRequest:
    raise NotImplementedError(
        "You need to write a custom operation for 'build_formdata_upload_file_request'. "
        "Please refer to https://aka.ms/azsdk/python/dpcodegen/python/customize to learn how to customize."
    )


def build_formdata_upload_file_via_body_request(*, content: IO, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
    accept = _headers.pop("Accept", "application/octet-stream, application/json")

    # Construct URL
    _url = "/formdata/stream/uploadfile"

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, headers=_headers, content=content, **kwargs)


def build_formdata_upload_files_request(*args, **kwargs) -> HttpRequest:
    raise NotImplementedError(
        "You need to write a custom operation for 'build_formdata_upload_files_request'. "
        "Please refer to https://aka.ms/azsdk/python/dpcodegen/python/customize to learn how to customize."
    )


class FormdataOperations(abc.ABC):
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~bodyformdataversiontolerant.AutoRestSwaggerBATFormDataService`'s
        :attr:`formdata` attribute.
    """

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    @abc.abstractmethod
    def upload_file(self, *args, **kwargs) -> Iterator[bytes]:
        """You need to write a custom operation for "upload_file". Please refer to
        https://aka.ms/azsdk/python/dpcodegen/python/customize to learn how to customize.

        """

    @distributed_trace
    def upload_file_via_body(self, file_content: IO, **kwargs: Any) -> Iterator[bytes]:
        """Upload file.

        :param file_content: File to upload. Required.
        :type file_content: IO
        :return: Iterator of the response bytes
        :rtype: Iterator[bytes]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", "application/octet-stream"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[Iterator[bytes]]

        _content = file_content

        request = build_formdata_upload_file_via_body_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=True, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = response.iter_bytes()

        if cls:
            return cls(pipeline_response, cast(Iterator[bytes], deserialized), {})

        return cast(Iterator[bytes], deserialized)

    @distributed_trace
    @abc.abstractmethod
    def upload_files(self, *args, **kwargs) -> Iterator[bytes]:
        """You need to write a custom operation for "upload_files". Please refer to
        https://aka.ms/azsdk/python/dpcodegen/python/customize to learn how to customize.

        """
