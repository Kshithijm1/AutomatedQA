import logging

# Setup basic logging configuration
def setup_logging():
    logging.basicConfig(
        level=logging.INFO,  # Set log level to INFO
        format='%(asctime)s - %(levelname)s - %(message)s',  # Define log message format
        handlers=[
            logging.FileHandler("automation.log"),  # Log messages to a file
            logging.StreamHandler()  # Log messages to the console
        ]
    )

# Enable debug level logging
def enable_debug_logging():
    logging.getLogger().setLevel(logging.DEBUG)  # Set log level to DEBUG
    logging.debug("Debug logging enabled.")  # Log a debug message

# Setup remote logging handler
def setup_remote_logging():
    logging.info("Setting up remote logging...")  # Log information about remote logging setup
    remote_handler = logging.StreamHandler()  # Example remote handler (StreamHandler used for simplicity)
    remote_handler.setLevel(logging.INFO)  # Set remote handler log level to INFO
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')  # Define log message format
    remote_handler.setFormatter(formatter)  # Set the formatter for the remote handler
    logging.getLogger().addHandler(remote_handler)  # Add remote handler to the root logger
    logging.info("Remote logging setup completed.")  # Log completion of remote logging setup
