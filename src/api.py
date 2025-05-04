import logging
import requests


def fetch_data():
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/todos")
        response.raise_for_status()
        logging.info(f"Response status: {response.status_code}")
        return response.json()
    except requests.exceptions.HTTPError:
        logging.exception("HTTP error occurred:")
        return 1
