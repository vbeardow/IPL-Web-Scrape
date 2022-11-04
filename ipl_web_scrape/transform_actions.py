import pandas as pd
from typing import List


def drop_null_rows(df: pd.DataFrame) -> pd.DataFrame:
    """Drop rows in dataframe where all columns are null

    Args:
        df (pd.DataFrame): pandas dataframe to perform operation on

    Returns:
        pd.DataFrame: pandas dataframe table with null rows removed
    """

    df.dropna(how="all", inplace=True)

    return df


def drop_other_rows(df: pd.DataFrame) -> pd.DataFrame:
    """Drop rows where column contains string specified

    Args:
        df (pd.DataFrame): pandas dataframe to perform operation on

    Returns:
        pd.DataFrame: pandas dataframe with specified rows removed
    """

    df = df[
        df["Batsman"].str.contains("Extras|TOTAL|Did not bat|Fall of wickets") == False
    ]

    return df


def drop_unnamed_cols(df: pd.DataFrame) -> pd.DataFrame:
    """Drop

    Args:
        df (pd.DataFrame): pandas dataframe to perform operation on

    Returns:
        pd.DataFrame: pandas dataframe with unnamed columns removed
    """

    unnamed_cols = [col for col in df.columns if "Unnamed" in col]
    df.drop(labels=unnamed_cols, axis="columns", inplace=True)

    return df


def rename_cols(df: pd.DataFrame) -> pd.DataFrame:
    """Rename columns in dataframe to those specified within dictionary

    Args:
        df (pd.DataFrame): pandas dataframe to perform operation on

    Returns:
        pd.DataFrame: pandas dataframe with renamed columns
    """

    df.rename(
        columns={
            "BATTING": "Batsman",
            "Unnamed: 1": "Status",
            "R": "Runs",
            "B": "Balls",
            "M": "Maidens",
            "4s": "Fours",
            "6s": "Sixes",
        },
        inplace=True,
    )

    return df


def out_column(df: pd.DataFrame) -> pd.DataFrame:
    """Create column on dataframe with name Out, which is a boolean value representing if the player is out (True) or in (False)

    Args:
        df (pd.DataFrame): pandas dataframe to perform operation on

    Returns:
        pd.DataFrame: pandas dataframe with additional Out column
    """
    df["Out"] = df["Status"].str.contains("not out")

    return df


def groupby_player(df: pd.DataFrame) -> pd.DataFrame:
    """Group data by Batsman

    Args:
        df (pd.DataFrame): pandas dataframe to perform operation on

    Returns:
        pd.DataFrame: grouped pandas dataframe
    """
    df = (
        df.groupby("Batsman")[["Runs", "Balls", "Fours", "Sixes", "Out"]]
        .count()
        .reset_index()
    )

    return df


def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """Apply cleaning methods to dataframe and return cleaned dataframe

    Args:
        df (pd.DataFrame): pandas dataframe to perform operation on

    Returns:
        pd.DataFrame: cleaned pandas dataframe
    """

    df = rename_cols(df)
    df = drop_unnamed_cols(df)
    df = drop_null_rows(df)
    df = drop_other_rows(df)
    df = out_column(df)

    return df
