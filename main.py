import logging
import pandas as pd

from src.utils.logger import setup_logging
from src.api import fetch_data
from src.data import clean_data, transform_data


def main():
    try:
        setup_logging()
        logging.info("Starting script...")
        logging.info("Fetching data...")
        data = fetch_data()

        logging.info("Converting JSON to DataFrame...")
        todos_df = pd.DataFrame(data)

        todos_df = clean_data(todos_df)
        todos_df = transform_data(todos_df)

        logging.info("Saving todos to Excel...")

        todos_df.to_excel("todos.xlsx", index=False, sheet_name="Todos")

        logging.info("Script completed successfully.\n")

    except Exception as e:
        logging.error(e, exc_info=True)


if __name__ == "__main__":
    main()
