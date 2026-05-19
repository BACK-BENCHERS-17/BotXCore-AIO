"""
╔══════════════════╗
              BOTXCORE
╚══════════════════╝

[ PROJECT   ]  BotXCore AIO (All-In-One Downloader)
[ DEVELOPER ]  xD3VS

────────────────────

[ SUPPORT   ]  https://t.me/BotXCore
[ UPDATES   ]  https://t.me/BotXCore
[ ABOUT US  ]  https://BotXCore.sbs

────────────────────

[ DONATE    ]  https://Pay.BotXCore.sbs

────────────────────
      FAST • POWERFUL • ALL-IN-ONE
      
"""


from fastapi import APIRouter, HTTPException, Response, Request
from pydantic import BaseModel
from app.core.database import get_db
from app.core.security import verify_password, create_access_token

router = APIRouter(tags=["Auth"])

class LoginRequest(BaseModel):
    username: str
    password: str

@router.post("/login")
async def login(body: LoginRequest, response: Response):
    db = get_db()
    admin = await db.admins.find_one({"username": body.username})

    if not admin or not verify_password(body.password, admin["password"]):
        raise HTTPException(status_code=401, detail="invalid_credentials")

    token = create_access_token({"sub": body.username, "role": "admin"})
    response.set_cookie("bx_token", token, httponly=True, samesite="lax", max_age=86400)
    return {"token": token, "username": body.username}
