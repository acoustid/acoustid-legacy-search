from dataclasses import dataclass
from typing import Union


@dataclass
class SearchResult:
    doc_id: int
    score: Union[float, int]
