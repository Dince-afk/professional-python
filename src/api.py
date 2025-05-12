import logging
import requests

from src.utils.cache import dev_cache


@dev_cache
def fetch_data():
    """
    Fetch data from the API and return it as a JSON object. as
    """
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/todos")
        response.raise_for_status()
        logging.info(f"Response status: {response.status_code}")
        return response.json()
    except Exception as e:
        raise e
