from selenium.webdriver import Chrome, Edge, Firefox
from libaryfiles.ConfigReader import configRead

driver = None

def startBrowser():
    global driver

    if configRead('Details', 'browser') == 'chrome':
        driver = Chrome()
    elif configRead('Details', 'browser') == 'edge':
        driver = Edge()
    else:
        driver = Firefox()

    driver.get(configRead('Details', 'APP_URL'))
    return driver


def closeBrowser():
    global driver
    if driver is not None:
        driver.quit()






# from selenium .webdriver import Chrome,Edge,Firefox
# from libraryfiles.ConfigReader import configRead

# def stfartBrowser():
#     global driver
#     if configRead('Details','browser')=='chrome':
#         driver=Chrome()
#     elif configRead('Details','browser')=='edge':
#         driver=Edge()
#     else:
#         driver=Firefox()
#     driver.get(configRead('Details' ,'APP_URL'))
#     driver.maximize_window()
#     return driver

# def closeBrowser(driver):
#     driver.quit()