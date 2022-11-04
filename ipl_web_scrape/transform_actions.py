import pandas as pd


def drop_null_rows(df: pd.DataFrame) -> pd.DataFrame:

    df.dropna(how="all", inplace=True)

    return df


def drop_other_rows(df: pd.DataFrame) -> pd.DataFrame:

    col_name = [col for col in df.columns if "bat" in col.lower()][0]
    df = df[
        df[col_name].str.contains("Extras|TOTAL|Did not bat|Fall of wickets") == False
    ]

    return df


def drop_cols(df: pd.DataFrame) -> pd.DataFrame:

    unnamed_cols = [col for col in df.columns if "Unnamed" in col]
    df.drop(labels=unnamed_cols, axis="columns", inplace=True)

    return df


def rename_cols(df: pd.DataFrame) -> pd.DataFrame:

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
    df["Out"] = df["Status"].str.contains("not out")

    return df


def groupby_player(df: pd.DataFrame) -> pd.DataFrame:
    df = df.groupby("Batsman")[["Batsman", "Runs", "Balls", "Fours", "Sixes"]]
    return df


def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:

    df = rename_cols(df)
    df = drop_cols(df)
    df = drop_null_rows(df)
    df = drop_other_rows(df)
    df = out_column(df)

    return df
