from urllib import request

import pandas as pd
import itertools
import sys

import airflow
from airflow import DAG
from airflow.operators.python import PythonOperator

from ipl_web_scrape.base_page import MatchSchedulePage
from ipl_web_scrape.extract_actions import (
    setup_driver,
    get_links,
    get_batting_scorecard,
)
from ipl_web_scrape.transform_actions import clean_dataframe, groupby_player
from ipl_web_scrape.load_actions import SQLite

sys.path.append("/Users/Victoria.Beardow/DE-Crash-Course/IPL-Web-Scrape/ipl_web_scrape")


dag = DAG(
    dag_id="ipl-web-scrape",
    start_date=airflow.utils.dates.days_ago(1),
    schedule_interval="@weekly",
)


def _extract():
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


def _transform():

    df = pd.read_csv("./data/batting_scores.csv")

    cleaned_df = clean_dataframe(df)
    grouped_df = groupby_player(cleaned_df)

    cleaned_df.to_csv("./data/cleaned_batting_scores.csv")
    grouped_df.to_csv("./data/grouped_batting_scores.csv", index=False)


def _load():

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


extract = PythonOperator(task_id="extract", python_callable=_extract, dag=dag)

transform = PythonOperator(task_id="transform", python_callable=_transform, dag=dag)

load = PythonOperator(task_id="load", python_callable=_load, dag=dag)

extract >> transform >> load
