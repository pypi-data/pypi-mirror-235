import logging.config
import os

import yaml


def get_logger(module: str):
    logger = logging.getLogger(module)

    # If log config file is set in the env, use the handlers from there,
    # Else, redirect to stdout
    logger_config_file = os.getenv("LOG_CONFIG_FILE")

    try:
        with open(logger_config_file, "r") as file:
            config = yaml.safe_load(file.read())
            logging.config.dictConfig(config)
    except Exception:
        if logger_config_file:
            logging.warning(
                f"Failed to create logger using the config file {logger_config_file}"
            )
        stream_handler = logging.StreamHandler()
        logger.addHandler(stream_handler)

        logger.info("No config found for logger. Redirecting to Standard output!")

    return logger
