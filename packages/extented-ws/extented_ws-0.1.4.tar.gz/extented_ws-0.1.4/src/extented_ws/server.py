import asyncio
from typing import Any

from websockets.server import serve, WebSocketServerProtocol

from .protocols import telegram_protocol_factory
from .message import WebsocketMessageObserver, WebsocketMessage
from .exceptions import HandlerException

class WebsocketServer:
    def __init__(self) -> None:
        self.message = WebsocketMessageObserver()

    async def listen(self,
               host: str = "localhost",
               port: int = 8000,
               create_protocol: WebSocketServerProtocol = telegram_protocol_factory(
                    token=""
               ),
               **kwargs: Any
          ):
        """
        This method does the same as `websockets.server.serve`
        See websockets doc: https://websockets.readthedocs.io/en/stable/reference/asyncio/server.html
        """

        stop = asyncio.Future()
        self.ws = await serve(self.__on_message, host, port, create_protocol=create_protocol, ** kwargs)
        await stop

    async def __on_message(self, websocket: WebSocketServerProtocol):
        async for data in websocket:
            try:
                message = WebsocketMessage.model_validate_json(data)
            except:
                response_message = WebsocketMessage(Type="HandlerException", Data="Invalid message")
                await websocket.send(response_message.model_dump_json())
                continue

            results = await self.message.trigger(message, getattr(websocket, "user", {}))

            for r in results:
                response_message = WebsocketMessage(Type=type(r).__name__, Data=r.model_dump())
                await websocket.send(response_message.model_dump_json())
                
                if isinstance(r, HandlerException) and r.disconnect:
                    await websocket.close(code=r.close_status)