"""
This type stub file was generated by pyright.
"""

from typing import Any, Callable, Dict, List, Optional, Tuple

__all__ = ["ViewSignature", "is_pydantic_model", "is_collection_type", "detect_collection_fields"]
FuncParam = ...
class ViewSignature:
    FLATTEN_PATH_SEP = ...
    response_arg: Optional[str] = ...
    def __init__(self, path: str, view_func: Callable) -> None:
        ...
    


def is_pydantic_model(cls: Any) -> bool:
    ...

def is_collection_type(annotation: Any) -> bool:
    ...

def detect_collection_fields(args: List[FuncParam], flatten_map: Dict[str, Tuple[str, ...]]) -> List[str]:
    """
    QueryDict has values that are always lists, so we need to help django ninja to understand
    better the input parameters if it's a list or a single value
    This method detects attributes that should be treated by ninja as lists and returns this list as a result
    """
    ...

