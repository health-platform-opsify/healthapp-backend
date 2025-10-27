import pytest
import pytest_asyncio

# Set the default fixture loop scope to function
pytest_asyncio.plugin.default_fixture_loop_scope = "function"

@pytest.fixture(scope="session")
def event_loop():
    """Create an instance of the default event loop for each test case."""
    import asyncio
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()