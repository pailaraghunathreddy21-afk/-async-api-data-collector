import asyncio
import json
import logging
import time

from src.collector import collect_all_pages


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def validate_data(data):
    required_fields = {"userId", "id", "title", "body"}

    for item in data:
        if not required_fields.issubset(item.keys()):
            return False

    return True

async def main():
    start_time = time.perf_counter()

    all_data = await collect_all_pages()

    if not validate_data(all_data):

        logging.error("Data validation failed.")

        return

    logging.info("Data validation successful.")

    with open("data/posts.json", "w") as file:

        json.dump(all_data, file, indent=4)

    logging.info(f"Total posts collected: {len(all_data)}")
    unique_ids = len({item["id"] for item in all_data})
    logging.info(f"Unique records: {unique_ids}")

    logging.info("Data saved to data/posts.json")
    end_time = time.perf_counter()

    elapsed_time = end_time - start_time

    logging.info(f"Collection completed in {elapsed_time:.2f} seconds")


asyncio.run(main())