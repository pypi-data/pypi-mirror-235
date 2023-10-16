import os
import requests
from io import BytesIO
from zipfile import ZipFile

# Function to download data
def download_data(dest_folder):
    if not os.path.exists(dest_folder):
        print('Downloading models data...')
        response = requests.get('https://github.com/simonoxen/ermodels/releases/download/v1.0/data.zip')
        with ZipFile(BytesIO(response.content)) as zipf:
            zipf.extractall(dest_folder)


# Destination folder for the data inside your package directory
models_dir = os.path.join(os.path.dirname(__file__), 'data')

# Call the download_data function to download data if it doesn't exist
download_data(models_dir)