# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from dat_client.models.dat_document_stream_input import DatDocumentStreamInput
from dat_client.models.emitted_at import EmittedAt
from dat_client.models.stream_state import StreamState
from typing import Optional, Set
from typing_extensions import Self

class DatStateMessage(BaseModel):
    """
    DatStateMessage
    """ # noqa: E501
    stream: DatDocumentStreamInput
    stream_state: StreamState
    emitted_at: Optional[EmittedAt] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["stream", "stream_state", "emitted_at"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of DatStateMessage from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of stream
        if self.stream:
            _dict['stream'] = self.stream.to_dict()
        # override the default output from pydantic by calling `to_dict()` of stream_state
        if self.stream_state:
            _dict['stream_state'] = self.stream_state.to_dict()
        # override the default output from pydantic by calling `to_dict()` of emitted_at
        if self.emitted_at:
            _dict['emitted_at'] = self.emitted_at.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DatStateMessage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "stream": DatDocumentStreamInput.from_dict(obj["stream"]) if obj.get("stream") is not None else None,
            "stream_state": StreamState.from_dict(obj["stream_state"]) if obj.get("stream_state") is not None else None,
            "emitted_at": EmittedAt.from_dict(obj["emitted_at"]) if obj.get("emitted_at") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


