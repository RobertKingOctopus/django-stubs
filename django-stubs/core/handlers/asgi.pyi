from typing import (
    IO,
    Any,
    Awaitable,
    Callable,
    Dict,
    Iterator,
    Mapping,
    Optional,
    Sequence,
    Tuple,
    Type,
    TypeVar,
    Union,
)

from django.core.handlers import base as base
from django.http.request import HttpRequest, _ImmutableQueryDict
from django.http.response import HttpResponseBase
from django.urls.resolvers import ResolverMatch, URLResolver
from django.utils.datastructures import MultiValueDict

_ReceiveCallback = Callable[[], Awaitable[Mapping[str, Any]]]
_SendCallback = Callable[[Mapping[str, Any]], Awaitable[None]]

class ASGIRequest(HttpRequest):
    body_receive_timeout: int = ...
    scope: Mapping[str, Any] = ...
    resolver_match: Optional[ResolverMatch] = ...
    script_name: Optional[str] = ...
    path_info: str = ...
    path: str = ...
    method: str = ...
    META: Dict[str, Any] = ...
    def __init__(self, scope: Mapping[str, Any], body_file: IO[bytes]) -> None: ...
    @property
    def GET(self) -> _ImmutableQueryDict: ...  # type: ignore
    POST: _ImmutableQueryDict = ...
    FILES: MultiValueDict = ...
    @property
    def COOKIES(self) -> Dict[str, str]: ...  # type: ignore

_T = TypeVar("_T")

class ASGIHandler(base.BaseHandler):
    request_class: Type[ASGIRequest] = ...
    chunk_size: int = ...
    def __init__(self) -> None: ...
    async def __call__(
        self,
        scope: Dict[str, Any],
        receive: _ReceiveCallback,
        send: _SendCallback,
    ) -> None: ...
    async def read_body(self, receive: _ReceiveCallback) -> IO[bytes]: ...
    def create_request(
        self, scope: Mapping[str, Any], body_file: IO[bytes]
    ) -> Union[Tuple[ASGIRequest, None], Tuple[None, HttpResponseBase]]: ...
    def handle_uncaught_exception(
        self, request: HttpRequest, resolver: URLResolver, exc_info: Any
    ) -> HttpResponseBase: ...
    async def send_response(self, response: HttpResponseBase, send: _SendCallback) -> None: ...
    @classmethod
    def chunk_bytes(cls, data: Sequence[_T]) -> Iterator[Tuple[Sequence[_T], bool]]: ...
    def get_script_prefix(self, scope: Mapping[str, Any]) -> str: ...
