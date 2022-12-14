"""
This type stub file was generated by pyright.
"""

from typing import no_type_check
from ninja.schema import ResolverMetaclass, Schema

_is_modelschema_class_defined = ...
class ModelSchemaMetaclass(ResolverMetaclass):
    @no_type_check
    def __new__(mcs, name: str, bases: tuple, namespace: dict): # -> Type[Schema] | Self@ModelSchemaMetaclass:
        ...
    


class ModelSchema(Schema, metaclass=ModelSchemaMetaclass):
    ...


_is_modelschema_class_defined = ...
