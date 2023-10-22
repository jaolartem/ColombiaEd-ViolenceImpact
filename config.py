import json

def load_database_config(filename="config.json"):
    """
    Loads the database configuration from a JSON file.
    
    Parameters:
    - filename (str): The path to the JSON configuration file. Default is "config.json".
    
    Returns:
    - tuple: A tuple containing the database host (DB_HOST), user (DB_USER), and password (DB_PASS).
    
    Example:
    DB_HOST, DB_USER, DB_PASS = load_database_config()
    """
    with open(filename, 'r') as file:
        config = json.load(file)
    db_config = config['database']
    return db_config['DB_HOST'], db_config['DB_USER'], db_config['DB_PASS']

def load_api_config(filename="config.json"):
    """
    Loads the API configuration from a JSON file.
    
    Parameters:
    - filename (str): The path to the JSON configuration file. Default is "config.json".
    
    Returns:
    - tuple: A tuple containing the application token (app_token), username, and password.
    
    Example:
    app_token, username, password = load_api_config()
    """
    with open(filename, 'r') as file:
        config = json.load(file)
    api_config = config['api']
    return api_config['app_token'], api_config['username'], api_config['password']

