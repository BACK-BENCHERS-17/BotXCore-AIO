import os
from motor.motor_asyncio import AsyncIOMotorClient
from datetime import datetime

MONGO_URI = "mongodb+srv://bb:bb@cluster0.wvo3g4y.mongodb.net/?appName=Cluster0"
DB_NAME = "botxcore_aio"

client: AsyncIOMotorClient = None
db = None

async def init_db():
    global client, db
    if not MONGO_URI:
        print("DEBUG: MONGO_URI is empty")
        return
    try:
        print(f"DEBUG: Connecting to MongoDB... (URI: {MONGO_URI[:20]}...)")
        client = AsyncIOMotorClient(MONGO_URI, serverSelectionTimeoutMS=5000)
        db = client[DB_NAME]
        await client.admin.command('ping')
        print("DEBUG: MongoDB connected successfully")
        await _ensure_indexes()
        await _seed_admin()
    except Exception as e:
        print(f"DEBUG: MongoDB connection failed: {e}")
        client = None
        db = None

async def _ensure_indexes():
    await db.api_keys.create_index("key", unique=True)
    await db.api_keys.create_index("owner")
    await db.banned_ips.create_index("ip", unique=True)
    await db.request_logs.create_index("ts")
    await db.request_logs.create_index("ip")
    await db.request_logs.create_index("api_key")
    await db.rate_configs.create_index("scope", unique=True)
    await db.admins.create_index("username", unique=True)
    await db.settings.create_index("key", unique=True)

async def _seed_admin():
    from app.core.security import hash_password
    existing = await db.admins.find_one({"username": "xD3VS"})
    if not existing:
        await db.admins.insert_one({
            "username": "xD3VS",
            "password": hash_password("BotXCore"),
            "created_at": datetime.utcnow()
        })
    await db.settings.update_one(
        {"key": "api_enforcement"},
        {"$setOnInsert": {"key": "api_enforcement", "value": True}},
        upsert=True
    )

async def get_setting(key: str, default=None):
    doc = await db.settings.find_one({"key": key})
    if doc:
        return doc["value"]
    return default

async def set_setting(key: str, value):
    await db.settings.update_one(
        {"key": key},
        {"$set": {"key": key, "value": value}},
        upsert=True
    )

def get_db():
    return db
