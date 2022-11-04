from selenium import webdriver


class BasePage:

    url = None

    def __init__(self) -> None:
        self.driver = webdriver.Chrome()

    def go(self):
        self.driver.get(self.url)

    def quit(self):
        self.driver.quit()


class MatchSchedulePage(BasePage):

    url = "https://www.espncricinfo.com/series/indian-premier-league-2022-1298423/match-schedule-fixtures-and-results"
