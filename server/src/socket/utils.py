from fastapi import WebSocket, status, Query
from typing import Optional

# 获取token，如果token为空，发出警告
# 之后这个文件用来验证token，区分不同user session
async def get_token(
    websocket: WebSocket,
    token: Optional[str] = Query(None),
):
    if token is None or token == "":
        await websocket.close(code=status.WS_1008_POLICY_VIOLATION)

    return token