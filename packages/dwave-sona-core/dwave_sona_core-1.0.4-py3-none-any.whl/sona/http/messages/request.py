import uuid
from typing import Any, Dict, List

from pydantic import BaseModel, Field
from sona.core.messages import File


class SonaRequest(BaseModel):
    context_id: uuid.UUID = Field(default_factory=uuid.uuid4)
    params: Dict[Any, Any] = {}
    files: List[File] = []
