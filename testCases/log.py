import logging

logging.basicConfig(filename="../logs/" + "test_homePageTitle.log", filemode="w", format="%(name)s - %(levelname)s - %(message)s")
logging.warning("This will get logged to a file")
