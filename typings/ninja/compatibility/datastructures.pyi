"""
This type stub file was generated by pyright.
"""

from collections.abc import Mapping

class CaseInsensitiveMapping(Mapping):
    """
    Mapping allowing case-insensitive key lookups. Original case of keys is
    preserved for iteration and string representation.
    Example::
        >>> ci_map = CaseInsensitiveMapping({'name': 'Jane'})
        >>> ci_map['Name']
        Jane
        >>> ci_map['NAME']
        Jane
        >>> ci_map['name']
        Jane
        >>> ci_map  # original case preserved
        {'name': 'Jane'}
    """
    def __init__(self, data) -> None:
        ...
    
    def __getitem__(self, key):
        ...
    
    def __len__(self): # -> int:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __iter__(self): # -> Generator[Unknown, None, None]:
        ...
    
    def __repr__(self): # -> str:
        ...
    
    def copy(self): # -> Self@CaseInsensitiveMapping:
        ...
    


