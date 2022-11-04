from ipl_web_scrape.pickle_actions import pickle_load
from ipl_web_scrape.extract_actions import get_batting_scorecard

# Unload links from pickle
pick_path = "C:\\temp\\perf_data.pkl"
links = pickle_load(pick_path)

# for link in links
batting_score_card = get_batting_scorecard(links[0])

print(batting_score_card[0])
print(batting_score_card[1])
