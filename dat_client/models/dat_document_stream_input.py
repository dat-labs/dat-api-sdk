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
from dat_client.models.cursor_field import CursorField
from dat_client.models.dat_document_stream_input_advanced import DatDocumentStreamInputAdvanced
from dat_client.models.dat_document_stream_input_read_sync_mode import DatDocumentStreamInputReadSyncMode
from dat_client.models.dat_document_stream_input_write_sync_mode import DatDocumentStreamInputWriteSyncMode
from dat_client.models.json_schema import JsonSchema
from dat_client.models.namespace1 import Namespace1
from typing import Optional, Set
from typing_extensions import Self

class DatDocumentStreamInput(BaseModel):
    """
    DatDocumentStreamInput
    """ # noqa: E501
    name: Optional[Any] = Field(description="The name of the document stream.")
    namespace: Optional[Namespace1] = None
    json_schema: Optional[JsonSchema] = None
    read_sync_mode: Optional[DatDocumentStreamInputReadSyncMode] = None
    write_sync_mode: Optional[DatDocumentStreamInputWriteSyncMode] = None
    cursor_field: Optional[CursorField] = None
    advanced: Optional[DatDocumentStreamInputAdvanced] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["name", "namespace", "json_schema", "read_sync_mode", "write_sync_mode", "cursor_field", "advanced"]

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
        """Create an instance of DatDocumentStreamInput from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of namespace
        if self.namespace:
            _dict['namespace'] = self.namespace.to_dict()
        # override the default output from pydantic by calling `to_dict()` of json_schema
        if self.json_schema:
            _dict['json_schema'] = self.json_schema.to_dict()
        # override the default output from pydantic by calling `to_dict()` of read_sync_mode
        if self.read_sync_mode:
            _dict['read_sync_mode'] = self.read_sync_mode.to_dict()
        # override the default output from pydantic by calling `to_dict()` of write_sync_mode
        if self.write_sync_mode:
            _dict['write_sync_mode'] = self.write_sync_mode.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cursor_field
        if self.cursor_field:
            _dict['cursor_field'] = self.cursor_field.to_dict()
        # override the default output from pydantic by calling `to_dict()` of advanced
        if self.advanced:
            _dict['advanced'] = self.advanced.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DatDocumentStreamInput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "namespace": Namespace1.from_dict(obj["namespace"]) if obj.get("namespace") is not None else None,
            "json_schema": JsonSchema.from_dict(obj["json_schema"]) if obj.get("json_schema") is not None else None,
            "read_sync_mode": DatDocumentStreamInputReadSyncMode.from_dict(obj["read_sync_mode"]) if obj.get("read_sync_mode") is not None else None,
            "write_sync_mode": DatDocumentStreamInputWriteSyncMode.from_dict(obj["write_sync_mode"]) if obj.get("write_sync_mode") is not None else None,
            "cursor_field": CursorField.from_dict(obj["cursor_field"]) if obj.get("cursor_field") is not None else None,
            "advanced": DatDocumentStreamInputAdvanced.from_dict(obj["advanced"]) if obj.get("advanced") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


