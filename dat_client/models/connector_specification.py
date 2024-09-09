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
from dat_client.models.connection_specification import ConnectionSpecification
from dat_client.models.documentation_url import DocumentationUrl
from typing import Optional, Set
from typing_extensions import Self

class ConnectorSpecification(BaseModel):
    """
    ConnectorSpecification
    """ # noqa: E501
    documentation_url: Optional[DocumentationUrl] = None
    name: Optional[Any] = Field(description="The name of the specific connector to which this ConnectorSpecification belongs.")
    module_name: Optional[Any] = Field(description="Name of the python module for this connector")
    connection_specification: ConnectionSpecification
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["documentation_url", "name", "module_name", "connection_specification"]

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
        """Create an instance of ConnectorSpecification from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of documentation_url
        if self.documentation_url:
            _dict['documentation_url'] = self.documentation_url.to_dict()
        # override the default output from pydantic by calling `to_dict()` of connection_specification
        if self.connection_specification:
            _dict['connection_specification'] = self.connection_specification.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if module_name (nullable) is None
        # and model_fields_set contains the field
        if self.module_name is None and "module_name" in self.model_fields_set:
            _dict['module_name'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConnectorSpecification from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "documentation_url": DocumentationUrl.from_dict(obj["documentation_url"]) if obj.get("documentation_url") is not None else None,
            "name": obj.get("name"),
            "module_name": obj.get("module_name"),
            "connection_specification": ConnectionSpecification.from_dict(obj["connection_specification"]) if obj.get("connection_specification") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


