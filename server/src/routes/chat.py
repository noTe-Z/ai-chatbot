import os
from fastapi import APIRouter, Depends, FastAPI, WebSocket,  Request, BackgroundTasks, HTTPException
import uuid
from ..socket.connection import ConnectionManager
from ..socket.utils import get_token

manager = ConnectionManager()


# APIRouter are used to create operations seperated from the rest of code
# It works in same way as FastAPI() and can be combined by .include_router(chat)
chat = APIRouter()

# @route   POST /token
# @desc    Route to generate chat token
# @access  Public

# issue user session token for the chat session  
# to identify each unique user session
@chat.post("/token")
async def token_generator(name: str, request: Request):
    # user provide a name and we return a token 
    if name == "":
        raise HTTPException(status_code=400, detail={
            "loc": "name",  "msg": "Enter a valid name"})

    token = str(uuid.uuid4())

    data = {"name": name, "token": token}

    return data


# @route   POST /refresh_token
# @desc    Route to refresh token
# @access  Public

# Get session history for user if connection is lost
@chat.post("/refresh_token")
async def refresh_token(request: Request):
    return None


# @route   Websocket /chat
# @desc    Socket for chatbot
# @access  Public

# open a Websocket to send message between user and server
@chat.websocket("/chat") # do websocket operation for the following code
async def websocket_endpoint(websocket: WebSocket, token: str = Depends(get_token)): # path parameter by class
    await manager.connect(websocket) # connect to websocket through function defined
    try:
        while True:
            data = await websocket.receive_text() # input text and store it in variable data
            print(data) 
            await manager.send_personal_message(f"Response: Simulating response from the GPT service", websocket)
    except WebSocketDisconnect:
        manager.disconnect(websocket)