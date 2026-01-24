import configparser

def configRead(section,key):
    config=configparser.ConfigParser
    config.read('../ConfigurationFiles/Config.cfg')
    return config.get(section, key)
print(configRead('Details', 'App_URL'))