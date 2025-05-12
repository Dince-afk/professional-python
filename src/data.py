import pandas as pd


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    # Change column type to object for column: 'id'
    print(df.columns.values.tolist())

    # Put the userId column at the end of the DataFrame

    # df = df.reindex(columns=[col for col in df.columns if col != "userId"] + ["userId"])

    df = df.astype({"id": "object"})
    return df
