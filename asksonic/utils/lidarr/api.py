#from typing import Optional
#from urllib.parse import quote_plus
#from libsonic import Connection
#from urllib.request import Request
#from random import shuffle
#from .track import Track
from pyarr import LidarrAPI


class Lidarr(LidarrAPI):
    def __init__(
        self,
        host_url: str,
        api_key: str
    ) -> None:
        super().__init__(
            host_url=host_url,
            api_key=api_key
        )

    def artist_add_to_collection(self, artistStr: str) -> bool:
        logger.debug('artist_add_to_collection')
        artists = self.lookup_artist(artistStr)
        if not artists:
            return false
        else:
            logger.debug(artists['name'))
        
        folder = self.get_root_folder()
        if not folder:
            return false
        else:
            logger.debug(folder['name'))
        
        for artist in artists:
            #TODO https://docs.totaldebug.uk/pyarr/modules/lidarr.html
            try:
                self.add_artist(artist: artist, root_dir: folder['name'), artist_search_for_missing_albums: bool = True)
            except PyarrMissingProfile as exception:
                logger.error(exception)
                return false
        
        return true
