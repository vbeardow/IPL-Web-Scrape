import pandas as pd
from selenium.webdriver.common.by import By
from ipl_web_scrape.base_page import BasePage
from typing import List


def get_links(browser: BasePage, selector: str, link_text: str) -> List[str]:
    """Extract list of links from webpage given selector and link text to search for within link

    Args:
        browser (BasePage): Base page object representing the web page and driver to navigate to
        selector (str): Selector indicating the html element to search for on the webpage
        link_text (str): String to search for in link to return

    Raises:
        Exception: raised if driver is not able to search for element, usually indicating driver error
        Exception: raised if no elements are found with given selector
        Exception: raised if no links are found containing given link text

    Returns:
        List[str]: list of links extracted from webpage
    """

    try:
        elems = browser.driver.find_elements(By.CSS_SELECTOR, selector)
    except:
        raise Exception(
            f"Could not apply the function find_elements to your driver. Check your driver."
        )

    if len(elems) == 0:
        raise Exception(f"Could not find any elements with selector {selector}")
    else:
        links = [
            elem.get_attribute("href")
            for elem in elems
            if link_text in elem.get_attribute("href")
        ]

    if len(links) == 0:
        raise Exception(
            f"Could not find any elements with href attribute containing {link_text}"
        )

    return links


def get_batting_scorecard(link: str) -> List[pd.DataFrame]:
    """Returns the 0th and 2nd index of tables from web page given url

    Args:
        link (str): url link to webpage to extract tables from

    Raises:
        Exception: raised if link is invalid and pd.read_html

    Returns:
        List[pd.DataFrame]: list of 2 dataframes representing batting tables on webpage
    """
    try:
        tables = pd.read_html(link)
    except:
        raise Exception(f"Could not read html with link {link}")

    return [tables[0], tables[2]]
