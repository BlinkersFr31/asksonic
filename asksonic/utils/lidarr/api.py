from typing import Optional
from urllib.parse import quote_plus
from libsonic import Connection
from urllib.request import Request
from random import shuffle
from .track import Track


class Lidarr(Connection):
    def __init__(
        self#,
        #baseUrl: str, username: str, password: str, port: int,
        #serverPath: str, apiVersion: str, appName: str,
        #extra_secret: Optional[str] = None
    ) -> None:
        super().__init__(
            #baseUrl=baseUrl, username=username, password=password, port=port,
            #serverPath=serverPath, appName=appName, apiVersion=apiVersion
        )
        #self._extra_secret = extra_secret
