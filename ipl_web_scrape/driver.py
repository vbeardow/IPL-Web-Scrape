from ipl_web_scrape.base_page import BasePage, MatchSchedulePage


def setup_driver(page: BasePage) -> BasePage:
    """Setup driver and navigate to url for given page object

    Args:
        page (BasePage): Page object representing a standard webpage

    Returns:
        BasePage: Return page object for specified page object instance
    """

    browser = page
    browser.go()

    return browser
