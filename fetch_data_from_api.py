import pandas as pd
from sodapy import Socrata
import logging

# Configuración del logging
logging.basicConfig(filename='etl_errors.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_data_from_api(app_token: str, username: str, password: str, endpoint: str, page_size: int = 2000) -> dict:
    """
    Fetches data from the specified API endpoint and returns it as a dictionary.
    
    Parameters:
    - app_token (str): The application token.
    - username (str): The API username.
    - password (str): The API password.
    - endpoint (str): The endpoint of the dataset.
    - page_size (int): The number of records per page. Default is 2000.
    
    Returns:
    - dict: A dictionary where the key is the endpoint name and the value is its associated DataFrame.
    """
    
    try:
        # Initialize an authenticated client
        client = Socrata("www.datos.gov.co", app_token, username=username, password=password)
    except Exception as e:
        logging.error(f"Authentication error for endpoint {endpoint}. Error: {str(e)}")
        return None

    try:
        # Determine the total number of records in the dataset
        count = client.get(endpoint, select="COUNT(*)")[0]["COUNT"]
    except Exception as e:
        logging.error(f"Error fetching total record count from endpoint {endpoint}. Error: {str(e)}")
        return None

    try:
        # Calculate the number of pages
        num_pages = -(-int(count) // page_size)  # Ceiling division

        # Retrieve all records
        all_records = []
        for i in range(num_pages):
            results = client.get(endpoint, offset=i*page_size, limit=page_size)
            all_records.extend(results)

        # Convert to DataFrame
        df = pd.DataFrame.from_records(all_records)

        return {endpoint: df}
    except Exception as e:
        logging.error(f"Error fetching data from page {i+1} of endpoint {endpoint}. Error: {str(e)}")
        return None

