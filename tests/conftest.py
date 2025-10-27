import sys
from pathlib import Path
import asyncio
from typing import Generator
import pytest

# Ensure the repository root is on sys.path so `import app` works during pytest collection.
# This mirrors what CI does when the repository root is the working directory.
REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))


@pytest.fixture(scope="session")
def event_loop() -> Generator[asyncio.AbstractEventLoop, None, None]:
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()