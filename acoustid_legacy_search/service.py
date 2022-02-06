import asyncio

import grpc.aio

from acoustid_legacy_search import chromaprint
from acoustid_legacy_search.searcher import Searcher

from acoustid_legacy_search.proto.legacy_search_pb2 import SearchRequest, SearchResponse, SearchResult
from acoustid_legacy_search.proto.legacy_search_pb2_grpc import LegacySearchServicer


class SearchService(LegacySearchServicer):

    def __init__(self, searcher: Searcher) -> None:
        super().__init__()
        self.searcher = searcher

    async def Search(self, request: SearchRequest, context: grpc.aio.ServicerContext) -> SearchResponse:
        loop = asyncio.get_running_loop()
        query = await loop.run_in_executor(None, chromaprint.decode_fingerprint, request.query)
        results = await self.searcher.search(query, timeout=context.time_remaining())
        response = SearchResponse()
        for result in results:
            response.results.append(SearchResult(doc_id=str(result.doc_id), score=result.score))
        return response
