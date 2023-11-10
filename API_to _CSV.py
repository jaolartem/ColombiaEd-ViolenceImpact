from fetch_data_from_api import fetch_data_from_api
from config import load_api_config

app_token, username, password = load_api_config()
endpoint = "vtub-3de2"

data_dict = fetch_data_from_api(app_token, username, password, endpoint)
print(data_dict)

# Puedes agregar código adicional aquí para hacer algo con `data_dict` si lo deseas.
