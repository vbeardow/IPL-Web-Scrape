from ipl_web_scrape.pickle_actions import pickle_dump, pickle_load
from ipl_web_scrape.driver import setup_driver
from ipl_web_scrape.extract_actions import get_matches, get_batting_scorecard

# Setup chrome webdriver for match page
browser = setup_driver()

# Extract links
locator = "a[class='ds-no-tap-higlight']"
link_text = "indian-premier-league"
links = get_matches(browser, locator, link_text)

# Dump list of links to pickle file
pick_path = "C:\\temp\\perf_data.pkl"
pickle_dump(links, pick_path)

browser.quit()
