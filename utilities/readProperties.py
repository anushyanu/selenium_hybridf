import configparser
# it is a predefined package already present in the python, no need to install
config = configparser.RawConfigParser()
config.read(".//configurations//config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationUrl():
        url = config.get("common info","baseURL")
        return url
    @staticmethod
    def getUsername():
        username = config.get("common info", "username")
        return username
    @staticmethod
    def getPassword():
        password = config.get("common info", "password")
        return password
