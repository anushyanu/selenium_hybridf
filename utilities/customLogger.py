import logging
class LogGen:
    @staticmethod
    def loggen():
        print("before config")
        logging.basicConfig(filename=".//logs/" + "automation.log",
                            filemode="w",force=True,
                            level=logging.DEBUG,
                            format="%(asctime)s: %(levelname)s: %(message)s",
                            datefmt='%Y/%m/%d %H:%M:%S')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        print("after config")
        return logger
