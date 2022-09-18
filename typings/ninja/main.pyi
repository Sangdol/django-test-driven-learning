"""
This type stub file was generated by pyright.
"""

from typing import Any, Callable, List, Optional, Sequence, TYPE_CHECKING, Tuple, Type, Union
from django.http import HttpRequest, HttpResponse
from django.urls import URLPattern, URLResolver
from ninja.constants import NOT_SET_TYPE
from ninja.openapi.schema import OpenAPISchema
from ninja.parser import Parser
from ninja.renderers import BaseRenderer
from ninja.router import Router
from ninja.types import TCallable
from .operation import Operation

if TYPE_CHECKING:
    ...
__all__ = ["NinjaAPI"]
Exc = Union[Exception, Type[Exception]]
ExcHandler = Callable[[HttpRequest, Exc], HttpResponse]
class NinjaAPI:
    """
    Ninja API
    """
    _registry: List[str] = ...
    def __init__(self, *, title: str = ..., version: str = ..., description: str = ..., openapi_url: Optional[str] = ..., docs_url: Optional[str] = ..., docs_decorator: Optional[Callable[[TCallable], TCallable]] = ..., urls_namespace: Optional[str] = ..., csrf: bool = ..., auth: Optional[Union[Sequence[Callable], Callable, NOT_SET_TYPE]] = ..., renderer: Optional[BaseRenderer] = ..., parser: Optional[Parser] = ..., default_router: Optional[Router] = ...) -> None:
        """
        Args:
            title: A title for the api.
            description: A description for the api.
            version: The API version.
            urls_namespace: The Django URL namespace for the API. If not provided, the namespace will be ``"api-" + self.version``.
            openapi_url: The relative URL to serve the openAPI spec.
            docs_url: The relative URL to serve the API docs.
            csrf: Require a CSRF token for unsafe request types. See <a href="../csrf">CSRF</a> docs.
            auth (Callable | Sequence[Callable] | NOT_SET | None): Authentication class
            renderer: Default response renderer
            parser: Default request parser
        """
        ...
    
    def get(self, path: str, *, auth: Any = ..., response: Any = ..., operation_id: Optional[str] = ..., summary: Optional[str] = ..., description: Optional[str] = ..., tags: Optional[List[str]] = ..., deprecated: Optional[bool] = ..., by_alias: bool = ..., exclude_unset: bool = ..., exclude_defaults: bool = ..., exclude_none: bool = ..., url_name: Optional[str] = ..., include_in_schema: bool = ...) -> Callable[[TCallable], TCallable]:
        """
        `GET` operation. See <a href="../operations-parameters">operations
        parameters</a> reference.
        """
        ...
    
    def post(self, path: str, *, auth: Any = ..., response: Any = ..., operation_id: Optional[str] = ..., summary: Optional[str] = ..., description: Optional[str] = ..., tags: Optional[List[str]] = ..., deprecated: Optional[bool] = ..., by_alias: bool = ..., exclude_unset: bool = ..., exclude_defaults: bool = ..., exclude_none: bool = ..., url_name: Optional[str] = ..., include_in_schema: bool = ...) -> Callable[[TCallable], TCallable]:
        """
        `POST` operation. See <a href="../operations-parameters">operations
        parameters</a> reference.
        """
        ...
    
    def delete(self, path: str, *, auth: Any = ..., response: Any = ..., operation_id: Optional[str] = ..., summary: Optional[str] = ..., description: Optional[str] = ..., tags: Optional[List[str]] = ..., deprecated: Optional[bool] = ..., by_alias: bool = ..., exclude_unset: bool = ..., exclude_defaults: bool = ..., exclude_none: bool = ..., url_name: Optional[str] = ..., include_in_schema: bool = ...) -> Callable[[TCallable], TCallable]:
        """
        `DELETE` operation. See <a href="../operations-parameters">operations
        parameters</a> reference.
        """
        ...
    
    def patch(self, path: str, *, auth: Any = ..., response: Any = ..., operation_id: Optional[str] = ..., summary: Optional[str] = ..., description: Optional[str] = ..., tags: Optional[List[str]] = ..., deprecated: Optional[bool] = ..., by_alias: bool = ..., exclude_unset: bool = ..., exclude_defaults: bool = ..., exclude_none: bool = ..., url_name: Optional[str] = ..., include_in_schema: bool = ...) -> Callable[[TCallable], TCallable]:
        """
        `PATCH` operation. See <a href="../operations-parameters">operations
        parameters</a> reference.
        """
        ...
    
    def put(self, path: str, *, auth: Any = ..., response: Any = ..., operation_id: Optional[str] = ..., summary: Optional[str] = ..., description: Optional[str] = ..., tags: Optional[List[str]] = ..., deprecated: Optional[bool] = ..., by_alias: bool = ..., exclude_unset: bool = ..., exclude_defaults: bool = ..., exclude_none: bool = ..., url_name: Optional[str] = ..., include_in_schema: bool = ...) -> Callable[[TCallable], TCallable]:
        """
        `PUT` operation. See <a href="../operations-parameters">operations
        parameters</a> reference.
        """
        ...
    
    def api_operation(self, methods: List[str], path: str, *, auth: Any = ..., response: Any = ..., operation_id: Optional[str] = ..., summary: Optional[str] = ..., description: Optional[str] = ..., tags: Optional[List[str]] = ..., deprecated: Optional[bool] = ..., by_alias: bool = ..., exclude_unset: bool = ..., exclude_defaults: bool = ..., exclude_none: bool = ..., url_name: Optional[str] = ..., include_in_schema: bool = ...) -> Callable[[TCallable], TCallable]:
        ...
    
    def add_router(self, prefix: str, router: Router, *, auth: Any = ..., tags: Optional[List[str]] = ..., parent_router: Router = ...) -> None:
        ...
    
    @property
    def urls(self) -> Tuple[List[Union[URLResolver, URLPattern]], str, str]:
        """
        str: URL configuration

        Returns:

            Django URL configuration
        """
        ...
    
    @property
    def root_path(self) -> str:
        ...
    
    def create_response(self, request: HttpRequest, data: Any, *, status: int = ..., temporal_response: HttpResponse = ...) -> HttpResponse:
        ...
    
    def create_temporal_response(self, request: HttpRequest) -> HttpResponse:
        ...
    
    def get_content_type(self) -> str:
        ...
    
    def get_openapi_schema(self, path_prefix: Optional[str] = ...) -> OpenAPISchema:
        ...
    
    def get_openapi_operation_id(self, operation: Operation) -> str:
        ...
    
    def get_operation_url_name(self, operation: Operation, router: Router) -> str:
        """
        Get the default URL name to use for an operation if it wasn't
        explicitly provided.
        """
        ...
    
    def add_exception_handler(self, exc_class: Type[Exception], handler: ExcHandler) -> None:
        ...
    
    def exception_handler(self, exc_class: Type[Exception]) -> Callable:
        ...
    
    def set_default_exception_handlers(self) -> None:
        ...
    
    def on_exception(self, request: HttpRequest, exc: Exc) -> HttpResponse:
        ...
    


