# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING

from azure.core.rest import HttpRequest
from msrest import Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

_SERIALIZER = Serializer()

# fmt: off

def build_get_required_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get true Boolean value on path.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword parameter3: I am a required parameter and I'm last in Swagger.
    :paramtype parameter3: str
    :keyword parameter1: I am a required parameter with a client default value.
    :paramtype parameter1: str
    :keyword parameter2: I was a required parameter, but now I'm optional.
    :paramtype parameter2: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    parameter3 = kwargs.pop('parameter3')  # type: str
    parameter1 = kwargs.pop('parameter1', "DefaultValue")  # type: str
    parameter2 = kwargs.pop('parameter2', None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/llc/parameters')

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['parameter1'] = _SERIALIZER.query("parameter1", parameter1, 'str')
    if parameter2 is not None:
        query_parameters['parameter2'] = _SERIALIZER.query("parameter2", parameter2, 'str')
    query_parameters['parameter3'] = _SERIALIZER.query("parameter3", parameter3, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )