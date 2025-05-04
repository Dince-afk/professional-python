import sys
import logging
import pandas as pd

from src.utils.logger import setup_logger
from src.api import fetch_data


def main():

    setup_logger()

    logging.info("Starting script...")
    try:
        logging.info("Fetching data...")
        data = fetch_data()

        logging.info("Converting JSON to DataFrame...")
        todos_df = pd.DataFrame(data)

        logging.info("Saving todos to Excel...")
        todos_df.to_excel("todos.xlsx", index=False, sheet_name="Todos")

        logging.info("Script completed successfully.\n")
        return 0

    except Exception:
        logging.exception("An error occurred:")
        return 1


if __name__ == "__main__":
    sys.exit(main())
