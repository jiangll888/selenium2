from selenium import webdriver
from config import settings

class BrowserEngine:
    def __init__(self,browser_type):
        self.browser = browser_type

    def start_browser(self):
        if self.browser == "chrome":
            option = webdriver.ChromeOptions()
            option.add_argument("disable-infobars")
            driver = webdriver.Chrome(chrome_options=option,executable_path=settings.CHROME_PATH)
        elif self.browser == "firefox":
            driver = webdriver.Firefox(executable_path=settings.FIREFOX_PATH)
        else:
            driver = webdriver.Edge(executable_path=settings.EDGE_PATH)
        return driver

