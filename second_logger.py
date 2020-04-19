import logging

logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)
logging.warning("the warning message:")
logging.info("the info message:")
logging.error("error messages")