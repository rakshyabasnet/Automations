from selenium.webdriver import Chrome
from libaryfiles.ConfigReader import configRead


def startBrowser():
    global driver
    driver=Chrome()
    driver.get(configRead('Details', 'App_URL'))
    driver.get("https://www.facebook.com/r.php")

    driver.maximize_window()
    return driver

def closeBrowser():
    driver.close()