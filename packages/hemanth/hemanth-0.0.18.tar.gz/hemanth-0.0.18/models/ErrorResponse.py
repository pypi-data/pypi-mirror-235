from typing import *

from pydantic import BaseModel, Field


class ErrorResponse(BaseModel):
    """
    None model

    """

    status: Optional[str] = Field(alias="status", default=None)

    errors: Optional[Dict[str, Any]] = Field(alias="errors", default=None)
