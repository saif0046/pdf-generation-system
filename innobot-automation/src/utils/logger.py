import logging

def get_logger(name: str):
    """
    Initialize and return a formatted logger instance.
    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )
    return logging.getLogger(name)
