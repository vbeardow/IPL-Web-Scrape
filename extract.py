import itertools
import pandas as pd

from ipl_web_scrape.driver import setup_driver
from ipl_web_scrape.extract_actions import get_links, get_batting_scorecard
from ipl_web_scrape.base_page import MatchSchedulePage
from ipl_web_scrape.batting_table import BattingTable


def extract():
    # Setup chrome webdriver for match page
    browser = setup_driver(MatchSchedulePage())

    # Extract links
    locator = "a[class='ds-no-tap-higlight']"
    link_text = "indian-premier-league"
    links = get_links(browser, locator, link_text)

    list_tables = []
    for link in links:
        list_tables.append(get_batting_scorecard(link))

    flat_list_tables = list(itertools.chain(*list_tables))
    batting_scores = pd.concat(flat_list_tables)

    browser.quit()

    print(batting_scores.head())

    batting_scores.to_csv("./data/batting_scores.csv")
