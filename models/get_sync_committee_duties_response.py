# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.get_sync_committee_duties_response_data_inner import GetSyncCommitteeDutiesResponseDataInner


class GetSyncCommitteeDutiesResponse(BaseModel):
    """GetSyncCommitteeDutiesResponse - a model defined in OpenAPI

        execution_optimistic: The execution_optimistic of this GetSyncCommitteeDutiesResponse [Optional].
        data: The data of this GetSyncCommitteeDutiesResponse [Optional].
    """

    execution_optimistic: Optional[bool] = Field(alias="execution_optimistic", default=None)
    data: Optional[List[GetSyncCommitteeDutiesResponseDataInner]] = Field(alias="data", default=None)

GetSyncCommitteeDutiesResponse.update_forward_refs()