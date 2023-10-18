from typing import *

from pydantic import BaseModel, Field


class ResumeRequest(BaseModel):
    """
    None model

    """

    filename: Optional[str] = Field(alias="filename", default=None)

    datastream: Optional[str] = Field(alias="datastream", default=None)
