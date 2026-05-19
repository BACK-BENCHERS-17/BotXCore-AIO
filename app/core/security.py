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

import os
import secrets
import hashlib
import hmac
from datetime import datetime, timedelta
from jose import jwt, JWTError

SECRET_KEY = os.getenv("SECRET_KEY", "botxcore-secret-change-in-prod-2026")
ALGORITHM = "HS256"
TOKEN_EXPIRE_HOURS = 24

def hash_password(pw: str) -> str:
    salt = secrets.token_hex(16)
    h = hashlib.pbkdf2_hmac("sha256", pw.encode(), salt.encode(), 260000)
    return f"{salt}:{h.hex()}"

def verify_password(pw: str, stored: str) -> bool:
    try:
        salt, hx = stored.split(":")
        h = hashlib.pbkdf2_hmac("sha256", pw.encode(), salt.encode(), 260000)
        return hmac.compare_digest(h.hex(), hx)
    except Exception:
        return False

def create_access_token(data: dict) -> str:
    payload = data.copy()
    payload["exp"] = datetime.utcnow() + timedelta(hours=TOKEN_EXPIRE_HOURS)
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def decode_token(token: str) -> dict:
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

def generate_api_key() -> str:
    return "bx_" + secrets.token_urlsafe(32)
