import logging
import requests
import pandas as pd

logging.basicConfig(
    level="INFO",
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(), logging.FileHandler("log.log", mode="a")],
)

logging.info("Starting script...")

try:
    logging.info("Loading todos...")
    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    response.raise_for_status()
    logging.info(f"Response status: {response.status_code}")

    logging.info("Converting JSON to DataFrame...")
    todos_df = pd.DataFrame(response.json())
    logging.info(f"DataFrame columns: {todos_df.columns}")

    logging.info("Saving todos to Excel...")
    todos_df.to_excel("todos.xlsx", index=False, sheet_name="Todos")
    logging.info("Todos saved to Excel successfully.")

except requests.exceptions.HTTPError:
    logging.exception("HTTP error occurred:")
except Exception:
    logging.exception("An error occurred:")


logging.info("Script completed successfully.\n")
