import sys
from pathlib import Path
from fetch_data_from_api import fetch_data_from_api
from config import load_api_config

DEFAULT_ENDPOINT = "vtub-3de2"

def main(endpoint: str = DEFAULT_ENDPOINT, output_folder: Path = Path("backup_csv")) -> Path:
    """
    Downloads a datos.gov.co dataset and saves it as CSV in `output_folder`.

    Returns the path of the CSV written.
    """
    app_token, username, password = load_api_config()
    data_dict = fetch_data_from_api(app_token, username, password, endpoint)
    if data_dict is None:
        sys.exit(f"Could not fetch endpoint {endpoint}: see etl_errors.log")

    output_folder.mkdir(parents=True, exist_ok=True)
    csv_path = output_folder / f"{endpoint}.csv"
    data_dict[endpoint].to_csv(csv_path, index=False)
    print(f"Saved {len(data_dict[endpoint])} rows to {csv_path}")
    return csv_path

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else DEFAULT_ENDPOINT)
