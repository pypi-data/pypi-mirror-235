import asyncio

from pydantic import BaseModel
from functools import partial
from typing import Any, Callable, Dict
from dataclasses import dataclass, field

import contextvars
import inspect


CallbackType = Callable[..., BaseModel]


@dataclass
class HandlerObject:
    callback: CallbackType
    awaitable: bool = field(init=False)
    spec: inspect.FullArgSpec = field(init=False)

    def __post_init__(self) -> None:
        callback = inspect.unwrap(self.callback)
        self.awaitable = inspect.isawaitable(
            callback) or inspect.iscoroutinefunction(callback)
        self.spec = inspect.getfullargspec(callback)

    def check(self, type: str) -> Dict[bool, Any]:
        if len(self.spec.annotations) == 0:
            return [False, None]

        first_annotation = list(self.spec.annotations.values())[0]

        return (type == first_annotation.__name__, first_annotation)

    def _prepare_kwargs(self, kwargs: Dict[str, Any]) -> Dict[str, Any]:
        if self.spec.varkw:
            return kwargs

        return {
            k: v for k, v in kwargs.items() if k in self.spec.args or k in self.spec.kwonlyargs
        }

    async def call(self, *args: Any, **kwargs: Any) -> Any:
        wrapped = partial(self.callback, *args, **self._prepare_kwargs(kwargs))

        if self.awaitable:
            return await wrapped()

        loop = asyncio.get_event_loop()
        context = contextvars.copy_context()
        wrapped = partial(context.run, wrapped)

        return await loop.run_in_executor(None, wrapped)
