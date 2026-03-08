from pathlib import Path
from urllib.parse import urlparse
import urllib.request


def download_file(url, folder):
    filename = Path(urlparse(url).path).name
    path = Path(folder) / filename

    path.parent.mkdir(parents=True, exist_ok=True)

    response = urllib.request.urlopen(url)

    with open(path, "wb") as f:
        f.write(response.read())

    print("Downloaded:", path)

    return str(path)