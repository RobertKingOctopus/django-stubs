import json
from typing import Any, Dict, Optional, Type, Union

from django.db.backends.base.base import BaseDatabaseWrapper
from django.db.models import lookups
from django.db.models.expressions import Expression
from django.db.models.lookups import PostgresOperatorLookup, Transform
from django.db.models.sql.compiler import SQLCompiler
from django.utils.connection import ConnectionProxy

from . import Field
from .mixins import CheckFieldDefaultMixin

class JSONField(CheckFieldDefaultMixin, Field):
    encoder: Optional[Type[json.JSONEncoder]]
    decoder: Optional[Type[json.JSONDecoder]]
    def __init__(
        self,
        verbose_name: Optional[str] = ...,
        name: Optional[str] = ...,
        encoder: Optional[Type[json.JSONEncoder]] = ...,
        decoder: Optional[Type[json.JSONDecoder]] = ...,
        **kwargs: Any
    ) -> None: ...
    def from_db_value(
        self,
        value: Optional[str],
        expression: Optional[Union[Field, Expression]],
        connection: Optional[ConnectionProxy],
    ) -> Optional[Dict]: ...

class DataContains(PostgresOperatorLookup): ...
class ContainedBy(PostgresOperatorLookup): ...

class HasKeyLookup(PostgresOperatorLookup):
    logical_operator: Optional[str] = ...

class HasKey(HasKeyLookup):
    postgres_operator: str = ...

class HasKeys(HasKeyLookup):
    postgres_operator: str = ...
    logical_operator: str = ...

class HasAnyKeys(HasKeys):
    postgres_operator: str = ...
    logical_operator: str = ...

class JSONExact(lookups.Exact): ...

class KeyTransform(Transform):
    key_name: str = ...
    postgres_operator: str = ...
    postgres_nested_operator: str = ...
    def __init__(self, key_name: Any, *args: Any, **kwargs: Any) -> None: ...
    def preprocess_lhs(self, compiler: SQLCompiler, connection: BaseDatabaseWrapper) -> Any: ...

class KeyTextTransform(KeyTransform):
    postgres_operator: str = ...
    postgres_nested_operator: str = ...

class KeyTransformTextLookupMixin:
    def __init__(self, key_transform: Any, *args: Any, **kwargs: Any) -> None: ...

class CaseInsensitiveMixin: ...
class KeyTransformIsNull(lookups.IsNull): ...
class KeyTransformIn(lookups.In): ...
class KeyTransformExact(JSONExact): ...
class KeyTransformIExact(CaseInsensitiveMixin, KeyTransformTextLookupMixin, lookups.IExact): ...
class KeyTransformIContains(CaseInsensitiveMixin, KeyTransformTextLookupMixin, lookups.IContains): ...
class KeyTransformStartsWith(KeyTransformTextLookupMixin, lookups.StartsWith): ...
class KeyTransformIStartsWith(CaseInsensitiveMixin, KeyTransformTextLookupMixin, lookups.IStartsWith): ...
class KeyTransformEndsWith(KeyTransformTextLookupMixin, lookups.EndsWith): ...
class KeyTransformIEndsWith(CaseInsensitiveMixin, KeyTransformTextLookupMixin, lookups.IEndsWith): ...
class KeyTransformRegex(KeyTransformTextLookupMixin, lookups.Regex): ...
class KeyTransformIRegex(CaseInsensitiveMixin, KeyTransformTextLookupMixin, lookups.IRegex): ...
class KeyTransformNumericLookupMixin: ...
class KeyTransformLt(KeyTransformNumericLookupMixin, lookups.LessThan): ...
class KeyTransformLte(KeyTransformNumericLookupMixin, lookups.LessThanOrEqual): ...
class KeyTransformGt(KeyTransformNumericLookupMixin, lookups.GreaterThan): ...
class KeyTransformGte(KeyTransformNumericLookupMixin, lookups.GreaterThanOrEqual): ...

class KeyTransformFactory:
    key_name: Any = ...
    def __init__(self, key_name: Any) -> None: ...
    def __call__(self, *args: Any, **kwargs: Any): ...
