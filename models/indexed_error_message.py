# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.submit_pool_attestations400_response_failures_inner import SubmitPoolAttestations400ResponseFailuresInner


class IndexedErrorMessage(BaseModel):
    """IndexedErrorMessage - a model defined in OpenAPI

        code: The code of this IndexedErrorMessage [Optional].
        message: The message of this IndexedErrorMessage [Optional].
        failures: The failures of this IndexedErrorMessage [Optional].
    """

    code: Optional[float] = Field(alias="code", default=None)
    message: Optional[str] = Field(alias="message", default=None)
    failures: Optional[List[SubmitPoolAttestations400ResponseFailuresInner]] = Field(alias="failures", default=None)

IndexedErrorMessage.update_forward_refs()
