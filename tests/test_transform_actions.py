import pandas as pd
import pytest
from ipl_web_scrape.transform_actions import (
    drop_null_rows,
    drop_other_rows,
    drop_cols,
    rename_cols,
    out_column,
)


@pytest.fixture
def dataframe():
    df = pd.read_csv("./data/batting_scores.csv")
    return df


def test_drop_null_rows(dataframe: pd.DataFrame):
    df = drop_null_rows(dataframe)
    assert df.isnull().all(axis=1).sum() == 0


def test_drop_other_rows(dataframe: pd.DataFrame):
    df = drop_other_rows(dataframe)
    assert (
        len(df[df["BATTING"].str.contains("Extras|TOTAL|Did not bat|Fall of wicket")])
        == 0
    )


def test_drop_cols(dataframe: pd.DataFrame):
    df = drop_cols(dataframe)
    unnamed_columns = [col for col in df.columns if "Unnamed" in col]
    assert len(unnamed_columns) == 0


def test_rename_cols(dataframe: pd.DataFrame):
    df = rename_cols(dataframe)
    column_names = {"Batsman", "Status", "Runs", "Balls", "Maidens", "Fours", "Sixes"}
    assert column_names.issubset(set(df.columns))


def test_out_columns(dataframe: pd.DataFrame):
    # df = out_column(dataframe)
    # assert isinstance(df['Out'].dtype, str)
    pass
