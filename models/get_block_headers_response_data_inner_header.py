# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.get_block_headers_response_data_inner_header_message import GetBlockHeadersResponseDataInnerHeaderMessage


class GetBlockHeadersResponseDataInnerHeader(BaseModel):
    """GetBlockHeadersResponseDataInnerHeader - a model defined in OpenAPI

        message: The message of this GetBlockHeadersResponseDataInnerHeader [Optional].
        signature: The signature of this GetBlockHeadersResponseDataInnerHeader [Optional].
    """

    message: Optional[GetBlockHeadersResponseDataInnerHeaderMessage] = Field(alias="message", default=None)
    signature: Optional[str] = Field(alias="signature", default=None)

    @validator("signature")
    def signature_pattern(cls, value):
        assert value is not None and re.match(r"^0x[a-fA-F0-9]{192}$", value)
        return value

GetBlockHeadersResponseDataInnerHeader.update_forward_refs()
