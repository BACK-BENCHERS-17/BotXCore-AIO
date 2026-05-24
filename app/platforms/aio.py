import requests as _requests
import time
import random

def clean_url(url: str) -> str:
    url = url.strip()
    if "youtube.com" in url or "youtu.be" in url:
        return url
    if "?" in url:
        return url
    if not url.endswith("/"):
        url += "/"
    return url

def _fetch_engine_1(url: str):
    """Engine: Downr (Primary)"""
    _EP = "https://downr.org/.netlify/functions"
    _HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Origin": "https://downr.org",
        "Referer": "https://downr.org/",
        "Content-Type": "application/json"
    }
    try:
        s = _requests.Session()
        # Pre-flight analytics call to mimic browser
        try: s.get(f"{_EP}/analytics", headers=_HEADERS, timeout=3)
        except: pass
        
        r = s.post(f"{_EP}/nyt", json={"url": url}, headers=_HEADERS, timeout=15)
        data = r.json()
        if data.get("medias") and len(data["medias"]) > 0:
            return data, None
        return None, "no_media"
    except Exception as e:
        return None, str(e)

def _fetch_engine_2(url: str):
    """Engine: Cobalt (Privacy-focused fallback)"""
    _EP = "https://api.cobalt.tools/api/json"
    _HEADERS = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Referer": "https://cobalt.tools/"
    }
    try:
        r = _requests.post(_EP, json={"url": url, "vQuality": "720"}, headers=_HEADERS, timeout=15)
        data = r.json()
        if data.get("status") == "stream" or data.get("status") == "picker":
            # Map Cobalt format to internal format
            internal_data = {
                "title": data.get("text", "Video"),
                "source": "cobalt",
                "medias": []
            }
            if data.get("url"):
                internal_data["medias"].append({"url": data["url"], "quality": "HD", "extension": "mp4"})
            if data.get("picker"):
                for p in data["picker"]:
                    internal_data["medias"].append({"url": p["url"], "quality": p.get("quality", "Default"), "extension": "mp4"})
            return internal_data, None
        return None, "no_media"
    except Exception as e:
        return None, str(e)

def fetch(url: str):
    url = clean_url(url)
    
    # Try Engine 1 (Downr)
    data, err = _fetch_engine_1(url)
    if data: return data, None
    
    # Fallback to Engine 2 (Cobalt)
    data, err = _fetch_engine_2(url)
    if data: return data, None
    
    return None, "no_media_found"
