import pandas as pd
import logging


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    # Change column type to object for column: 'id'
    logging.info("Start cleaning data")
    df = df.reindex(columns=[col for col in df.columns if col != "userId"] + ["userId"])
    # print(df)
    # df = df.reindex(columns=[col for col in df.columns if col != "userId"] + ["userId"])

    # df = df.astype({"id": "object"})
    return df


def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    logging.info("Start transforming data")
    print(df)
    print(df.groupby("userId").describe().droplevel(1), on="userId")
    print(df.join(df.groupby("userId").describe(), on="userId", how="inner"))
    return df
