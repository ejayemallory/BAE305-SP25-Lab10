import pandas as pd

def get_unique_site_locations(file_path):
    """
    Reads a CSV file containing water quality measurement site data,
    filters for site names and displays unique location information.

    Parameters:
    - file_path (str): The path to the CSV file.

    Returns:
    - pd.DataFrame: A DataFrame with unique site names and locations.
    """
    # Load the CSV into a DataFrame
    df = pd.read_csv(file_path)

    # Display the first few rows to understand the structure (optional)
    print("First few rows of the dataset:")
    print(df.head())

    # Assuming columns like 'Site Name', 'Latitude', 'Longitude', or similar exist
    # You might need to adjust the column names based on your file
    site_info_columns = ['Site Name', 'Latitude', 'Longitude']  # update as necessary

    # Filter to just the relevant columns
    if all(col in df.columns for col in site_info_columns):
        unique_sites = df[site_info_columns].drop_duplicates()
        print("\nUnique water quality measurement site locations:")
        print(unique_sites)
        return unique_sites
    else:
        missing = [col for col in site_info_columns if col not in df.columns]
        print(f"Missing expected columns: {missing}")
        return pd.DataFrame()

# Example usage:
file_path = 'station.csv'
get_unique_site_locations(file_path)
