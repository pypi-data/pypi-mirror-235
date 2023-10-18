from typing import *

from pydantic import BaseModel, Field


class ResumeResponse(BaseModel):
    """
    None model

    """

    status: Optional[str] = Field(alias="status", default=None)

    message: Optional[str] = Field(alias="message", default=None)

    messageKey: Optional[str] = Field(alias="messageKey", default=None)

    timeStamp: Optional[str] = Field(alias="timeStamp", default=None)

    data: Optional[Dict[str, Any]] = Field(alias="data", default=None)
