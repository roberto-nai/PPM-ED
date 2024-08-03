from pathlib import Path
import pandas as pd
def extract_files(folder: str, extension: str) -> list:
    """
    Extracts all file names with a given extension from a specified folder.

    Args:
        folder (str): The path to the folder in which to search for files.
        extension (str): The extension of the files to extract (including the dot, e.g., ".txt").

    Returns:
        List[str]: A list of file names with the specified extension, or an empty list if the folder is invalid.
    """
    folder_path = Path(folder)
    
    # Check that the folder exists and is a directory
    if not folder_path.is_dir():
        print(f"The path '{folder}' is not a valid directory.")
        return []

    # Search for all files with the specified extension and extract their names
    filenames_with_extension = [file.name for file in folder_path.glob(f'*{extension}')]
    
    return filenames_with_extension


def convert_seconds_to_hours(seconds):
    minutes = seconds / 60
    hours = minutes / 60
    return minutes, hours


def find_min_max_timestamp(df: pd.DataFrame, column: str) -> dict:
    """
    Finds the minimum and maximum values in a TIMESTAMP column of a DataFrame.
    
    Parameters:
    - df: The DataFrame containing the data.
    - column: The name of the column containing the timestamps.
    
    Returns:
    - A tuple containing the minimum and maximum values.
    """
    # Ensure the column is in datetime format
    df[column] = pd.to_datetime(df[column])
    
    # Find the minimum and maximum values
    min_timestamp = df[column].min()
    max_timestamp = df[column].max()
    
    dic_min_max = {"min_timestamp":min_timestamp, "max_timestamp":max_timestamp}
    
    return dic_min_max