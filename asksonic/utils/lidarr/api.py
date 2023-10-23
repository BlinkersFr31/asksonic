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
        artists = self.lookup_artist(artistStr)
        if not artists:
            return false
        
        folders = self.get_root_folder()
        if not folders:
            return false
        
        for artist in artists:
            #TODO
            self.add_artist(artist, root_dir: str, quality_profile_id: int | None = None, metadata_profile_id: int | None = None, monitored: bool = True, artist_monitor: Literal['all', 'future', 'missing', 'existing', 'first', 'latest'] = 'all', artist_search_for_missing_albums: bool = False)

        
        return true
