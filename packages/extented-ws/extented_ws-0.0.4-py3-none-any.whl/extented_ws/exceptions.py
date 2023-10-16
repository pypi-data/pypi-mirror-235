class HandlerException(Exception):
    close_status: int
    disconnect: bool

    def __init__(self, message: str, disconnect: bool = True, close_status: int = 1005) -> None:
        """
        Init new handler exceptions, used for error handling in websocket handler
        """

        self.disconnect = disconnect
        self.close_status = close_status
        
        super().__init__(message)

    def __str__(self) -> str:
        return super().__str__()
