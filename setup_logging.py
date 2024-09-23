import logging


def setup_logging():
    """
    Set up logging configuration.
    This function configures the logging module to log messages with a specific format and level.
    It sets up two handlers: one to log messages to a file named "postcode_validator.log" and another to log messages to the console.
    """

    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler("postcode_validator.log"),  # Log to file
            logging.StreamHandler(),  # Log to console
        ],
    )
