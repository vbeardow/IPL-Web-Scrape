import pytest
from unittest.mock import patch
from ipl_web_scrape.extract_actions import get_matches, get_batting_scorecard
from ipl_web_scrape.driver import setup_driver
from ipl_web_scrape.base_page import BasePage


@pytest.fixture
def browser():
    return setup_driver()


@pytest.fixture
def match_link():
    return "https://www.espncricinfo.com/series/indian-premier-league-2022-1298423/chennai-super-kings-vs-kolkata-knight-riders-1st-match-1304047/full-scorecard"


def test_get_matches_not_zero(browser: BasePage):
    selector = "a[class='ds-no-tap-higlight']"
    link_text = "indian-premier-league"
    links = get_matches(browser, selector, link_text)
    assert len(links) != 0


def test_get_matches_driver_error(browser: BasePage):
    browser.driver = "x"
    selector = "test_selector"
    link_text = "indian-premier-league"
    with pytest.raises(
        Exception,
        match=f"Could not apply the function find_elements to your driver. Check your driver.",
    ):
        get_matches(browser, selector, link_text)


def test_get_matches_selector_error(browser: BasePage):
    selector = "test_selector"
    link_text = "indian-premier-league"
    with pytest.raises(
        Exception, match=f"Could not find any elements with selector {selector}"
    ):
        get_matches(browser, selector, link_text)


def test_get_matches_link_text_error(browser: BasePage):
    selector = "a[class='ds-no-tap-higlight']"
    link_text = "test_link_text"
    with pytest.raises(
        Exception,
        match=f"Could not find any elements with href attribute containing {link_text}",
    ):
        get_matches(browser, selector, link_text)


def get_batting_scorecard_from_link(match_link: str):
    tables = get_batting_scorecard(match_link)
    assert len(tables) == 2
