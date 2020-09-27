from selenium.webdriver.common.keys import Keys
from browser.browser import Browser

chrome = Browser()  # CREATE BROWSER OBJECT
url = "https://www.github.com"  # SET URL
chrome.Launch(url=url, browser="Chrome")  # LAUNCH BROWSER + LOAD URL

# LOCATE THE SEARCH BOX IN THE HEADER PANEL
search = chrome.driver.find_element_by_xpath("//input[contains(@placeholder, 'Search')]")  # FIND ELEMENT
search.send_keys("python/cpython")  # SEARCH FOR THE GIVEN REPO
search.send_keys(Keys.ENTER)  # HIT ENTER TO PROCEED

# LOCATE THE FIRST REPO (RESULT)
firstRepo = chrome.driver.find_element_by_xpath("(//li//em//..)[1]")  # GET THE FIRST REPO
firstRepo.click()  # CLICK ON THE FIRST REPO

# ASSERT THE CURRENT PAGE (MAKE SURE IT IS THE RIGHT URL)
assertPageUrl = chrome.getPageURL() == "https://github.com/python/cpython"
print("> ASSERT CURRENT URL RESULT: {0}".format(assertPageUrl))
print("> CURRENT URL: " + chrome.getPageURL())

# MAKE SURE ALL 5 IMAGES (UNDER THE README SECTION) ARE VISIBLE (EXISTENCE TEST)
for index in range(1,6):
    image = chrome.driver.find_element_by_xpath("//div[@id='readme']//a[{0}]//img[1]".format(index))
    existence  = image.is_displayed()
    print("EXISTENCE RESULT FOR IMAGE#{0} : {1} ".format(index,existence))

# MAKE SURE THE TEXT (UNDER THE README SECTION) IS VISIBLE (EXISTENCE TEST)
text = chrome.driver.find_element_by_xpath("(//div[@id='readme']//p)[1]")
existence = text.is_displayed()
print("TEXT '{0}' EXISTENCE RESULT: {1}".format(text.text, existence))