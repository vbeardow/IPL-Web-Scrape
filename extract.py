import itertools
import pandas as pd

from ipl_web_scrape.extract_actions import (
    setup_driver,
    get_links,
    get_batting_scorecard,
)
from ipl_web_scrape.base_page import MatchSchedulePage


def extract():
    # Setup chrome webdriver for match page
    browser = setup_driver(MatchSchedulePage())

    # Extract links
    locator = "a[class='ds-no-tap-higlight']"
    link_text = "indian-premier-league"
    links = get_links(browser, locator, link_text)

    # Loop through games and append each table to list_tables
    list_tables = []
    for link in links:
        list_tables.append(get_batting_scorecard(link))

    # Flatten list of tables
    flat_list_tables = list(itertools.chain(*list_tables))

    # Concat into one dataframe
    batting_scores = pd.concat(flat_list_tables)

    browser.quit()

    batting_scores.to_csv("./data/batting_scores.csv")


extract()
