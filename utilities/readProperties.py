import configparser
#use the method and read the ini(initialization file)
config=configparser.RawConfigParser()
config.read(".\\Configurations/config.ini")

class ReadConfig:
    @staticmethod
    def getURL():
        url=config.get('common info','baseURL')
        return url
    @staticmethod
    def getUserEmail():
        username=config.get('common info','username')
        return username
    @staticmethod
    def getPassword():
        password=config.get('common info','password')
        return password

