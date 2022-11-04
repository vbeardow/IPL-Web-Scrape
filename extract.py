from ipl_web_scrape.driver import setup_driver
from ipl_web_scrape.extract_actions import get_links, get_batting_scorecard
from ipl_web_scrape.base_page import MatchSchedulePage

# Setup chrome webdriver for match page
browser = setup_driver(MatchSchedulePage())

# Extract links
locator = "a[class='ds-no-tap-higlight']"
link_text = "indian-premier-league"
links = get_links(browser, locator, link_text)

# for link in links
batting_score_card = get_batting_scorecard(links[0])

print(batting_score_card[0])
print(batting_score_card[1])

browser.quit()
