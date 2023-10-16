import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="AssaysFilterResponse200ItemWindow")


@attr.s(auto_attribs=True)
class AssaysFilterResponse200ItemWindow:
    """  Assay window.

        Attributes:
            model_name (str):  Model name.
            path (str):  Window data path
            pipeline_name (str):  Pipeline name.
            width (str):  Window width.
            workspace_id (int):
            interval (Union[Unset, None, str]):  Window interval.
            start (Union[Unset, None, datetime.datetime]):  Window start definition.
     """

    model_name: str
    path: str
    pipeline_name: str
    width: str
    workspace_id: int
    interval: Union[Unset, None, str] = UNSET
    start: Union[Unset, None, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        model_name = self.model_name
        path = self.path
        pipeline_name = self.pipeline_name
        width = self.width
        workspace_id = self.workspace_id
        interval = self.interval
        start: Union[Unset, None, str] = UNSET
        if not isinstance(self.start, Unset):
            start = self.start.isoformat() if self.start else None


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "model_name": model_name,
            "path": path,
            "pipeline_name": pipeline_name,
            "width": width,
            "workspace_id": workspace_id,
        })
        if interval is not UNSET:
            field_dict["interval"] = interval
        if start is not UNSET:
            field_dict["start"] = start

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        model_name = d.pop("model_name")

        path = d.pop("path")

        pipeline_name = d.pop("pipeline_name")

        width = d.pop("width")

        workspace_id = d.pop("workspace_id")

        interval = d.pop("interval", UNSET)

        _start = d.pop("start", UNSET)
        start: Union[Unset, None, datetime.datetime]
        if _start is None:
            start = None
        elif isinstance(_start,  Unset):
            start = UNSET
        else:
            start = isoparse(_start)




        assays_filter_response_200_item_window = cls(
            model_name=model_name,
            path=path,
            pipeline_name=pipeline_name,
            width=width,
            workspace_id=workspace_id,
            interval=interval,
            start=start,
        )

        assays_filter_response_200_item_window.additional_properties = d
        return assays_filter_response_200_item_window

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
