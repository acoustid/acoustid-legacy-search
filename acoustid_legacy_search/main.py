import os
import asyncio
import signal
import logging
from contextlib import AsyncExitStack

import grpc.aio

from sqlalchemy.ext.asyncio import create_async_engine

from acoustid_legacy_search.index import IndexClient
from acoustid_legacy_search.service import SearchService
from acoustid_legacy_search.proto.legacy_search_pb2_grpc import add_LegacySearchServicer_to_server
from acoustid_legacy_search.db import FingerprintDatabaseClient
from acoustid_legacy_search.searcher import Searcher

logger = logging.getLogger(__name__)


async def run_search_service() -> None:
    logging.basicConfig(level=logging.INFO)

    server = grpc.aio.server()

    stop_attempts = 0

    def stop_server() -> asyncio.Task:
        nonlocal stop_attempts
        stop_attempts += 1
        if stop_attempts > 2:
            logger.info('Stopping server')
            return asyncio.create_task(server.stop(0.0))
        else:
            logger.info('Stopping server (gracefully)')
            return asyncio.create_task(server.stop(10.0))

    loop = asyncio.get_running_loop()
    loop.add_signal_handler(signal.SIGINT, stop_server)
    loop.add_signal_handler(signal.SIGTERM, stop_server)

    async with AsyncExitStack() as exit_stack:
        index_url = os.environ.get('ACOUSTID_SEARCH_INDEX_URL', 'http://127.0.0.1:6081')
        index = await exit_stack.enter_async_context(IndexClient(index_url))

        db_url = os.environ.get('ACOUSTID_SEARCH_DB_URL', 'postgresql+asyncpg://acoustid:acoustid@127.0.0.1:5432/acoustid')
        db_engine = create_async_engine(db_url)
        exit_stack.callback(db_engine.dispose)
        db = FingerprintDatabaseClient(db_engine)

        searcher = Searcher(index, db)
        service = SearchService(searcher)
        add_LegacySearchServicer_to_server(service, server)

        logger.info('Starting server')
        await server.start()
        await server.wait_for_termination()


def main() -> None:
    asyncio.run(run_search_service())
