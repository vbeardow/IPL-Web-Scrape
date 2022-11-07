import pandas as pd

from ipl_web_scrape.transform_actions import clean_dataframe, groupby_player


def transform():

    df = pd.read_csv("./data/batting_scores.csv")

    cleaned_df = clean_dataframe(df)
    grouped_df = groupby_player(cleaned_df)

    temp_df = grouped_df.loc[grouped_df["Batsman"] == "Alzarri Joseph"]
    print(temp_df)

    cleaned_df.to_csv("./data/cleaned_batting_scores.csv")
    grouped_df.to_csv("./data/grouped_batting_scores.csv")


transform()
