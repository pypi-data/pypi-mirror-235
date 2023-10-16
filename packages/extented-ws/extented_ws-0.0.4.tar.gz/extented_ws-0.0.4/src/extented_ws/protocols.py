import functools
import http
from typing import Any, Callable
import urllib

from aiogram.utils.web_app import WebAppUser, safe_parse_webapp_init_data
from websockets.server import  WebSocketServerProtocol

class TelegramAuthProtocol(WebSocketServerProtocol):
    user: WebAppUser

    def __init__(self, *args: Any, token: str, **kwargs: Any) -> None:
        self.__token = token
        super().__init__(*args, **kwargs)
    
    async def process_request(self, path, headers):
        initData = urllib.parse.urlparse(path).query
        
        try:
            initData = safe_parse_webapp_init_data(self.__token, initData)
        except ValueError:
            return http.HTTPStatus.UNAUTHORIZED, [], b"Invalid init data\n"

        self.user = initData.user

        return await super().process_request(path, headers)
    
def telegram_protocol_factory(token: str) -> Callable[..., TelegramAuthProtocol]:
    create_protocol = TelegramAuthProtocol

    return functools.partial(
        create_protocol,
        token=token    
    )