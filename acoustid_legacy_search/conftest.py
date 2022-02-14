import os
import random
from typing import AsyncGenerator

import pytest

from acoustid_legacy_search.index.client import IndexClient


@pytest.fixture
async def index_client() -> AsyncGenerator[IndexClient, None]:
    host = os.environ.get('ACOUSTID_SEARCH_TEST_INDEX_HOST', 'localhost')
    port = int(os.environ.get('ACOUSTID_SEARCH_TEST_INDEX_PORT', '6082'))
    async with IndexClient(host, port) as client:
        yield client


@pytest.fixture
async def index_name(index_client: IndexClient) -> AsyncGenerator[str, None]:
    i = random.randint(0, 1000000)
    index_name = f'acoustid_legacy_search_test_{i}'
    await index_client.create_index(index_name)
    try:
        yield index_name
    finally:
        await index_client.delete_index(index_name)
