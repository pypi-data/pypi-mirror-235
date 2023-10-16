# Extented Websockets

[![pipeline status](https://gitlab.com/ts-workflow/template/tbot-ts-example-sockets-webapp/badges/main/pipeline.svg?ignore_skipped=true)](https://gitlab.com/ts-workflow/template/tbot-ts-example-sockets-webapp/-/commits/main)

The library is based on [Websockets](https://github.com/python-websockets/websockets/tree/main)<br/>
The observer-handlers approach is used, like in FastAPI and Aiogram it's allows you to quickly integrate web sockets into the project, and expand the list of requests-responses

## Installation

Download [![Latest Release](https://gitlab.com/ts-workflow/template/tbot-ts-example-sockets-webapp/-/badges/release.svg)](https://gitlab.com/ts-workflow/template/tbot-ts-example-sockets-webapp/-/packages/19226878)

Or use:
```sh
pip install extented-ws --index-url https://__token__:<your_personal_token>@gitlab.com/api/v4/projects/51025004/packages/pypi/simple
```

## Usage
By default, the server accepts a **JSON** message of the following format:
```json
{
  "Type": "CalculateRequest",
  "Data": {
    "numbers": [2, 2]
  }
}
```
>After that, the server calls `trigger` from the `observer`, and that in turn calls all `handlers` whose first argument type name equals `Type` in **JSON**
The returned object, in turn, will be the answer for the client
When the `observer` finds the desired `handlers`, it calls it by passing arguments:
- Unpacked object from `Data` in **JSON**
- The user received from the authorization `protocol`

>For known how `create_protocol` work see:         [Authentication](https://websockets.readthedocs.io/en/stable/topics/authentication.html#query-parameter), [Factory](https://websockets.readthedocs.io/en/stable/faq/common.html#how-can-i-pass-arguments-to-a-custom-protocol-subclass)

```python
from extented_ws import WebsocketServer, telegram_protocol_factory

server = WebsocketServer()

class CalculateRequest(BaseModel):
    numbers: List[int]

class CalculateResponse(BaseModel):
    result: int

@server.message()
async def calculate_handler(request: CalculateRequest, user: WebAppUser): # user is optional argument
    result = 0

    for i in request.numbers:
        result += i

    return CalculateResponse(result=result)

async def main() -> None:
    """
        telegram_protocol_factory used for create TelegramAuthProtocol instance with bot token
    """
    await server.listen(create_protocol=telegram_protocol_factory(
        token=TOKEN
    ))


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

```

> Also see [EXAMPLE](https://gitlab.com/ts-workflow/template/tbot-ts-example-sockets-webapp/-/tree/main/example?ref_type=heads)
