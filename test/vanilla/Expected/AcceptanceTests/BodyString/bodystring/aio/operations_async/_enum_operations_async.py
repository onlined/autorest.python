# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


from ... import models


class EnumOperations:
    """EnumOperations async operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer) -> None:

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer

        self._config = config

    async def get_not_expandable(self, *, cls=None, **kwargs):
        """Get enum value 'red color' from enumeration of 'red color',
        'green-color', 'blue_color'.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: Colors or the result of cls(response)
        :rtype: ~bodystring.models.Colors
        :raises: :class:`ErrorException<bodystring.models.ErrorException>`
        """
        # Construct URL
        url = self.get_not_expandable.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            raise models.ErrorException(response, self._deserialize)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('Colors', response)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    get_not_expandable.metadata = {'url': '/string/enum/notExpandable'}

    async def put_not_expandable(self, string_body, *, cls=None, **kwargs):
        """Sends value 'red color' from enumeration of 'red color', 'green-color',
        'blue_color'.

        :param string_body: Possible values include: 'red color',
         'green-color', 'blue_color'
        :type string_body: str or ~bodystring.models.Colors
        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: :class:`ErrorException<bodystring.models.ErrorException>`
        """
        # Construct URL
        url = self.put_not_expandable.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        # Construct body
        body_content = self._serialize.body(string_body, 'Colors')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            raise models.ErrorException(response, self._deserialize)

        if cls:
            response_headers = {}
            return cls(response, None, response_headers)
    put_not_expandable.metadata = {'url': '/string/enum/notExpandable'}

    async def get_referenced(self, *, cls=None, **kwargs):
        """Get enum value 'red color' from enumeration of 'red color',
        'green-color', 'blue_color'.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: Colors or the result of cls(response)
        :rtype: ~bodystring.models.Colors
        :raises: :class:`ErrorException<bodystring.models.ErrorException>`
        """
        # Construct URL
        url = self.get_referenced.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            raise models.ErrorException(response, self._deserialize)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('Colors', response)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    get_referenced.metadata = {'url': '/string/enum/Referenced'}

    async def put_referenced(self, enum_string_body, *, cls=None, **kwargs):
        """Sends value 'red color' from enumeration of 'red color', 'green-color',
        'blue_color'.

        :param enum_string_body: Possible values include: 'red color',
         'green-color', 'blue_color'
        :type enum_string_body: str or ~bodystring.models.Colors
        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: :class:`ErrorException<bodystring.models.ErrorException>`
        """
        # Construct URL
        url = self.put_referenced.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        # Construct body
        body_content = self._serialize.body(enum_string_body, 'Colors')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            raise models.ErrorException(response, self._deserialize)

        if cls:
            response_headers = {}
            return cls(response, None, response_headers)
    put_referenced.metadata = {'url': '/string/enum/Referenced'}

    async def get_referenced_constant(self, *, cls=None, **kwargs):
        """Get value 'green-color' from the constant.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: RefColorConstant or the result of cls(response)
        :rtype: ~bodystring.models.RefColorConstant
        :raises: :class:`ErrorException<bodystring.models.ErrorException>`
        """
        # Construct URL
        url = self.get_referenced_constant.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            raise models.ErrorException(response, self._deserialize)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('RefColorConstant', response)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    get_referenced_constant.metadata = {'url': '/string/enum/ReferencedConstant'}

    async def put_referenced_constant(self, field1=None, *, cls=None, **kwargs):
        """Sends value 'green-color' from a constant.

        :param field1: Sample string.
        :type field1: str
        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: :class:`ErrorException<bodystring.models.ErrorException>`
        """
        enum_string_body = models.RefColorConstant(field1=field1)

        # Construct URL
        url = self.put_referenced_constant.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        # Construct body
        body_content = self._serialize.body(enum_string_body, 'RefColorConstant')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            raise models.ErrorException(response, self._deserialize)

        if cls:
            response_headers = {}
            return cls(response, None, response_headers)
    put_referenced_constant.metadata = {'url': '/string/enum/ReferencedConstant'}
