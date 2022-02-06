from typing import List, Dict, Any, Optional

from aiohttp import ClientSession

from acoustid_legacy_search.types import SearchResult


class IndexClient:
    def __init__(self, base_url):
        self.session = ClientSession(base_url=base_url)

    async def close(self) -> None:
        await self.session.close()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()

    async def get_index(self, index_name: str):
        async with self.session.get(f'/{index_name}') as response:
            return await response.json()

    async def create_index(self, index_name: str) -> None:
        async with self.session.put(f'/{index_name}') as response:
            await response.json()

    async def delete_index(self, index_name: str) -> None:
        async with self.session.put(f'/{index_name}') as response:
            await response.json()

    async def get_document(self, index_name: str, doc_id: int) -> None:
        async with self.session.get(f'/{index_name}/_doc/{doc_id}') as response:
            return await response.json()

    async def create_or_update_document(self, index_name: str, doc_id: int, terms: List[int]) -> None:
        payload = {"terms": terms}
        async with self.session.put(f'/{index_name}/_doc/{doc_id}', json=payload) as response:
            return await response.json()

    async def delete_document(self, index_name: str, doc_id: int) -> None:
        async with self.session.delete(f'/{index_name}/_doc/{doc_id}') as response:
            return await response.json()

    async def bulk_update(self, index_name: str, operations: List[Dict[str, Any]]) -> None:
        payload = {"operations": operations}
        async with self.session.post(f'/{index_name}/_bulk', json=payload) as response:
            return await response.json()

    async def search(self, index_name: str, terms: List[int], timeout: Optional[float] = None) -> List[SearchResult]:
        params = {"query": ",".join([str(t) for t in terms])}
        async with self.session.get(f'/{index_name}/_search', params=params, timeout=timeout) as response:
            response.raise_for_status()
            print(response.headers)
            doc = await response.json()
            return [SearchResult(doc_id=doc['id'], score=doc['score']) for doc in doc['results']]
