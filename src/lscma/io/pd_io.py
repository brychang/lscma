import pandas as pd

def read_csv(path):
    """
    Reads a CSV file into a Pandas DataFrame.
    
    Parameters:
    - path (str): Path to the CSV file.

    Returns:
    - pd.DataFrame: The DataFrame containing the CSV data.
    """
    return pd.read_csv(path, index_col=0)

def write_csv(path, df):
    """
    Writes a Pandas DataFrame to a CSV file.
    
    Parameters:
    - path (str): Path where the CSV file will be saved.
    - df (pd.DataFrame): The DataFrame to save.
    
    Returns:
    - None
    """
    df.to_csv(path)
