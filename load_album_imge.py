import urllib.request
import requests
from PIL import Image

API_KEY = '18c5910bdb220f9a8fbb62f9fe9f8f59'


def get_album_info(artist_name, album_title):
    url = f'http://ws.audioscrobbler.com/2.0/?method=album.getinfo&api_key={API_KEY}&artist={artist_name}&album={album_title}&format=json'
    album_info = requests.get(url).json()

    if album_info is None:
        return None

    try:
        return album_info['album']['image'][2]['#text']
    except KeyError:
        return None


# artist_name, release => 'Faster Pussy cat', 'Monster Ballads X-Mas'
def open_image(artist_name, release):
    file = str(get_album_info(artist_name, release))
    if file is not None:
        image = Image.open(urllib.request.urlopen(file))
        return image
    else:
        return None
