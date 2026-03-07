import requests
from pathlib import Path

def download_file(url, filename):
    """
    takes in url : url to download
             filename : location to store the file
    reference : https://www.geeksforgeeks.org/python/how-to-download-files-from-urls-with-python/
    """
    path = Path("data") / filename
    path.parent.mkdir(exist_ok=True)

    response = requests.get(url)

    if response.status_code == 200:
        with open(path, "wb") as f:
            f.write(response.content)
        print("Downloaded:", path)
    else:
        print("Download failed")
