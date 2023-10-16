from typing import Any, List, Callable, Union
from pydantic import BaseModel, validate_call

from .handler import HandlerObject, CallbackType
from .types import WebsocketMessage
from ..exceptions import HandlerException

class WebsocketMessageObserver:
    def __init__(self) -> None:
        self.handlers: List[HandlerObject] = []

    @validate_call
    def register(self, callback: CallbackType) -> CallbackType:
        """
        Register message handler
        """

        self.handlers.append(HandlerObject(callback=callback))

        return callback
    
    async def trigger(self, message: WebsocketMessage, user: Any = {}) -> List[Union[BaseModel, HandlerException]]:
        """
        Calling `WebsocketMessage.Type` handlers
        """

        results = []

        for handler in self.handlers:
            check, annotation = handler.check(message.Type)

            if check:
                data = annotation(**message.Data)
                
                try:
                    result = await handler.call(data, user=user)
                except HandlerException as e:
                    results.append(e)
                    continue

                assert isinstance(result, BaseModel)

                results.append(result)

        return results
    
    def __call__(self,) -> Callable[[CallbackType], CallbackType]:
        """
        Decorator for registering message handlers
        """

        def wrapper(callback: CallbackType) -> CallbackType:
            self.register(callback)
            return callback

        return wrapper