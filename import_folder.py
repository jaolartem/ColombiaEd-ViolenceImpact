import os
from pathlib import Path
import requests

def download_folder():
    # Define the local folder name
    local_folder_name = "3. Resultados Saber11"

    # Define the local path to the folder in the user's current working directory
    local_folder_path = Path.cwd() / local_folder_name

    # Check if the folder exists locally
    if local_folder_path.exists():
        print(f"The folder '{local_folder_name}' already exists in the current working directory.")
    else:
        print(f"Downloading the folder '{local_folder_name}'...")

        # Replace with your Microsoft SharePoint link
        sharepoint_link = "https://unaledu-my.sharepoint.com/:f:/g/personal/jaolartem_unal_edu_co/ElghYmfT6nJOiqUhWD7oCZsBIOIA8aU0yzglfwLMyLP-KQ?e=i0nIIv"

        # Download the folder using requests
        response = requests.get(sharepoint_link)

        # Check if the request was successful
        if response.status_code == 200:
            # Save the content to a local file
            with open(local_folder_path, "wb") as f:
                f.write(response.content)
            print(f"Folder '{local_folder_name}' downloaded successfully.")
        else:
            print(f"Failed to download. Status code: {response.status_code}")
            print(response.text)

if __name__ == "__main__":
    download_folder()