_imported_while_running_in_debug_server = ...
def debug_server_url_reimport() -> bool:
    """
    Detect reimport of URL module to allow error to propagate to developer.

    When Django loads urls it uses: ``django.urls.resolvers.urlconf_module()``

    ```Python
    @cached_property
    def urlconf_module(self):
        if isinstance(self.urlconf_name, str):
            return import_module(self.urlconf_name)
        else:
            return self.urlconf_name
    ```

    This uses ``@cached_property`` to generally only import once.  But if the
    import throws an error when using the development server, the following
    code in ``django.utils.autoreload.BaseReloader.run()`` is used:

    ```Python
    # Prevent a race condition where URL modules aren't loaded when the
    # reloader starts by accessing the urlconf_module property.
    try:
        get_resolver().urlconf_module
    except Exception:
        # Loading the urlconf can result in errors during development.
        # If this occurs then swallow the error and continue.
        pass
    ```

    This means the (likely) developer error that caused the Exception is
    initially ignored. This is not generally a problem since the error will
    usually be exercised again, and reported at that time.  But Ninja has
    various code which guards against errors where items that cannot be reused,
    are attempted to be reused.  This results in Ninja throwing a false error,
    and hiding the true error from the developer when running under the
    development server.

    Returns:

        True if this module was originally imported during Django dev-server
        init but the caller is not being running during Django dev-server init.
    """
    ...
