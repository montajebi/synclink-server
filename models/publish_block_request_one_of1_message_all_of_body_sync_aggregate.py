# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class PublishBlockRequestOneOf1MessageAllOfBodySyncAggregate(BaseModel):
    """PublishBlockRequestOneOf1MessageAllOfBodySyncAggregate - a model defined in OpenAPI

        sync_committee_bits: The sync_committee_bits of this PublishBlockRequestOneOf1MessageAllOfBodySyncAggregate [Optional].
        sync_committee_signature: The sync_committee_signature of this PublishBlockRequestOneOf1MessageAllOfBodySyncAggregate [Optional].
    """

    sync_committee_bits: Optional[str] = Field(alias="sync_committee_bits", default=None)
    sync_committee_signature: Optional[str] = Field(alias="sync_committee_signature", default=None)

    @validator("sync_committee_bits")
    def sync_committee_bits_pattern(cls, value):
        assert value is not None and re.match(r"^0x[a-fA-F0-9]+$", value)
        return value

    @validator("sync_committee_signature")
    def sync_committee_signature_pattern(cls, value):
        assert value is not None and re.match(r"^0x[a-fA-F0-9]{192}$", value)
        return value

PublishBlockRequestOneOf1MessageAllOfBodySyncAggregate.update_forward_refs()
