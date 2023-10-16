from typing import Optional

import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

SUPPORTED_SPARK_PARQUET_TIMESTAMP_PRECISION = "us"


def parquet_to_arrow(parquet: bytes) -> pa.Table:
    """Convert parquet as bytes to pyarrow table"""
    return pq.read_table(pa.py_buffer(parquet))


def arrow_to_parquet(table: pa.Table) -> bytes:
    """Convert pyarrow table to parquet as bytes"""
    buf = pa.BufferOutputStream()
    pq.write_table(table, buf)
    return buf.getvalue().to_pybytes()


def pandas_to_arrow(
    df: pd.DataFrame, schema: Optional[dict] = None, preserve_index: bool = False
) -> pa.Table:
    df = df.copy()
    if schema:
        arrow_schema = pa.schema(schema)
    else:
        arrow_schema = None

    # Due to spark not supporting nanosecond precision, we round to microseconds
    for column in df.select_dtypes(["datetime", "datetimetz"]).columns:
        df[column] = df[column].round(SUPPORTED_SPARK_PARQUET_TIMESTAMP_PRECISION)

    table = pa.Table.from_pandas(df, arrow_schema, preserve_index=preserve_index)

    # pandas may leave metadata, which we don't want
    table = table.replace_schema_metadata(None)

    return table


def arrow_to_pandas(table: pa.Table):
    df = table.to_pandas()
    return df


def pandas_to_parquet(df: pd.DataFrame, schema: Optional[dict] = None) -> bytes:
    table = pandas_to_arrow(df, schema)
    return arrow_to_parquet(table)


def parquet_to_pandas(parquet: bytes) -> pd.DataFrame:
    table = parquet_to_arrow(parquet)
    return arrow_to_pandas(table)
