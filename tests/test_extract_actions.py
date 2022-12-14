import pytest
import pandas as pd
from unittest.mock import patch
from ipl_web_scrape.extract_actions import (
    setup_driver,
    get_links,
    get_batting_scorecard,
)
from ipl_web_scrape.base_page import BasePage, MatchSchedulePage


@pytest.fixture
def browser():
    page = MatchSchedulePage()
    return setup_driver(page)


@pytest.fixture
def match_link():
    return "https://www.espncricinfo.com/series/indian-premier-league-2022-1298423/chennai-super-kings-vs-kolkata-knight-riders-1st-match-1304047/full-scorecard"


def test_get_links_not_zero(browser: BasePage):
    selector = "a[class='ds-no-tap-higlight']"
    link_text = "indian-premier-league"
    links = get_links(browser, selector, link_text)
    assert len(links) != 0


def test_get_links_driver_error(browser: BasePage):
    browser.driver = "driver"
    selector = "a[class='ds-no-tap-higlight']"
    link_text = "indian-premier-league"
    with pytest.raises(
        Exception,
        match=f"Could not apply the function find_elements to your driver. Check your driver.",
    ):
        get_links(browser, selector, link_text)


def test_get_links_selector_error(browser: BasePage):
    selector = "test_selector"
    link_text = "indian-premier-league"
    with pytest.raises(
        Exception, match=f"Could not find any elements with selector {selector}"
    ):
        get_links(browser, selector, link_text)


def test_get_links_link_text_error(browser: BasePage):
    selector = "a[class='ds-no-tap-higlight']"
    link_text = "test_link_text"
    with pytest.raises(
        Exception,
        match=f"Could not find any elements with href attribute containing {link_text}",
    ):
        get_links(browser, selector, link_text)


def test_get_batting_scorecard_from_link(match_link: str):
    tables = get_batting_scorecard(match_link)
    assert len(tables) == 2


def test_get_batting_scorecard_dataframe_size(match_link: str):
    tables = get_batting_scorecard(match_link)
    assert len(tables[0].columns) == 10
    assert len(tables[1].columns) == 10


def test_get_batting_scorecard_return_type(match_link: str):
    tables = get_batting_scorecard(match_link)
    assert isinstance(tables[0], pd.DataFrame)
    assert isinstance(tables[1], pd.DataFrame)


def test_get_batting_scorecard_invalid_link():
    link = "test_invalid_link"
    with pytest.raises(Exception, match=f"Could not read html with link {link}"):
        get_batting_scorecard(link)
