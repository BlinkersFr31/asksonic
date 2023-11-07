from os import getenv
from .api import Liadarr

lidarr_url = getenv('ASKS_LIDARR_URL', '')
lidarr_api_key = getenv('ASKS_LIDARR_APIKEY', '')

if any(x == '' for x in [lidarr_url, lidarr_api_key]):
    raise RuntimeError('Lidarr login information is missing from env')


liadarr = Lidarr(
    lidarr_url,
    lidarr_api_key
)