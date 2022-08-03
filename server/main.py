from fastapi import FastAPI, Request
import uvicorn
import os
from dotenv import load_dotenv
from src.routes.chat import chat # import chat.py from src

# Initialize load_dotenv to load variables from .env
load_dotenv()

# Initialize FastAPI
api = FastAPI()

# include router "chat"
api.include_router(chat)

# Create test route - return JSON response
@api.get("/test")
async def root():
    return {"msg": "API is Online"}


if __name__ == "__main__":
    # set up development server
    if os.environ.get('APP_ENV') == "development":
        uvicorn.run("main:api", host="0.0.0.0", port=3500,
                    workers=4, reload=True)
    else:
      pass