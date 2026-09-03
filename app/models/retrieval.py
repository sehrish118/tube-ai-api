from dataclasses import dataclass
from collections.abc import Mapping
from typing import Any


@dataclass
class RetrievedChunk:
    chunk_id: str
    text: str
    metadata: Mapping[str, Any]
    distance: float
