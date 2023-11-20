# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Unbranded Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Unbranded (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from corehttp.utils import CaseInsensitiveEnumMeta


class LR(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of LR."""

    LEFT = "left"
    RIGHT = "right"


class UD(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of UD."""

    UP = "up"
    DOWN = "down"