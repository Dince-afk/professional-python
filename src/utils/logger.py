import logging


def setup_logging():
    """
    Sets up logging to console and to log.log file.
    """
    logging.basicConfig(
        level="INFO",
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[logging.StreamHandler(), logging.FileHandler("log.log", mode="w")],
    )
