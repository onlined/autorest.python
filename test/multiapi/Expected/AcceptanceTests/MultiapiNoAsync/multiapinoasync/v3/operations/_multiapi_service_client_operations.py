# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Optional, TYPE_CHECKING

from msrest import Serializer

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models
from .._vendor import _convert_request

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Iterable, Optional, TypeVar
    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False
# fmt: off

def build_test_paging_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/multiapi/paging")

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_test_different_calls_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop('api_version', _params.pop('api-version', "3.0.0"))  # type: str
    greeting_in_english = kwargs.pop('greeting_in_english')  # type: str
    greeting_in_chinese = kwargs.pop('greeting_in_chinese', _headers.pop('greetingInChinese', None))  # type: Optional[str]
    greeting_in_french = kwargs.pop('greeting_in_french', _headers.pop('greetingInFrench', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/multiapi/testDifferentCalls")

    # Construct parameters
    _params['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    _headers['greetingInEnglish'] = _SERIALIZER.header("greeting_in_english", greeting_in_english, 'str')
    if greeting_in_chinese is not None:
        _headers['greetingInChinese'] = _SERIALIZER.header("greeting_in_chinese", greeting_in_chinese, 'str')
    if greeting_in_french is not None:
        _headers['greetingInFrench'] = _SERIALIZER.header("greeting_in_french", greeting_in_french, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_params,
        headers=_headers,
        **kwargs
    )

# fmt: on
class MultiapiServiceClientOperationsMixin(object):

    @distributed_trace
    def test_paging(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["_models.ModelThree"]
        """Returns ModelThree with optionalProperty 'paged'.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either ModelThree or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~multiapinoasync.v3.models.ModelThree]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop('cls', None)  # type: ClsType[_models.PagingResult]

        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_test_paging_request(
                    template_url=self.test_paging.metadata['url'],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore

            else:
                
                request = build_test_paging_request(
                    template_url=next_link,
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("PagingResult", pipeline_response)
            list_of_elem = deserialized.values
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
                request,
                stream=False,
                **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response


        return ItemPaged(
            get_next, extract_data
        )
    test_paging.metadata = {'url': "/multiapi/paging"}  # type: ignore

    @distributed_trace
    def test_different_calls(  # pylint: disable=inconsistent-return-statements
        self,
        greeting_in_english,  # type: str
        greeting_in_chinese=None,  # type: Optional[str]
        greeting_in_french=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Has added parameters across the API versions.

        :param greeting_in_english: pass in 'hello' to pass test. Required.
        :type greeting_in_english: str
        :param greeting_in_chinese: pass in 'nihao' to pass test. Default value is None.
        :type greeting_in_chinese: str
        :param greeting_in_french: pass in 'bonjour' to pass test. Default value is None.
        :type greeting_in_french: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "3.0.0"))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[None]

        
        request = build_test_different_calls_request(
            greeting_in_english=greeting_in_english,
            greeting_in_chinese=greeting_in_chinese,
            greeting_in_french=greeting_in_french,
            api_version=api_version,
            template_url=self.test_different_calls.metadata['url'],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    test_different_calls.metadata = {'url': "/multiapi/testDifferentCalls"}  # type: ignore

