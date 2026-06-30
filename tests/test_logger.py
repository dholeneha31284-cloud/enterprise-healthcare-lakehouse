from config.logging_config import get_logger

logger = get_logger(__name__)

logger.info("Pipeline Started")

logger.warning("This is a warning.")

logger.error("This is an error.")

print("Logging completed.")