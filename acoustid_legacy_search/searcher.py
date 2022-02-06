import time
from typing import List, Optional

from acoustid_legacy_search.types import SearchResult
from acoustid_legacy_search.index import IndexClient
from acoustid_legacy_search.db import FingerprintDatabaseClient

DEFAULT_SEARCH_LIMIT = 100
DEFAULT_SEARCH_TIMEOUT = 10.0


class DeadlineTimer:
    def __init__(self, timeout: float):
        self.deadline = time.monotonic() + timeout

    def remaining_time(self) -> float:
        return self.deadline - time.monotonic()

    def is_expired(self) -> bool:
        return self.remaining_time() <= 0.0


class Searcher:

    def __init__(self, index: IndexClient, db: FingerprintDatabaseClient) -> None:
        self.index = index
        self.db = db

    async def search(self, query: List[int], limit: Optional[int] = None, timeout: Optional[float] = None) -> List[SearchResult]:
        if limit is None:
            limit = DEFAULT_SEARCH_LIMIT
        if timeout is None:
            timeout = DEFAULT_SEARCH_TIMEOUT
        deadline = DeadlineTimer(timeout)
        index_query = await self.db.extract_index_query(query)
        if deadline.is_expired():
            raise TimeoutError()
        candidates = await self.index.search('main', index_query, timeout=deadline.remaining_time())
        if deadline.is_expired():
            raise TimeoutError()
        return await self.db.search(query, candidates, timeout=deadline.remaining_time())
