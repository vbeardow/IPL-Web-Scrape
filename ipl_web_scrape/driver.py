from ipl_web_scrape.base_page import MatchSchedulePage


def setup_driver():
    browser = MatchSchedulePage()
    browser.go()

    return browser
