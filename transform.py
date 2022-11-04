import pandas as pd

from ipl_web_scrape.transform_actions import clean_dataframe, groupby_player


def transform():

    df = pd.read_csv("./data/batting_scores.csv")

    new_df = clean_dataframe(df)

    # print(new_df.head())

    grouped_df = groupby_player(new_df)

    print(grouped_df.head())


transform()
