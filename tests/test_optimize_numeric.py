import pandas as pd
import numpy as np
from group_32.optimize_numeric import optimize_numeric
import pytest


def test_optimize_numeric():
    """
    Test the optimize_numeric function to ensure it correctly downcasts
    numeric columns to more memory-efficient dtypes.
    """
    # Create a sample DataFrame with various numeric types
    df = pd.DataFrame({
        "int_col": np.array([1, 2, 3], dtype=np.int64),
        "big_int_col": np.array([1000, 2000, 3000], dtype=np.int64),
        "float_col": np.array([0.1, 0.2, 0.3], dtype=np.float64),
        "non_numeric": ["a", "b", "c"]
    })

    # Optimize the DataFrame
    optimized_df = optimize_numeric(df)

    # Check that the dtypes have been downcasted appropriately
    assert optimized_df["int_col"].dtype == np.int8
    assert optimized_df["big_int_col"].dtype == np.int16
    assert optimized_df["float_col"].dtype == np.float32
    assert optimized_df["non_numeric"].dtype == object


def test_columns_with_missing_values():
    """
    Test that columns containing missing values (NaN) are handled
    correctly without raising errors.
    """
    df = pd.DataFrame({
        "int_col": [1, 2, None],
        "float_col": [1.0, None, 3.0]
    })

    result = optimize_numeric(df)

    assert result.isna().sum().sum() == df.isna().sum().sum()


def test_no_numeric_columns():
    """
    Test that the function works correctly when there are
    no numeric columns in the DataFrame.
    """
    df = pd.DataFrame({
        "a": ["x", "y", "z"],
        "b": ["foo", "bar", "baz"]
    })

    result = optimize_numeric(df)

    pd.testing.assert_frame_equal(result, df)

















def test_integer_columns_are_downcasted_only():
    """
    Ensure that integer columns are downcasted, and that the function
    does not modify non-numeric columns in any way.
    """
    df = pd.DataFrame({
        "int_col": np.array([1, 2, 3], dtype=np.int64),
        "cat_col": ["a", "b", "c"]
    })

    result = optimize_numeric(df)

    # Integer column should remain integer
    assert pd.api.types.is_integer_dtype(result["int_col"])
    pd.testing.assert_series_equal(result["int_col"], df["int_col"])

    # Non-numeric column should be unchanged
    pd.testing.assert_series_equal(result["cat_col"], df["cat_col"])


def test_float_columns_are_downcasted_only():
    """
    Verify that float columns are optimized while non-numeric
    columns are not affected.
    """
    df = pd.DataFrame({
        "float_col": np.array([1.5, 2.5, 3.5], dtype=np.float64),
        "cat_col": ["x", "y", "z"]
    })

    result = optimize_numeric(df)

    assert pd.api.types.is_float_dtype(result["float_col"])
    np.testing.assert_allclose(result["float_col"], df["float_col"], rtol=1e-6)
    pd.testing.assert_series_equal(result["cat_col"], df["cat_col"])


def test_mixed_numeric_columns_are_handled_independently():
    """
    Confirm that integer and float columns are both optimized
    independently within the same DataFrame.
    """
    df = pd.DataFrame({
        "int_col": np.array([10, 20, 30], dtype=np.int64),
        "float_col": np.array([1.1, 2.2, 3.3], dtype=np.float64)
    })

    result = optimize_numeric(df)

    assert pd.api.types.is_integer_dtype(result["int_col"])
    assert pd.api.types.is_float_dtype(result["float_col"])
    pd.testing.assert_series_equal(result["int_col"], df["int_col"])
    np.testing.assert_allclose(result["float_col"], df["float_col"], rtol=1e-6)


def test_missing_values_preserved_for_numeric_columns():
    """
    Ensure that missing values in numeric columns are preserved
    after optimization.
    """
    df = pd.DataFrame({
        "int_col": [1, None, 3],
        "float_col": [1.0, np.nan, 3.0],
        "cat_col": ["a", "b", "c"]
    })

    result = optimize_numeric(df)

    assert result["int_col"].isna().sum() == df["int_col"].isna().sum()
    assert result["float_col"].isna().sum() == df["float_col"].isna().sum()
    pd.testing.assert_series_equal(result["cat_col"], df["cat_col"])


def test_no_numeric_columns_does_not_alter_dataframe():
    """
    Verify that the function does not alter the DataFrame
    when no numeric columns are present.
    """
    df = pd.DataFrame({
        "cat1": ["a", "b", "c"],
        "cat2": ["x", "y", "z"]
    })

    result = optimize_numeric(df)

    pd.testing.assert_frame_equal(result, df)
