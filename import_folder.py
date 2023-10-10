import os
import subprocess
from pathlib import Path

def install_required_libraries():
    try:
        import gdown
    except ImportError:
        print("Installing required libraries...")
        subprocess.run(["pip", "install", "gdown"])
        print("Libraries installed successfully.")

def download_folder():
    # Ensure required libraries are installed
    install_required_libraries()

    # Define the local folder name
    local_folder_name = "3. Resultados Saber11"

    # Define the local path to the folder in the user's current working directory
    local_folder_path = Path.cwd() / local_folder_name

    # Check if the folder exists locally
    if local_folder_path.exists():
        print(f"The folder '{local_folder_name}' already exists in the current working directory.")
    else:
        print(f"Downloading the folder '{local_folder_name}'...")

        # Define the Google Drive link for the folder
        google_drive_link = "https://drive.google.com/drive/folders/1Vg6-7lv8iyJCux8B0m3c5DNvOrlW1byC?usp=sharing"

        # Download the folder using gdown
        import gdown
        gdown.download(google_drive_link, output=str(local_folder_path.parent))

        print(f"Folder '{local_folder_name}' downloaded successfully.")

if __name__ == "__main__":
    download_folder()
