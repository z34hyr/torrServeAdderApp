from requests import get, post, Request, Response, Session, ConnectionError
from models import AddTorrentResponse
from pydantic import ValidationError
from contextlib import nullcontext
from functools import wraps

class CustomSession(Session):
    def request(self, method, url, **kwargs):
        kwargs.setdefault("timeout", 5)
        return super().request(method, url, **kwargs)

def wrap_http_session(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        print(func, args, kwargs)
    return wrapper

class TorrServe:
    def __init__(self, host: str, port: str):
        self._base_url = f'http://{host}:{port}/'

    def get_base_url(self):
        return self._base_url

    def _int_check_connection(self, s: CustomSession):
        prepped_req = s.prepare_request(Request('GET', self._base_url + 'echo'))
        s.send(prepped_req)
        return True

    def _upload_torrent(self, s: CustomSession, file, display_name: str):
        endpoint = 'torrent/upload/'
        values = {
            'save': 'save',
            'title': display_name,
        }
        files = {'file': file}

        req = Request('POST', self._base_url + endpoint, files=files, data=values)
        prepped_req = s.prepare_request(req)

        resp: Response = s.send(prepped_req)
        return True
        # try:
        #     resp: Response = s.send(prepped_req)
        #     # AddTorrentResponse.model_validate(resp.json())
        #     return True
        # # except ValidationError as err:
        # #     print(err)
        # except Exception as err:
        #     print(err)

    def check_connection(self):
        try:
            with CustomSession() as http_session:
                return self._int_check_connection(http_session)
        except ConnectionError as err:
            print('Connection error')
            return 'Torr serve запущен?'

    def add_torrent(self, file_path: str, display_name: str) -> str:
        try:
            with CustomSession() as http_session, open(file_path, 'rb') as f:
                self._int_check_connection(http_session)
                self._upload_torrent(http_session, f, display_name)
                return 'OK'
        except FileNotFoundError as err:
            return 'Файл не найден'
        except ConnectionError as err:
            return 'Torr serve запущен?'
