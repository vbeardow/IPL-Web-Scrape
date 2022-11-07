from ipl_web_scrape.load_actions import SQLite
import pandas as pd


def load():

    # Set table name
    table = "batting_scores"

    # Create new SQLite instance
    batting_db = SQLite("IPL_WebScrape.db")

    # Fetch data from csv
    data = pd.read_csv("./data/grouped_batting_scores.csv", index_col=False)

    # Insert record into db table
    batting_db.insert_record(table, data)

    # Commit and close connection
    batting_db.commit()
    batting_db.close_connection()


load()
