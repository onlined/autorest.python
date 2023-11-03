# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import sys
from typing import Any, Dict, Mapping, TYPE_CHECKING, overload

from .. import _model_base
from .._model_base import rest_discriminator, rest_field

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import models as _models


class AbstractModel(_model_base.Model):
    """Used in internal operations, should be generated but not exported.

    You probably want to use the sub-classes and not this class directly. Known sub-classes are:
    RealModel

    All required parameters must be populated in order to send to server.

    :ivar name: Required.
    :vartype name: str
    :ivar kind: Required. Default value is None.
    :vartype kind: str
    """

    __mapping__: Dict[str, _model_base.Model] = {}
    name: str = rest_field()
    """Required."""
    kind: Literal[None] = rest_discriminator(name="kind")
    """Required. Default value is None."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.kind: Literal[None] = None


class BaseModel(_model_base.Model):
    """Used in internal operations, should be generated but not exported.

    All required parameters must be populated in order to send to server.

    :ivar name: Required.
    :vartype name: str
    """

    name: str = rest_field()
    """Required."""


class InnerModel(_model_base.Model):
    """Used in internal operations, should be generated but not exported.

    All required parameters must be populated in order to send to server.

    :ivar name: Required.
    :vartype name: str
    """

    name: str = rest_field()
    """Required."""


class InternalDecoratorModelInInternal(_model_base.Model):
    """Used in an internal operation, should be generated but not exported.

    All required parameters must be populated in order to send to server.

    :ivar name: Required.
    :vartype name: str
    """

    name: str = rest_field()
    """Required."""


class NoDecoratorModelInInternal(_model_base.Model):
    """Used in an internal operation, should be generated but not exported.

    All required parameters must be populated in order to send to server.

    :ivar name: Required.
    :vartype name: str
    """

    name: str = rest_field()
    """Required."""


class NoDecoratorModelInPublic(_model_base.Model):
    """Used in a public operation, should be generated and exported.

    All required parameters must be populated in order to send to server.

    :ivar name: Required.
    :vartype name: str
    """

    name: str = rest_field()
    """Required."""

    @overload
    def __init__(
        self,
        *,
        name: str,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class OuterModel(BaseModel):
    """Used in internal operations, should be generated but not exported.

    All required parameters must be populated in order to send to server.

    :ivar name: Required.
    :vartype name: str
    :ivar inner: Required.
    :vartype inner: ~specs.azure.clientgenerator.core.access.models.InnerModel
    """

    inner: "_models._models.InnerModel" = rest_field()
    """Required."""


class PublicDecoratorModelInInternal(_model_base.Model):
    """Used in an internal operation but with public decorator, should be generated and exported.

    All required parameters must be populated in order to send to server.

    :ivar name: Required.
    :vartype name: str
    """

    name: str = rest_field()
    """Required."""

    @overload
    def __init__(
        self,
        *,
        name: str,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class PublicDecoratorModelInPublic(_model_base.Model):
    """Used in a public operation, should be generated and exported.

    All required parameters must be populated in order to send to server.

    :ivar name: Required.
    :vartype name: str
    """

    name: str = rest_field()
    """Required."""

    @overload
    def __init__(
        self,
        *,
        name: str,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class RealModel(AbstractModel, discriminator="real"):
    """Used in internal operations, should be generated but not exported.

    All required parameters must be populated in order to send to server.

    :ivar name: Required.
    :vartype name: str
    :ivar kind: Required. Default value is "real".
    :vartype kind: str
    """

    kind: Literal["real"] = rest_discriminator(name="kind")  # type: ignore
    """Required. Default value is \"real\"."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.kind: Literal["real"] = "real"


class SharedModel(_model_base.Model):
    """Used by both public and internal operation. It should be generated and exported.

    All required parameters must be populated in order to send to server.

    :ivar name: Required.
    :vartype name: str
    """

    name: str = rest_field()
    """Required."""

    @overload
    def __init__(
        self,
        *,
        name: str,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)