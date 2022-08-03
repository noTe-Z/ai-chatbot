
from fastapi import WebSocket

# purpose: control connections to Websocket
class ConnectionManager:
    # create a list to collect current websocket status
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    # connect websocket and update the status
    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    # disconnect websocket and update the status
    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    # input a message from client and websocket then send the message to the websocket
    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)