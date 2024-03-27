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

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.catalog import Catalog
from openapi_client.models.configuration import Configuration
from openapi_client.models.cron_string import CronString
from openapi_client.models.status import Status
from typing import Optional, Set
from typing_extensions import Self

class ConnectionRequestInstance(BaseModel):
    """
    ConnectionRequestInstance
    """ # noqa: E501
    name: StrictStr
    source_instance_id: StrictStr
    generator_instance_id: StrictStr
    destination_instance_id: StrictStr
    configuration: Optional[Configuration] = None
    catalog: Optional[Catalog] = None
    cron_string: Optional[CronString] = None
    status: Optional[Status] = None
    __properties: ClassVar[List[str]] = ["name", "source_instance_id", "generator_instance_id", "destination_instance_id", "configuration", "catalog", "cron_string", "status"]

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
        """Create an instance of ConnectionRequestInstance from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of configuration
        if self.configuration:
            _dict['configuration'] = self.configuration.to_dict()
        # override the default output from pydantic by calling `to_dict()` of catalog
        if self.catalog:
            _dict['catalog'] = self.catalog.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cron_string
        if self.cron_string:
            _dict['cron_string'] = self.cron_string.to_dict()
        # override the default output from pydantic by calling `to_dict()` of status
        if self.status:
            _dict['status'] = self.status.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConnectionRequestInstance from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "source_instance_id": obj.get("source_instance_id"),
            "generator_instance_id": obj.get("generator_instance_id"),
            "destination_instance_id": obj.get("destination_instance_id"),
            "configuration": Configuration.from_dict(obj["configuration"]) if obj.get("configuration") is not None else None,
            "catalog": Catalog.from_dict(obj["catalog"]) if obj.get("catalog") is not None else None,
            "cron_string": CronString.from_dict(obj["cron_string"]) if obj.get("cron_string") is not None else None,
            "status": Status.from_dict(obj["status"]) if obj.get("status") is not None else None
        })
        return _obj


