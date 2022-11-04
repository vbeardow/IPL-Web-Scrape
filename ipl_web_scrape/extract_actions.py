import pandas as pd
from selenium.webdriver.common.by import By
from ipl_web_scrape.base_page import BasePage


def get_matches(browser: BasePage, selector: str, link_text: str):
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


def get_batting_scorecard(link: str):

    try:
        tables = pd.read_html(link)
    except:
        raise Exception(f"Could not read html with link {link}")

    return [tables[0], tables[2]]
