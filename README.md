<div align="center">

<img src="static/botxcore-logo-hd.jpg" alt="BotXCore Logo" width="220" style="border-radius:16px;" />

<br/>

```
╔══════════════════════════════════════════════════════╗
                    B O T X C O R E
         FAST  •  POWERFUL  •  ALL-IN-ONE
╚══════════════════════════════════════════════════════╝
```

# BotXCore AIO ── All-In-One Downloader API

**A blazing-fast, production-grade media download REST API**  
Built with FastAPI · MongoDB · Python 3.11 · Docker

<br/>

[![Railway Deploy](https://img.shields.io/badge/Deploy%20on-Railway-blueviolet?style=for-the-badge&logo=railway)](https://railway.app)
[![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com)
[![MongoDB](https://img.shields.io/badge/MongoDB-Motor-47A248?style=for-the-badge&logo=mongodb)](https://mongodb.com)
[![License](https://img.shields.io/badge/License-Proprietary-red?style=for-the-badge)](https://BotXCore.sbs)

<br/>

```
[ PROJECT   ]  BotXCore AIO (All-In-One Downloader)
[ DEVELOPER ]  xD3VS
[ VERSION   ]  v2.0.0

────────────────────────────────────

[ SUPPORT   ]  https://t.me/BotXCore
[ UPDATES   ]  https://t.me/BotXCore
[ ABOUT US  ]  https://BotXCore.sbs

────────────────────────────────────

[ DONATE    ]  https://Pay.BotXCore.sbs

────────────────────────────────────
```

</div>

---

## ◈ Showcase

<div align="center">

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   Send URL  ──►  API resolves platform  ──►  Get media      │
│                                                             │
│   YouTube · Instagram · TikTok · Twitter · Facebook        │
│   Spotify · Terabox · XHamster · PornHub · HentaiCity      │
│   + 10 more platforms via yt-dlp universal engine          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

</div>

One unified endpoint handles **20+ platforms** — no per-platform keys required. Submit a URL, receive structured JSON with title, thumbnail, author, duration, and direct download links at every available quality.

---

## ◈ Features

### ◆ Universal Download Engine
```
/api/v1/dl?url=<ANY_URL>&api=YOUR_KEY
```
- Powered by **yt-dlp** — supports YouTube, Instagram, TikTok, Twitter/X, Facebook, Reddit, Dailymotion, Vimeo, and 1000+ sites
- Automatic platform detection — no manual routing needed
- Returns all available qualities (1080p, 720p, 480p, 360p, audio-only)
- Title, thumbnail, author, duration, type all included in response

### ◆ Platform-Specific Endpoints

| Endpoint | Platform | Notes |
|---|---|---|
| `/api/v1/dl` | Universal (1000+ sites) | yt-dlp powered |
| `/api/v1/s` | Spotify | Track download via Playwright |
| `/api/v1/tb` | Terabox | File listing + direct links |
| `/api/v1/phub` | PornHub | Multi-quality formats |
| `/api/v1/xham` | XHamster | Video + search endpoint |
| `/api/v1/xham/search` | XHamster Search | Query-based results |
| `/api/v1/hcity` | HentaiCity | M3U8 + trailer links |

### ◆ API Key Management
- Admin panel at `/admin` — full web UI, no CLI needed
- Generate, revoke, enable/disable keys with one click
- Per-key rate limits configurable independently
- Key expiry dates, usage counters, last-used timestamps
- `bx_` prefixed tokens via cryptographically secure generation

### ◆ Intelligent Rate Limiting
- Per-IP and per-API-key rate buckets (independent sliding windows)
- Default: **60 requests / 60 seconds** — fully overridable per key or globally
- `Retry-After`, `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-RateLimit-Reset` headers on every response
- Admin panel controls without touching code

### ◆ IP Ban System
- Ban/unban IPs directly from the admin panel
- Banned IPs receive `403 Forbidden` instantly — blocked at middleware layer
- Persistent bans stored in MongoDB — survives restarts

### ◆ Request Logging
- Every request logged: IP, API key, path, method, timestamp
- Queryable from admin panel
- MongoDB-indexed for fast lookups by IP, key, or time range

### ◆ Security Architecture
```
Request ──► BanMiddleware ──► RateLimitMiddleware ──► Auth (API Key)
                                                           │
                                              PBKDF2-SHA256 password hashing
                                              JWT tokens (HS256, 24h expiry)
                                              Secure key generation (secrets module)
```

### ◆ SEO Ready Out-of-the-Box
- `robots.txt` — crawlers allowed on `/`, blocked on `/admin`, `/api`, `/auth`
- `sitemap.xml` — structured for Google/Bing indexing
- Open Graph meta tags (`og-image.jpg` included)
- `favicon.ico`, `favicon-16.png`, `favicon-32.png`, `apple-touch-icon.png` all included
- `/health` endpoint for uptime monitoring and load balancer probes

### ◆ Docker + Railway Native
- Single `Dockerfile` — no compose needed for basic deployment
- Playwright + Chromium bundled inside container (Spotify support)
- `render.yml` + Railway compatible — deploy in under 2 minutes
- `PORT` env respected automatically

---

## ◈ Deploy on Railway ── 3 Steps

> Connect repo, add one variable, done. App goes live automatically.

<div align="center">

```
┌────────────────────────────────────────────────────────────┐
│                                                            │
│   STEP 1 ──  Fork / push this repo to GitHub              │
│                                                            │
│   STEP 2 ──  Go to railway.app → New Project              │
│              → Deploy from GitHub repo → select this repo  │
│                                                            │
│   STEP 3 ──  Add environment variable:                     │
│                                                            │
│              MONGO_URI = mongodb+srv://...                 │
│                                                            │
│              (Railway auto-generates SECRET_KEY)           │
│                                                            │
│   Done. Your API is live at *.up.railway.app              │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

</div>

### Environment Variables

| Variable | Required | Description |
|---|---|---|
| `MONGO_URI` | **YES** | Your MongoDB Atlas connection string |
| `SECRET_KEY` | auto | JWT signing secret — Railway generates this |
| `DB_NAME` | no | Database name (default: `botxcore_aio`) |

### After Deploy

1. Visit `https://your-app.up.railway.app/admin/login`
2. Login with default credentials:
   ```
   Username : admin
   Password : BotXCore@2026
   ```
3. **Change your password immediately** from the admin panel
4. Generate your first API key and start making requests

---

## ◈ API Usage

### Authentication

Pass your API key in any of these ways:

```bash
# Query parameter (easiest)
GET /api/v1/dl?url=https://youtu.be/dQw4w9WgXcQ&api=bx_YOUR_KEY

# Header (recommended for production)
GET /api/v1/dl?url=https://youtu.be/dQw4w9WgXcQ
X-API-Key: bx_YOUR_KEY
```

### Universal Download ── `/api/v1/dl`

**Request:**
```http
GET /api/v1/dl?url=https://www.youtube.com/watch?v=dQw4w9WgXcQ&api=bx_xxx
```

**Response:**
```json
{
  "success": true,
  "source": "youtube",
  "title": "Rick Astley - Never Gonna Give You Up",
  "author": "Rick Astley",
  "thumbnail": "https://i.ytimg.com/vi/dQw4w9WgXcQ/maxresdefault.jpg",
  "duration": 213,
  "type": "video",
  "medias": [
    { "quality": "1080p", "url": "https://...", "ext": "mp4" },
    { "quality": "720p",  "url": "https://...", "ext": "mp4" },
    { "quality": "audio", "url": "https://...", "ext": "m4a" }
  ],
  "stats": { ... }
}
```

### Spotify ── `/api/v1/s`

```http
GET /api/v1/s?url=https://open.spotify.com/track/xxx&api=bx_xxx
```

```json
{
  "success": true,
  "source": "spotify",
  "title": "Track Name",
  "artist": "Artist Name",
  "thumbnail": "https://...",
  "download_url": "https://..."
}
```

### Terabox ── `/api/v1/tb`

```http
GET /api/v1/tb?url=https://1024terabox.com/s/xxx&api=bx_xxx
```

```json
{
  "success": true,
  "source": "terabox",
  "total_files": 3,
  "list": [
    { "name": "file.mp4", "size": 104857600, "dlink": "https://..." }
  ],
  "free_credits_remaining": 42
}
```

### Error Responses

| Code | Error | Meaning |
|---|---|---|
| `400` | `invalid_url` | URL doesn't start with http |
| `401` | `missing_api_key` | No key provided |
| `401` | `invalid_api_key` | Key not found |
| `403` | `api_key_disabled` | Key revoked by admin |
| `403` | `api_key_expired` | Key past expiry date |
| `403` | `banned` | Your IP is banned |
| `422` | `fetch_failed` | Platform scraping error |
| `429` | `rate_limit_exceeded` | Too many requests |
| `503` | `retry_required` | Temporary upstream error |

---

## ◈ Self-Host with Docker

```bash
# Clone the repo
git clone https://github.com/justfortestingnothibghere/BotXCore-AIO
cd botxcore-aio

# Build the image
docker build -t botxcore-aio .

# Run with your MongoDB URI
docker run -d \
  -p 8000:8000 \
  -e MONGO_URI="mongodb+srv://user:pass@cluster.mongodb.net/botxcore_aio" \
  -e SECRET_KEY="your-super-secret-key" \
  --name botxcore-aio \
  botxcore-aio
```

App will be live at `http://localhost:8000`  
Admin panel at `http://localhost:8000/admin`

---

## ◈ Local Development

```bash
# Prerequisites: Python 3.11+, MongoDB

git clone https://github.com/YOUR_USERNAME/botxcore-aio.git
cd botxcore-aio

pip install -r requirements.txt
playwright install chromium

export MONGO_URI="mongodb://localhost:27017"
export SECRET_KEY="dev-secret"

python main.py
# → Server running at http://localhost:8000
```

---

## ◈ Project Structure

```
botxcore-aio/
├── main.py                    ◄  FastAPI app entry point
├── requirements.txt           ◄  Python dependencies
├── Dockerfile                 ◄  Production container
├── render.yml                 ◄  Render / Railway config
├── robots.txt                 ◄  SEO crawler rules
├── sitemap.xml                ◄  Google sitemap
├── favicon.ico
│
├── app/
│   ├── core/
│   │   ├── database.py        ◄  MongoDB Motor client + seed
│   │   ├── security.py        ◄  JWT, PBKDF2, key generation
│   │   └── deps.py            ◄  API key dependency injection
│   │
│   ├── middleware/
│   │   ├── rate_limit.py      ◄  Sliding window rate limiter
│   │   ├── ban.py             ◄  IP ban enforcement
│   │   └── logger.py          ◄  Request logging to MongoDB
│   │
│   ├── platforms/
│   │   ├── aio.py             ◄  Universal yt-dlp engine
│   │   ├── spotify.py         ◄  Spotify via Playwright
│   │   ├── terabox.py         ◄  Terabox file resolver
│   │   ├── phub.py            ◄  PornHub extractor
│   │   ├── xham.py            ◄  XHamster extractor + search
│   │   └── hcity.py           ◄  HentaiCity M3U8 extractor
│   │
│   └── routes/
│       ├── download.py        ◄  /api/v1/* endpoints
│       ├── admin.py           ◄  /admin/* panel + API
│       └── auth.py            ◄  /auth/login + JWT issue
│
├── templates/
│   ├── index.html             ◄  Landing page
│   ├── admin.html             ◄  Admin dashboard
│   └── login.html             ◄  Admin login
│
└── static/
    ├── botxcore-logo-hd.jpg    ◄  HD logo
    ├── og-image.jpg           ◄  Open Graph preview image
    └── favicon-*.png          ◄  Icons for all devices
```

---

## ◈ Google Search Indexing Guide

Your API ships with full SEO infrastructure already in place. Follow these steps to get indexed:

### Step 1 ── Update sitemap.xml
Replace `your-api-domain.com` with your actual Railway/custom domain:
```xml
<loc>https://your-actual-domain.com/</loc>
```

### Step 2 ── Update robots.txt
Edit the `Sitemap:` line at the bottom of `robots.txt`:
```
Sitemap: https://your-actual-domain.com/sitemap.xml
```

### Step 3 ── Submit to Google Search Console
1. Go to [search.google.com/search-console](https://search.google.com/search-console)
2. Add your domain as a property
3. Verify via HTML meta tag or DNS TXT record
4. Navigate to **Sitemaps** → Submit `https://your-domain.com/sitemap.xml`

### Step 4 ── Submit to Bing Webmaster Tools
1. Go to [bing.com/webmasters](https://bing.com/webmasters)
2. Import from Google Search Console (one click)
3. Your sitemap auto-submits

### What's Already Configured
```
robots.txt   ──  Allows Googlebot on /  ──  Blocks /admin, /api, /auth
sitemap.xml  ──  Weekly changefreq  ──  Priority 1.0 on homepage
og-image.jpg ──  1200x630 Open Graph image for social sharing
favicon      ──  16px, 32px, 180px apple-touch-icon — all browsers covered
/health      ──  Uptime Robot / monitoring probe endpoint
```

---

## ◈ Admin Panel Features

| Feature | Description |
|---|---|
| API Key Generation | Create keys with custom labels, rate limits, expiry |
| Key Management | Enable / disable / delete keys |
| IP Banning | Ban abusive IPs with one click |
| Request Logs | Browse all API requests with filters |
| Rate Config | Set global or per-key rate limits live |
| Settings | Toggle API enforcement on/off (open mode for testing) |
| Terabox Keys | Pool third-party Terabox API keys for load balancing |

Default login: `admin` / `BotXCore@2026`  
**Change password immediately after first login.**

---

## ◈ Tech Stack

| Layer | Technology |
|---|---|
| Runtime | Python 3.11 |
| Framework | FastAPI 0.115 |
| Server | Uvicorn (ASGI) |
| Database | MongoDB via Motor (async) |
| Auth | JWT (HS256) + PBKDF2-SHA256 |
| Scraping | yt-dlp, BeautifulSoup4, httpx |
| Browser automation | Playwright + Camoufox (Spotify) |
| Templating | Jinja2 |
| Containerization | Docker |
| Deployment | Railway / Render / any Docker host |

---

## ◈ License

This project is **proprietary software** built by BotXCore.  
Do not copy, redistribute, or repurpose this code without written permission.

```
© 2026 BotXCore (xD3VS) — All rights reserved.
Read license header in each source file before use.
```

---

## ◈ Links

<div align="center">

```
┌────────────────────────────────────────────────────────┐
│                                                        │
│   SUPPORT    ──  https://t.me/BotXCore               │
│   UPDATES    ──  https://t.me/BotXCore            │
│   WEBSITE    ──  https://BotXCore.sbs                  │
│   DONATE     ──  https://Pay.BotXCore.sbs              │
│   DEVELOPER  ──  xD3VS  (Telegram)             │
│                                                        │
└────────────────────────────────────────────────────────┘
```

<img src="BotXCore-Logo.jpg" alt="BotXCore Banner" width="480" />

<br/>

**Built with dedication by [xD3VS](https://t.me/xD3VS)**  
*FAST · POWERFUL · ALL-IN-ONE*

</div>
