import logging
import sys

def get_logger(name: str):
    """
    Initializes a logger with a specified name and returns it.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    # Create a handler to write log messages to stdout
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.INFO)
    
    # Create a formatter and add it to the handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    
    # Add the handler to the logger
    logger.addHandler(handler)
    
    return logger

# Example of using the logger
if __name__ == '__main__':
    logger = get_logger(__name__)
    logger.info("This is an informational message.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.") 