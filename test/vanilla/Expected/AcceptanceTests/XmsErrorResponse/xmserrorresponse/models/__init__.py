# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import Animal
    from ._models_py3 import AnimalNotFound, AnimalNotFoundException
    from ._models_py3 import BaseError
    from ._models_py3 import LinkNotFound, LinkNotFoundException
    from ._models_py3 import NotFoundErrorBase, NotFoundErrorBaseException
    from ._models_py3 import Pet
    from ._models_py3 import PetAction
    from ._models_py3 import PetActionError, PetActionErrorException
    from ._models_py3 import PetHungryOrThirstyError, PetHungryOrThirstyErrorException
    from ._models_py3 import PetSadError, PetSadErrorException
except (SyntaxError, ImportError):
    from ._models import Animal
    from ._models import AnimalNotFound, AnimalNotFoundException
    from ._models import BaseError
    from ._models import LinkNotFound, LinkNotFoundException
    from ._models import NotFoundErrorBase, NotFoundErrorBaseException
    from ._models import Pet
    from ._models import PetAction
    from ._models import PetActionError, PetActionErrorException
    from ._models import PetHungryOrThirstyError, PetHungryOrThirstyErrorException
    from ._models import PetSadError, PetSadErrorException

__all__ = [
    'Animal',
    'AnimalNotFound', 'AnimalNotFoundException',
    'BaseError',
    'LinkNotFound', 'LinkNotFoundException',
    'NotFoundErrorBase', 'NotFoundErrorBaseException',
    'Pet',
    'PetAction',
    'PetActionError', 'PetActionErrorException',
    'PetHungryOrThirstyError', 'PetHungryOrThirstyErrorException',
    'PetSadError', 'PetSadErrorException',
]