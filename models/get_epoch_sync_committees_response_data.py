# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class GetEpochSyncCommitteesResponseData(BaseModel):
    """GetEpochSyncCommitteesResponseData - a model defined in OpenAPI

        validators: The validators of this GetEpochSyncCommitteesResponseData [Optional].
        validator_aggregates: The validator_aggregates of this GetEpochSyncCommitteesResponseData [Optional].
    """

    validators: Optional[List] = Field(alias="validators", default=None)
    validator_aggregates: Optional[List[List]] = Field(alias="validator_aggregates", default=None)

GetEpochSyncCommitteesResponseData.update_forward_refs()