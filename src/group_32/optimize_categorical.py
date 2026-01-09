def optimize_categorical(df: pd.DataFrame, max_unique_ratio: float = 0.5) -> pd.DataFrame:
    """
    This function makes a copy of a DataFrame (df) and looks through all the string columns. 
    It counts the number of unique strings and calculates the ratio of the unique values to the total number of rows. 
    If this ratio is below a chosen threshold in this function, it converts the column to category dtype.
    This function returns a dataframe with the converted columns.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame containing string columns.

    max_unique_ratio : float, default=0.5
        The maximum ratio of (unique_values / total_rows) for categorical conversion.
        - 0.5 means convert if unique values are less than 50% of total rows
        - Lower values (e.g., 0.3) make conversion more conservative
        - Higher values (e.g., 0.7) make conversion more aggressive

    Returns
    -------
    pd.DataFrame
        The DataFrame with eligible string columns converted to category dtype.

    Notes
    -----
    - Only processes columns with 'object' dtype (typically strings)
    - Prints the number of columns successfully converted
    - Conversion is reversible using .astype('object') if needed
    - Categorical columns maintain the same values and ordering
    """