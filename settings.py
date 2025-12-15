from os import getenv
import sys

# UI params
GRID_DEFAULT_PARAMS = {
    'padx': 5,
    'pady': 5,
    'sticky': 'nswe'
}

# TorrServe params
HOST = getenv('TORR_HOST', '192.168.0.136')
PORT = getenv('TORR_PORT', '8090')
DEFAULT_TIMEOUT = int(getenv('TORR_CONN_TIMEOUT', '5'))

def get_default_path():
    platform = sys.platform
    if platform == 'linux':
        return getenv('HOME') + '/' + 'Downloads'
    elif (
            platform in ('win32', 'win64') and
            (drive_name := getenv('HOMEDRIVE')) and
            (home_path := getenv('HOMEPATH'))
    ):
        return drive_name + home_path + '\\Downloads'
    else:
        return '.'
DEFAULT_TORRENT_FILE_PATH = getenv('DEFAULT_TORRENT_FILE_PATH', get_default_path())
