import asyncio
from typing import AsyncGenerator, Generator
import pytest
import pytest_asyncio

# Set the event loop fixture scope
pytest.ini_options = {
    "asyncio_mode": "auto",
}

@pytest.fixture(scope="session")
def event_loop() -> Generator[asyncio.AbstractEventLoop, None, None]:
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()