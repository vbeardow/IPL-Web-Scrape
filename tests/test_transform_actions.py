import pandas as pd
import pytest
from ipl_web_scrape.transform_actions import (
    drop_null_rows,
    drop_named_rows,
    drop_unnamed_cols,
    drop_named_columns,
    clean_batsman_names,
    rename_cols,
    out_column,
    groupby_player,
)


@pytest.fixture(scope="class")
def raw_dataframe():
    data = {
        "BATTING": [
            "Player 1 (c) †",
            "Extras",
            None,
            "TOTAL",
            "Did not bat",
            "Fall of wickets",
        ],
        "Unnamed: 1": ["out", "not out", None, "out", "not out", "out"],
        "R": [30, 45, None, 20, 18, 12],
        "B": [4, 16, None, 1, 10, 11],
        "M": [0, 2, None, 1, 0, 0],
        "4s": [1, 3, None, 1, 2, 3],
        "6s": [1, 0, None, 1, 1, 0],
        "SR": [1.0, 1.0, None, 2.3, 2.4, 5.4],
    }
    df = pd.DataFrame(data)
    return df


@pytest.fixture(scope="class")
def renamed_df():
    data = {
        "Batsman": [
            "Player 1 (c) †",
            "Extras (c)",
            None,
            "TOTAL",
            "Did not bat",
            "Fall of wickets",
        ],
        "Status": ["out", "not out", None, "out", "not out", "out"],
        "Runs": [30, 45, None, 20, 18, 12],
        "Balls": [4, 16, None, 1, 10, 11],
        "Fours": [1, 3, None, 1, 2, 3],
        "Sixes": [1, 0, None, 1, 1, 0],
    }
    df = pd.DataFrame(data)
    return df


@pytest.fixture
def cleaned_df():
    data = {
        "Batsman": ["Player 1", "Player 1"],
        "Status": ["out", "not out"],
        "Runs": [4, 5],
        "Balls": [2, 3],
        "Fours": [1, 2],
        "Sixes": [0, 3],
        "Out": [True, False],
    }
    df = pd.DataFrame(data)
    return df


def test_drop_null_rows(raw_dataframe: pd.DataFrame):
    df = drop_null_rows(raw_dataframe)
    assert df.isnull().all(axis=1).sum() == 0


def test_drop_named_rows(renamed_df: pd.DataFrame):
    df = drop_named_rows(renamed_df)
    assert (
        len(df[df["Batsman"].str.contains("Extras|TOTAL|Did not bat|Fall of wickets")])
        == 0
    )


def test_drop_unnamed_cols(raw_dataframe: pd.DataFrame):
    df = drop_unnamed_cols(raw_dataframe)
    unnamed_columns = [col for col in df.columns if "Unnamed" in col]
    assert len(unnamed_columns) == 0


def test_drop_named_cols(raw_dataframe: pd.DataFrame):
    df = drop_named_columns(raw_dataframe)
    assert ("M|SR" in df.columns) == False


def test_rename_cols(raw_dataframe: pd.DataFrame):
    df = rename_cols(raw_dataframe)
    column_names = ["Batsman", "Status", "Runs", "Balls", "M", "Fours", "Sixes", "SR"]
    assert df.columns.to_list() == column_names


def test_clean_batsman_names(renamed_df: pd.DataFrame):
    df = clean_batsman_names(renamed_df)
    assert df["Batsman"].str.findall("(c) |†").any() == False


def test_out_column(renamed_df: pd.DataFrame):
    df = out_column(renamed_df)
    assert df["Out"].to_list() == [True, False, True, True, False, True]


def test_groupby_player(cleaned_df: pd.DataFrame):
    df = groupby_player(cleaned_df)
    assert df.iloc[0].to_list() == ["Player 1", 9, 5, 3, 3, 1]
