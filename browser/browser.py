from selenium import webdriver


class Browser:
    driver = None  # HOLDS THE CHOSEN BROWSER

    def __init__(self):
        # CONSTRUCTOR
        pass

    def Launch(self, browser="F", url=""):
        # Instantiate the browser Command
        if browser.lower() == "firefox" or browser.lower() == "f":
            print("LAUNCHING FIREFOX...")
            self.driver = webdriver.Firefox()  # Starts webElement new local session of Firefox.

        elif browser.lower() == "chrome" or browser.lower() == "c":
            print("LAUNCHING CHROME...")
            self.driver = webdriver.Chrome()  # Creates webElement new instance of the chrome drive

        elif browser.lower() == "edge" or browser.lower() == "e":
            print("LAUNCHING EDGE...")
            self.driver = webdriver.Edge()  # Creates webElement new instance of the chrome drive

        elif browser.upper() == "GHOST MODE":
            print("GHOST MODE...")
            from selenium.webdriver.chrome.options import Options
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--window-size=1920x1080")
            self.driver = webdriver.Chrome(chrome_options=chrome_options)

        self.driver.get(url)

        self.driver.implicitly_wait(1)

    def navigate(self, command):
        if command.upper() == "BACK" or command.upper() == "B" \
                or command.upper() == "PREVIOUS" or command.upper() == "P":
            self.driver.back()
        elif command.upper() == "FORWARD" or command.upper() == "F" \
                or command.upper() == "NEXT" or command.upper() == "N":
            self.driver.forward()
        elif command.upper() == "REFRESH" or command.upper() == "RELOAD" or command.upper() == "R":
            self.refreshPage()
        elif command.__contains__("http"):
            self.launchURL(command)

    def getPageTitle(self):
        pageTitle = self.driver.title
        return pageTitle

    def getPageURL(self):
        pageURL = self.driver.current_url
        return pageURL

    def refreshPage(self):
        self.driver.refresh()
        self.driver.find_element_by_id().send_keys()
