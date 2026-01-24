from Basefiles.InitiateDriver import startBrowser, closeBrowser

def test_validateRegistration():
    driver=startBrowser()
    driver.find_element('xpath', "//input[@name='firstname']").send_keys("Deekshya")
    closeBrowser()