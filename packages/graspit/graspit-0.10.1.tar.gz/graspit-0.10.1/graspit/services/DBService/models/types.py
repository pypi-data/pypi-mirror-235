import uuid
from typing import Union, List, Optional, Literal, Any
from graspit.services.DBService.models.enums import Status, SuiteType, AttachmentType
from pydantic import BaseModel
from datetime import datetime
from typing_extensions import TypedDict


def understand_js_date(utc_date_string: str) -> datetime:
    return datetime.strptime(utc_date_string, "%a, %d %b %Y %H:%M:%S %Z")


class CommonRegisterCols(BaseModel):
    retried: int
    started: datetime


class RegisterSession(CommonRegisterCols):
    specs: List[str]


class RegisterSuite(CommonRegisterCols):
    title: str
    description: Optional[str] = ""
    suiteType: SuiteType
    session_id: uuid.UUID
    file: str
    parent: str
    standing: Union[
        Literal[Status.YET_TO_CALCULATE],
        Literal[Status.PENDING],
        Literal[Status.SKIPPED],
    ]
    tags: Optional[List] = []


class MarkSession(BaseModel):
    duration: float
    skipped: int
    passed: int
    failed: int
    tests: int
    hooks: int
    ended: datetime
    sessionID: uuid.UUID
    entityName: str
    entityVersion: str
    simplified: str


class Error(TypedDict):
    name: str
    message: str
    stack: Optional[str]


class MarkSuite(BaseModel):
    duration: float
    ended: datetime
    suiteID: uuid.UUID
    error: Optional[Error] = None
    errors: Optional[List[Error]] = []
    standing: Optional[Status] = Status.SKIPPED


class AddAttachmentForEntity(BaseModel):
    entityID: uuid.UUID
    type: AttachmentType
    description: Optional[str] = ""
    value: str
    color: Optional[str] = ""
    title: Optional[str] = ""
