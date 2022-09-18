"""
This type stub file was generated by pyright.
"""

from pydantic import BaseModel

class Settings(BaseModel):
    """
    Alter these by modifying the values in Django's settings module (usually
    `settings.py`).

    Attributes:
        NINJA_PAGINATION_CLASS (str):
            The pagination class to use. Defaults to
            `ninja.pagination.Pagination`.
        NINJA_PAGINATION_PAGE_SIZE (int):
            The default page size. Defaults to `100`.
        NINJA_DOCS_VIEW ("swagger"|"redoc"):
            The view to use for the documentation. Defaults to `swagger`, but
            change to `redoc` to use alternative
            [Redoc](https://github.com/Redocly/redoc) automatic documentation.
    """
    PAGINATION_CLASS: str = ...
    PAGINATION_PER_PAGE: int = ...
    DOCS_VIEW: str = ...
    class Config:
        orm_mode = ...
    
    


settings = ...