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
from ._serialization import Serializer, Deserializer
from io import IOBase
from typing import Any, IO, Iterable, Optional, Union

from azure.core.paging import ItemPaged
from azure.core.polling import LROPoller

from . import models as _models


class MultiapiServiceClientOperationsMixin(object):

    def begin_test_lro(
        self,
        product: Optional[Union[_models.Product, IO[bytes]]] = None,
        **kwargs: Any
    ) -> LROPoller[_models.Product]:
        """Put in whatever shape of Product you want, will return a Product with id equal to 100.

        :param product: Product to put. Is either a Product type or a IO[bytes] type. Default value is
         None.
        :type product: ~multiapikeywordonly.v1.models.Product or IO[bytes]
        :return: An instance of LROPoller that returns either Product or the result of cls(response)
        :rtype: ~azure.core.polling.LROPoller[~multiapikeywordonly.v1.models.Product]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        api_version = self._get_api_version('begin_test_lro')
        if api_version == '1.0.0':
            from .v1.operations import MultiapiServiceClientOperationsMixin as OperationClass
        else:
            raise ValueError("API version {} does not have operation 'begin_test_lro'".format(api_version))
        mixin_instance = OperationClass()
        mixin_instance._client = self._client
        mixin_instance._config = self._config
        mixin_instance._config.api_version = api_version
        mixin_instance._serialize = Serializer(self._models_dict(api_version))
        mixin_instance._serialize.client_side_validation = False
        mixin_instance._deserialize = Deserializer(self._models_dict(api_version))
        return mixin_instance.begin_test_lro(product, **kwargs)

    def begin_test_lro_and_paging(
        self,
        test_lro_and_paging_options: Optional[_models.TestLroAndPagingOptions] = None,
        *,
        client_request_id: Optional[str] = None,
        **kwargs: Any
    ) -> LROPoller[Iterable["_models.Product"]]:
        """A long-running paging operation that includes a nextLink that has 10 pages.

        :param test_lro_and_paging_options: Parameter group. Default value is None.
        :type test_lro_and_paging_options: ~multiapikeywordonly.v1.models.TestLroAndPagingOptions
        :keyword client_request_id: Default value is None.
        :paramtype client_request_id: str
        :return: An instance of LROPoller that returns an iterator like instance of either PagingResult
         or the result of cls(response)
        :rtype:
         ~azure.core.polling.LROPoller[~azure.core.paging.ItemPaged[~multiapikeywordonly.v1.models.Product]]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        api_version = self._get_api_version('begin_test_lro_and_paging')
        if api_version == '1.0.0':
            from .v1.operations import MultiapiServiceClientOperationsMixin as OperationClass
        else:
            raise ValueError("API version {} does not have operation 'begin_test_lro_and_paging'".format(api_version))
        mixin_instance = OperationClass()
        mixin_instance._client = self._client
        mixin_instance._config = self._config
        mixin_instance._config.api_version = api_version
        mixin_instance._serialize = Serializer(self._models_dict(api_version))
        mixin_instance._serialize.client_side_validation = False
        mixin_instance._deserialize = Deserializer(self._models_dict(api_version))
        return mixin_instance.begin_test_lro_and_paging(test_lro_and_paging_options, client_request_id=client_request_id, **kwargs)

    def test_different_calls(  # pylint: disable=inconsistent-return-statements
        self,
        *,
        greeting_in_english: str,
        greeting_in_chinese: Optional[str] = None,
        greeting_in_french: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """Has added parameters across the API versions.

        :keyword greeting_in_english: pass in 'hello' to pass test. Required.
        :paramtype greeting_in_english: str
        :keyword greeting_in_chinese: pass in 'nihao' to pass test. Default value is None.
        :paramtype greeting_in_chinese: str
        :keyword greeting_in_french: pass in 'bonjour' to pass test. Default value is None.
        :paramtype greeting_in_french: str
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        api_version = self._get_api_version('test_different_calls')
        if api_version == '1.0.0':
            from .v1.operations import MultiapiServiceClientOperationsMixin as OperationClass
        elif api_version == '2.0.0':
            from .v2.operations import MultiapiServiceClientOperationsMixin as OperationClass
        elif api_version == '3.0.0':
            from .v3.operations import MultiapiServiceClientOperationsMixin as OperationClass
        else:
            raise ValueError("API version {} does not have operation 'test_different_calls'".format(api_version))
        mixin_instance = OperationClass()
        mixin_instance._client = self._client
        mixin_instance._config = self._config
        mixin_instance._config.api_version = api_version
        mixin_instance._serialize = Serializer(self._models_dict(api_version))
        mixin_instance._serialize.client_side_validation = False
        mixin_instance._deserialize = Deserializer(self._models_dict(api_version))
        return mixin_instance.test_different_calls(greeting_in_english=greeting_in_english, greeting_in_chinese=greeting_in_chinese, greeting_in_french=greeting_in_french, **kwargs)

    def test_one(  # pylint: disable=inconsistent-return-statements
        self,
        *,
        id: int,
        message: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """TestOne should be in an FirstVersionOperationsMixin.

        :keyword id: An int parameter. Required.
        :paramtype id: int
        :keyword message: An optional string parameter. Default value is None.
        :paramtype message: str
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        api_version = self._get_api_version('test_one')
        if api_version == '1.0.0':
            from .v1.operations import MultiapiServiceClientOperationsMixin as OperationClass
        elif api_version == '2.0.0':
            from .v2.operations import MultiapiServiceClientOperationsMixin as OperationClass
        else:
            raise ValueError("API version {} does not have operation 'test_one'".format(api_version))
        mixin_instance = OperationClass()
        mixin_instance._client = self._client
        mixin_instance._config = self._config
        mixin_instance._config.api_version = api_version
        mixin_instance._serialize = Serializer(self._models_dict(api_version))
        mixin_instance._serialize.client_side_validation = False
        mixin_instance._deserialize = Deserializer(self._models_dict(api_version))
        return mixin_instance.test_one(id=id, message=message, **kwargs)

    def test_paging(
        self,
        **kwargs: Any
    ) -> Iterable["_models.ModelThree"]:
        """Returns ModelThree with optionalProperty 'paged'.

        :return: An iterator like instance of either ModelThree or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~multiapikeywordonly.v3.models.ModelThree]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        api_version = self._get_api_version('test_paging')
        if api_version == '3.0.0':
            from .v3.operations import MultiapiServiceClientOperationsMixin as OperationClass
        else:
            raise ValueError("API version {} does not have operation 'test_paging'".format(api_version))
        mixin_instance = OperationClass()
        mixin_instance._client = self._client
        mixin_instance._config = self._config
        mixin_instance._config.api_version = api_version
        mixin_instance._serialize = Serializer(self._models_dict(api_version))
        mixin_instance._serialize.client_side_validation = False
        mixin_instance._deserialize = Deserializer(self._models_dict(api_version))
        return mixin_instance.test_paging(**kwargs)
