import pandas as pd
from sodapy import Socrata
import logging

logging.basicConfig(filename='etl_errors.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_data_from_api(app_token: str, username: str, password: str, endpoint: str, page_size: int = 50000) -> dict:
    """
    Fetches all data from the specified API endpoint and returns it as a dictionary.

    Socrata's `get` returns only the first 1000 rows when no limit is given, so the records are read
    with `get_all`, which pages through the whole dataset.

    Parameters:
    - app_token (str): The application token.
    - username (str): The API username.
    - password (str): The API password.
    - endpoint (str): The endpoint of the dataset.
    - page_size (int): Rows requested per page. Default is 50000.

    Returns:
    - dict: A dictionary where the key is the endpoint name and the value is its associated DataFrame,
      or None if the request failed.
    """
    try:
        # Initialize an authenticated client
        client = Socrata("www.datos.gov.co", app_token, username=username, password=password)
    except Exception as e:
        logging.error(f"Authentication error for endpoint {endpoint}. Error: {str(e)}")
        return None

    try:
        all_records = list(client.get_all(endpoint, limit=page_size))
        df = pd.DataFrame.from_records(all_records)
        return {endpoint: df}
    except Exception as e:
        logging.error(f"Error fetching all data from endpoint {endpoint}. Error: {str(e)}")
        return None
    finally:
        client.close()
