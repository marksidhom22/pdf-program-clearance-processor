import logging
import os

class LoggerSetup:
    """Sets up logging for the application."""
    @staticmethod
    def setup_logging(output_dir):
        log_filename = os.path.join(output_dir, "process.log")
        logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        logger = logging.getLogger()
        handler = logging.StreamHandler()
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger
