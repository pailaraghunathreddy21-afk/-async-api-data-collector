# Async API Data Collector

An asynchronous Python application that collects data from REST APIs efficiently using `asyncio` and `aiohttp`.

## Project Overview

The **Async API Data Collector** is designed to collect large amounts of data from REST APIs efficiently.

Instead of sending API requests one by one, the project uses asynchronous programming to handle multiple requests concurrently. It also supports pagination, retries, timeout handling, data validation, logging, and structured JSON storage.

## Features

- Asynchronous API requests using `asyncio`
- HTTP requests using `aiohttp`
- Concurrent data collection
- Pagination support
- Retry mechanism for failed requests
- Request timeout handling
- Error handling
- Data validation
- Duplicate record checking
- Structured JSON storage
- Logging with timestamps
- Performance measurement
- Automated testing with `pytest`

## Technologies Used

- Python 3
- `asyncio`
- `aiohttp`
- REST API
- JSON
- `pytest`
- Git & GitHub

## Project Architecture

```text
User
  |
  v
Python Application
  |
  v
Asyncio Controller
  |
  +----> API Request 1
  +----> API Request 2
  +----> API Request 3
  +----> API Request 4
  +----> API Request 5
             |
             v
         REST API
             |
             v
        JSON Response
             |
             v
      Pagination Handler
             |
             v
       Data Validation
             |
             v
        JSON Storage
             |
             v
         posts.json

API Used

This project uses the public JSONPlaceholder REST API for learning and testing.

Endpoint:https://jsonplaceholder.typicode.com/posts

The API provides sample post data in JSON format.

Project Structure
async-api-data-collector/
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   └── collector.py
│
├── data/
│   └── posts.json
│
├── tests/
│   └── test_main.py
│
├── .gitignore
├── requirements.txt
└── README.md

Installation

1. Clone the repository
git clone https://github.com/pailaraghunathreddy21-afk/-async-api-data-collector.git
cd -async-api-data-collector

2. Create a virtual environment
python3 -m venv .venv

3. Activate the virtual environment
macOS/Linux: source .venv/bin/activate

4. Install dependencies
python3 -m pip install -r requirements.txt

Run the Project
Run the application using: python3 -m src.main
The collected data will be saved to: data/posts.json

Example Output

INFO - Page 1 collected: 10 posts
INFO - Page 2 collected: 10 posts
INFO - Page 3 collected: 10 posts
INFO - Page 4 collected: 10 posts
INFO - Page 5 collected: 10 posts
INFO - Total posts collected: 100
INFO - Unique records: 100
INFO - Data saved to data/posts.json
INFO - Collection completed in 0.26 seconds

The order of page completion may vary because requests are executed asynchronously.

Pagination

The application requests data in pages.

For example:

Page 1  → 10 records
Page 2  → 10 records
Page 3  → 10 records
...
Page 10 → 10 records
Page 11 → 0 records

When an empty page is received, the collector stops requesting additional pages.

Error Handling and Retries

The collector attempts a failed request up to 3 times.

Attempt 1
   ↓
Failed
   ↓
Attempt 2
   ↓
Failed
   ↓
Attempt 3
   ↓
Success / Final Failure

The application also handles HTTP errors and aiohttp.ClientError exceptions.

Data Validation

Before saving the collected data, the application verifies that each record contains the required fields:
userId
id
title
body

The project also reports the number of unique records collected.

Testing

Run the automated tests using:

python3 -m pytest -q

Expected result:
3 passed
Performance

The application uses asynchronous requests and concurrent page fetching to improve API data collection efficiency.

Example execution:
Total posts collected: 100
Unique records: 100
Collection completed in 0.26 seconds

Execution time can vary depending on network conditions and API response time.

Learning Outcomes

Through this project, I learned:

* Python asynchronous programming
* asyncio
* aiohttp
* REST API communication
* Concurrent API requests
* API pagination
* Retry mechanisms
* Exception handling
* JSON data processing
* Data validation
* Automated testing
* Performance measurement
* Git and GitHub

Future Improvements

Possible future improvements include:

* Command-line arguments
* Configurable API URLs
* Progress indicators
* Advanced retry strategies
* Database storage
* CSV export
* API authentication
* Data analytics dashboard
* Docker deployment
* Scheduled data collection

Author

Paila Raghunath Reddy

B.Tech Computer Science Engineering — Data Science



