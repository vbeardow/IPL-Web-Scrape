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


def drop_named_rows(df: pd.DataFrame) -> pd.DataFrame:
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


def drop_named_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Drop column with column names 'M' and 'SR

    Args:
        df (pd.DataFrame): pandas dataframe to perform operation on

    Returns:
        pd.DataFrame: pandas dataframe without columns 'M' and 'SR
    """
    df.drop(columns="M", inplace=True)
    df.drop(columns="SR", inplace=True)

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
            "4s": "Fours",
            "6s": "Sixes",
        },
        inplace=True,
    )

    return df


def clean_batsman_names(df: pd.DataFrame) -> pd.DataFrame:
    df["Batsman"] = df["Batsman"].str.replace("\\xa0", " ")
    df["Batsman"] = df["Batsman"].str.strip("(c) |†|")
    return df


def out_column(df: pd.DataFrame) -> pd.DataFrame:
    """Create column on dataframe with name Out, which is a boolean value representing if the player is out (True) or in (False)

    Args:
        df (pd.DataFrame): pandas dataframe to perform operation on

    Returns:
        pd.DataFrame: pandas dataframe with additional Out column
    """
    df["Out"] = ~df["Status"].str.contains("not out", na=False)

    return df


def update_types(df: pd.DataFrame) -> pd.DataFrame:
    """Update data types of columns

    Args:
        df (pd.DataFrame): pandas dataframe to perform operation on

    Returns:
        pd.DataFrame: pandas dataframe with updated datatypes
    """
    df = df.astype(
        {"Runs": "int64", "Balls": "int64", "Fours": "int64", "Sixes": "int64"}
    )
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
        .sum()
        .reset_index()
    )
    df = update_types(df)

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
    df = drop_named_columns(df)
    df = drop_null_rows(df)
    df = drop_named_rows(df)
    df = clean_batsman_names(df)
    df = out_column(df)
    df = update_types(df)

    return df
