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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.cursor_field import CursorField
from openapi_client.models.dat_document_stream import DatDocumentStream
from openapi_client.models.destination_sync_mode import DestinationSyncMode
from openapi_client.models.primary_key import PrimaryKey
from openapi_client.models.sync_mode import SyncMode
from typing import Optional, Set
from typing_extensions import Self

class ConfiguredDocumentStream(BaseModel):
    """
    ConfiguredDocumentStream
    """ # noqa: E501
    stream: DatDocumentStream
    namespace: Optional[Any] = Field(description="namespace the data is associated with")
    sync_mode: SyncMode
    destination_sync_mode: DestinationSyncMode
    cursor_field: Optional[CursorField] = None
    primary_key: Optional[PrimaryKey] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["stream", "namespace", "sync_mode", "destination_sync_mode", "cursor_field", "primary_key"]

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
        """Create an instance of ConfiguredDocumentStream from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of cursor_field
        if self.cursor_field:
            _dict['cursor_field'] = self.cursor_field.to_dict()
        # override the default output from pydantic by calling `to_dict()` of primary_key
        if self.primary_key:
            _dict['primary_key'] = self.primary_key.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if namespace (nullable) is None
        # and model_fields_set contains the field
        if self.namespace is None and "namespace" in self.model_fields_set:
            _dict['namespace'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConfiguredDocumentStream from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "stream": DatDocumentStream.from_dict(obj["stream"]) if obj.get("stream") is not None else None,
            "namespace": obj.get("namespace"),
            "sync_mode": obj.get("sync_mode"),
            "destination_sync_mode": obj.get("destination_sync_mode"),
            "cursor_field": CursorField.from_dict(obj["cursor_field"]) if obj.get("cursor_field") is not None else None,
            "primary_key": PrimaryKey.from_dict(obj["primary_key"]) if obj.get("primary_key") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


