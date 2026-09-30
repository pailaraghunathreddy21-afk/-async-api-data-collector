from src.main import validate_data
from src.collector import fetch_page


def test_validate_data_with_valid_data():
    data = [
        {
            "userId": 1,
            "id": 1,
            "title": "Test title",
            "body": "Test body"
        }
    ]

    assert validate_data(data) is True
def test_validate_data_with_invalid_data():
    data = [
        {
            "userId": 1,
            "id": 1,
            "title": "Test title"
        }
    ]

    assert validate_data(data) is False
import asyncio
import aiohttp


def test_fetch_page():
    async def run_test():
        semaphore = asyncio.Semaphore(1)

        async with aiohttp.ClientSession() as session:
            data = await fetch_page(
                session,
                page=1,
                limit=5,
                semaphore=semaphore
            )

            assert len(data) == 5
            assert data[0]["id"] == 1

    asyncio.run(run_test())