import asyncio
from typing import List

import grpc.aio

from acoustid_legacy_search import chromaprint
from acoustid_legacy_search.index import IndexClient
from acoustid_legacy_search.db import FingerprintDatabaseClient

from acoustid_legacy_search.proto.legacy_search_pb2 import SearchRequest, SearchResponse
from acoustid_legacy_search.proto.legacy_search_pb2_grpc import LegacySearchServicer


async def decode_fingerprint(encoded_fingerprint: str) -> List[int]:
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(None, chromaprint.decode_fingerprint, encoded_fingerprint)


class SearchService(LegacySearchServicer):

    def __init__(self, index: IndexClient, db: FingerprintDatabaseClient) -> None:
        super().__init__()
        self.index = index
        self.db = db

    async def Search(self, request: SearchRequest, context: grpc.aio.ServicerContext) -> SearchResponse:
        query = await decode_fingerprint(request.query)
        index_query = await self.db.extract_index_query(query)
        candidates = await self.index.search(index_query)
        print(query)
        response = SearchResponse()
        return response
