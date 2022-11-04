from selenium import webdriver


class BasePage:
    """Base page object representing a web page with a driver and actions to go to webpage and quit browser"""

    url = None

    def __init__(self) -> None:
        """Initiate page driver as a chrome webdriver"""
        self.driver = webdriver.Chrome()

    def go(self) -> None:
        """Navigate to webpage url"""
        self.driver.get(self.url)

    def quit(self):
        """Close browser"""
        self.driver.quit()


class MatchSchedulePage(BasePage):
    """IPL Match Schedule page"""

    url = "https://www.espncricinfo.com/series/indian-premier-league-2022-1298423/match-schedule-fixtures-and-results"
