"""
This type stub file was generated by pyright.
"""

from typing import NoReturn, Optional, TYPE_CHECKING
from django.http import HttpRequest, HttpResponse
from ninja.types import DictStrAny
from ninja import NinjaAPI

if TYPE_CHECKING:
    ...
__all__ = ["default_home", "openapi_json", "openapi_view", "openapi_view_cdn"]
render_swagger = ...
view_tpl = ...
view_cdn_tpl = ...
def default_home(request: HttpRequest, api: NinjaAPI) -> NoReturn:
    "This view is mainly needed to determine the full path for API operations"
    ...

def openapi_json(request: HttpRequest, api: NinjaAPI) -> HttpResponse:
    ...

def openapi_view(request: HttpRequest, api: NinjaAPI) -> HttpResponse:
    """
    I do not really want ninja to be required in INSTALLED_APPS for now
    so we automatically detect - if ninja is in INSTALLED_APPS - then we render with django.shortcuts.render
    otherwise - rendering custom html with swagger js from cdn
    """
    ...

def openapi_view_cdn(request: HttpRequest, context: Optional[DictStrAny] = ...) -> HttpResponse:
    ...
