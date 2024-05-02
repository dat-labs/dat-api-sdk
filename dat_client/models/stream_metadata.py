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
from dat_client.models.dat_document_chunk import DatDocumentChunk
from dat_client.models.dat_document_entity import DatDocumentEntity
from dat_client.models.dat_last_modified import DatLastModified
from typing import Optional, Set
from typing_extensions import Self

class StreamMetadata(BaseModel):
    """
    StreamMetadata
    """ # noqa: E501
    dat_source: Optional[Any]
    dat_stream: Optional[Any]
    dat_document_entity: Optional[DatDocumentEntity] = None
    dat_last_modified: Optional[DatLastModified] = None
    dat_document_chunk: Optional[DatDocumentChunk] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["dat_source", "dat_stream", "dat_document_entity", "dat_last_modified", "dat_document_chunk"]

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
        """Create an instance of StreamMetadata from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of dat_document_entity
        if self.dat_document_entity:
            _dict['dat_document_entity'] = self.dat_document_entity.to_dict()
        # override the default output from pydantic by calling `to_dict()` of dat_last_modified
        if self.dat_last_modified:
            _dict['dat_last_modified'] = self.dat_last_modified.to_dict()
        # override the default output from pydantic by calling `to_dict()` of dat_document_chunk
        if self.dat_document_chunk:
            _dict['dat_document_chunk'] = self.dat_document_chunk.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if dat_source (nullable) is None
        # and model_fields_set contains the field
        if self.dat_source is None and "dat_source" in self.model_fields_set:
            _dict['dat_source'] = None

        # set to None if dat_stream (nullable) is None
        # and model_fields_set contains the field
        if self.dat_stream is None and "dat_stream" in self.model_fields_set:
            _dict['dat_stream'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of StreamMetadata from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dat_source": obj.get("dat_source"),
            "dat_stream": obj.get("dat_stream"),
            "dat_document_entity": DatDocumentEntity.from_dict(obj["dat_document_entity"]) if obj.get("dat_document_entity") is not None else None,
            "dat_last_modified": DatLastModified.from_dict(obj["dat_last_modified"]) if obj.get("dat_last_modified") is not None else None,
            "dat_document_chunk": DatDocumentChunk.from_dict(obj["dat_document_chunk"]) if obj.get("dat_document_chunk") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

