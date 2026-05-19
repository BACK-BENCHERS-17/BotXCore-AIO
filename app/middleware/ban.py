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


from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse
from app.core.database import get_db

class BanMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        if request.url.path.startswith("/admin"):
            return await call_next(request)

        ip = request.client.host
        db = get_db()

        if db is not None:
            banned = await db.banned_ips.find_one({"ip": ip, "active": True})
            if banned:
                return JSONResponse(
                    status_code=403,
                    content={
                        "error": "ip_banned",
                        "reason": banned.get("reason", "Policy violation"),
                        "msg": "Your IP has been banned. Contact support. @BotXCore"
                    }
                )

        return await call_next(request)
