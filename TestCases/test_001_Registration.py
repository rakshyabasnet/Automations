from Basefiles.InitiateDriver import startBrowser, closeBrowser
from libaryfiles.ConfigReader import ElementsRead


def test_validateRegistration():
    driver = startBrowser()
    
    # Example: Fill first name field (update XPATH)
   # driver.find_element(By.XPATH, "//input[@name='firstname']").send_keys("Rakshya")
    driver.find_element('name',ElementsRead('Registration','fname')).send_keys('Rakshya')
    driver.find_element('name',ElementsRead('Registration','lname')).send_keys('Basnet') 
    closeBrowser(driver)
