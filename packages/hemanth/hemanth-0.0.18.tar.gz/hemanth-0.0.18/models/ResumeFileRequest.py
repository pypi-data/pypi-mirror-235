from typing import *

from pydantic import BaseModel, Field


class ResumeFileRequest(BaseModel):
    """
    None model

    """

    file: Optional[str] = Field(alias="file", default=None)
