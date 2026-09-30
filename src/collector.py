import asyncio
import aiohttp
import logging

MAX_CONCURRENT_REQUESTS = 5

API_URL = "https://jsonplaceholder.typicode.com/posts"

logger = logging.getLogger(__name__)


async def fetch_page(session, page, limit, semaphore, retries=3):
    url = f"{API_URL}?_page={page}&_limit={limit}"

    for attempt in range(1, retries + 1):

        try:
            async with semaphore:
                async with session.get(url) as response:

                    if response.status == 200:
                        data = await response.json()

                        logger.info(
                            f"Page {page} collected: {len(data)} posts"
                        )

                        return data

                    else:
                        logger.warning(
                            f"Page {page} failed with status {response.status} "
                            f"(attempt {attempt}/{retries})"
                        )

        except aiohttp.ClientError as error:
            logger.error(
                f"Page {page} error: {error} "
                f"(attempt {attempt}/{retries})"
            )

        if attempt < retries:
            await asyncio.sleep(1)

    logger.error(f"Page {page} failed after {retries} attempts.")

    return []


async def collect_all_pages():
    limit = 10
    all_data = []

    semaphore = asyncio.Semaphore(MAX_CONCURRENT_REQUESTS)

    timeout = aiohttp.ClientTimeout(total=10)

    async with aiohttp.ClientSession(timeout=timeout) as session:

        page = 1

        while True:

            tasks = [
                fetch_page(
                    session,
                    current_page,
                    limit,
                    semaphore
                )
                for current_page in range(
                    page,
                    page + MAX_CONCURRENT_REQUESTS
                )
            ]

            page_results = await asyncio.gather(*tasks)

            for data in page_results:

                if not data:
                    logger.info("No more data. Stopping pagination.")
                    return all_data

                all_data.extend(data)

            page += MAX_CONCURRENT_REQUESTS

    return all_data