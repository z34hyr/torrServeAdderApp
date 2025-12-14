from pydantic import BaseModel
from typing import Literal

class AddTorrentResponse(BaseModel):
    stat_string: Literal['Torrent added', 'Torrent working']
    poster: str
    title: str
