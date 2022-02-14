import logging
from typing import List

import grpc.aio

from acoustid_legacy_search.types import SearchResult
from acoustid_legacy_search.index.proto import index_pb2, index_pb2_grpc

logger = logging.getLogger(__name__)

DEFAULT_SEARCH_TIMEOUT = 10.0


class IndexUpdateBuilder:
    def __init__(self):
        self.update = index_pb2.UpdateRequest()

    def insert_or_update_document(self, doc_id: int, terms: List[int]) -> None:
        logger.info('Inserting or updating document %s with %s', doc_id, terms)
        op = index_pb2.InsertOrUpdateDocumentOp(doc_id=doc_id, terms=terms)
        self.update.updats.append(index_pb2.Operation(insert_or_update_document=op))


class IndexClient:

    def __init__(self, host: str, port: int) -> None:
        self.channel = grpc.aio.insecure_channel(f'{host}:{port}')
        self.stub = index_pb2_grpc.IndexStub(self.channel)

    async def __aenter__(self) -> 'IndexClient':
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self.close()

    async def close(self) -> None:
        await self.channel.close()

    async def create_index(self, index_name: str) -> None:
        logger.info('Creating index %s', index_name)
        request = index_pb2.CreateIndexRequest(index_name=index_name)
        await self.stub.CreateIndex(request)

    async def delete_index(self, index_name: str) -> None:
        logger.info('Deleting index %s', index_name)
        request = index_pb2.DeleteIndexRequest(index_name=index_name)
        await self.stub.DeleteIndex(request)

    async def search(self, index_name: str, terms: List[int], timeout: float = DEFAULT_SEARCH_TIMEOUT) -> List[SearchResult]:
        logger.info('Searching index %s for %s', index_name, terms)
        request = index_pb2.SearchRequest(index_name=index_name, terms=terms)
        response = await self.stub.Search(request, timeout=timeout)
        return [SearchResult(doc_id=r.doc_id, score=r.score) for r in response.results]
