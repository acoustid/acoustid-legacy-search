from typing import List, Optional

from sqlalchemy import sql
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncConnection

from acoustid_legacy_search.searcher import SearchResult
from acoustid_legacy_search.db.schema import fingerprint_table


DEFAULT_SEARCH_TIMEOUT = 10.0
DEFAULT_SEARCH_LIMIT = 100


async def set_statement_timeout(conn: AsyncConnection, timeout: Optional[float]) -> None:
    if timeout is not None:
        await conn.execute(sql.text(f"SET LOCAL statement_timeout = {int(timeout * 1000)}"))


class FingerprintDatabaseClient:

    def __init__(self, engine: AsyncEngine) -> None:
        self.engine = engine

    async def extract_index_query(self, query: List[int], timeout: Optional[float] = None) -> List[int]:
        async with self.engine.connect() as conn:
            await set_statement_timeout(conn, timeout)
            select_stmt = sql.select(sql.func.acoustid_extract_query(query))
            return await conn.scalar(select_stmt)

    async def search(
            self, query: List[int], candidates: List[SearchResult],
            limit: Optional[int] = None, timeout: Optional[float] = None
    ) -> List[SearchResult]:
        async with self.engine.connect() as conn:
            await set_statement_timeout(conn, timeout)
            select_stmt = (
                sql.select([
                    fingerprint_table.c.id,
                    sql.func.acoustid_compare2(fingerprint_table.c.fingerprint, query).label("score"),
                ])
                .select_from(fingerprint_table)
                .where(fingerprint_table.c.id.in_([c.doc_id for c in candidates]))
                .order_by(sql.desc("score"))
                .limit(limit or DEFAULT_SEARCH_LIMIT)
            )
            results = []
            rows = await conn.execute(select_stmt)
            for row in rows:
                results.append(SearchResult(row.id, row.score))
            return results
