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

from .fish_py3 import Fish


class Salmon(Fish):
    """Salmon.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: SmartSalmon

    All required parameters must be populated in order to send to Azure.

    :param species:
    :type species: str
    :param length: Required.
    :type length: float
    :param siblings:
    :type siblings: list[~bodycomplex.models.Fish]
    :param fishtype: Required. Constant filled by server.
    :type fishtype: str
    :param location:
    :type location: str
    :param iswild:
    :type iswild: bool
    """

    _validation = {
        'length': {'required': True},
        'fishtype': {'required': True},
    }

    _attribute_map = {
        'species': {'key': 'species', 'type': 'str'},
        'length': {'key': 'length', 'type': 'float'},
        'siblings': {'key': 'siblings', 'type': '[Fish]'},
        'fishtype': {'key': 'fishtype', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'iswild': {'key': 'iswild', 'type': 'bool'},
    }

    _subtype_map = {
        'fishtype': {'smart_salmon': 'SmartSalmon'}
    }

    def __init__(self, *, length: float, species: str=None, siblings=None, location: str=None, iswild: bool=None, **kwargs) -> None:
        super(Salmon, self).__init__(species=species, length=length, siblings=siblings, **kwargs)
        self.location = location
        self.iswild = iswild
        self.fishtype = 'salmon'