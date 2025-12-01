
# config.py
# --- Edit these values before running ---

# Telegram Bot settings
BOT_TOKEN = "7859423336:AAEfFg13-RuiWZGEUjrfIMGna4K4Ouay8HU"
ADMIN_ID = 6379161238
GROUP_ID = -1003289627261
OWNER_LINK = "Https://t.me/LootFiHunter"


# ==========================================================
# IVASMS Login Credentials
# ==========================================================
LOGIN_URL = "https://www.ivasms.com/login"
LOGIN_EMAIL = "fujivczy@hi2.in"
LOGIN_PASSWORD = "As6379161238@"

# IVASMS endpoints
BASE = "https://www.ivasms.com"
GET_SMS_URL = f"{BASE}/portal/sms/received/getsms"
GET_NUMBER_URL = f"{BASE}/portal/sms/received/getsms/number"
GET_OTP_URL = f"{BASE}/portal/sms/received/getsms/number/sms"

# ==========================================================
# Session and CSRF token (leave these as they are)
# ==========================================================
SESSION_COOKIE = "eyJpdiI6IjA5aXh6aWZxUnBWR2YzbTBoTm1xTnc9PSIsInZhbHVlIjoiQnpBUGxsNEpQRUlwRXNUcmcyb1R1dGluYmYrdGFRUWZnVmJMd1R0ZHc1YkV2d2syUDRQYVJsL21mOUVWL3hKTEk5QnFJUW1TSjJwdDR6MkNGMkNTVWc4RzhXRzJTc2UraG9POFliNWNGVHE3VDV2L3NBUllPUXp1MGNsQ2Z2SEgiLCJtYWMiOiI3MzYwYzAzMDdjMWYwYmQ3ZGU3YmFjN2I3MTE4M2RjMmEyOTU3NmNkNTRmNTdmNzRlN2UxMmRiZDFmMjM3MTcyIiwidGFnIjoiIn0%3D"
CSRF_TOKEN = "eyJpdiI6ImlLbmR5enNuS0Q5SmE2em41VnZnV0E9PSIsInZhbHVlIjoiT0N0Q0Zsd0ZWSk84NEJJbW9nTC9GMlJOcWRsSS80N2U3MDRBc3lCRWFVdy9pYXJGR2RCbFVYTHlQRWVPcEJ3a2xmS25JLzd3ZkJBbUY1YlpqM0QvNzlvREdmOXVjWGxHZTU4NFNBc1hBRURnT0o3Tmk5NFhoZFVMdU9UYk04YW8iLCJtYWMiOiI2MDZhZWYxYzE1ZDdjYzBjMDU0ODgzYzU3NmJkYTcwZDFkMTVhZWJlMTBjNzMyMTExNmY3NzFlM2VhZjU1OGM1IiwidGFnIjoiIn0%3D"

# Request headers (don't change unless necessary)
HEADERS = {
    "Origin": "https://www.ivasms.com",
    "Referer": "https://www.ivasms.com/portal/sms/received",
    "User-Agent": "Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "Accept": "application/json, text/javascript, */*; q=0.01"
}

# Polling interval (seconds)
FETCH_INTERVAL = 6

# DB file
DB_FILE = "otps_and_errors.db"
# ==========================================================
# Country and Service Mappings
# ==========================================================
COUNTRY_FLAGS = {
    "234": "🇳🇬 Nigeria",
    "880": "🇧🇩 Bangladesh",
    "51": "🇵🇪 Peru",
    "225": "🇨🇮 Ivory Coast",
    "20": "🇪🇬 Egypt",
    "255": "🇹🇿 Tanzania",
    "44": "🇬🇧 United Kingdom",
    "58": "🇻🇪 Venezuela",
    "996": "🇰🇬 Kyrgyzstan",
    "593": "🇪🇨 Ecuador",
    "591": "🇧🇴 Bolivia",
    "228": "🇹🇬 Togo",
    "221": "🇸🇳 Senegal",
    "1": "🇺🇸 United States",
    "970": "🇵🇸 Palestine",
    "98": "🇮🇷 Iran",
    "964": "🇮🇶 Iraq",
    "966": "🇸🇦 Saudi Arabia",
    "236": "🇨🇫 Central African Republic",
    "93": "🇦🇫 Afghanistan",
    "261": "🇲🇬 Madagascar",
    "977": "🇳🇵 Nepal",
    "967": "🇾🇪 Yemen",
    "998": "🇺🇿 Uzbekistan",
    "216": "🇹🇳 Tunisia",
    "963": "🇸🇾 Syria",
    # Sabbin Ƙasashe
    "229": "🇧🇯 Benin",
    "63": "🇵🇭 Philippines",
    "60": "🇲🇾 Malaysia",
    "992": "🇹🇯 Tajikistan",
    "254": "🇰🇪 Kenya"
}

# An ƙara wasu kalmomi don gane sabis da kyau
SERVICES = {
    "whatsapp": "WhatsApp",
    "facebook": "Facebook",
    "meta": "Facebook",
    "fb": "Facebook",
    "telegram": "Telegram",
    "google": "Google",
    "instagram": "Instagram",
    "signal": "Signal",
    "snapchat": "Snapchat",
    "tiktok": "Tiktok",
    "twitter": "Twitter",
    "premierbet": "Premier Bet",
    "premier bet": "Premier Bet",
    # Sabbin Ayyuka
    "truecaller": "Truecaller",
    "netflix": "Netflix",
    "microsoft": "Microsoft",
    "binance": "Binance",
    "twilio":  "Twilio"
}

# Masking rule: keep first N chars then **** then last M chars
MASK_PREFIX_LEN = 7
MASK_SUFFIX_LEN = 3
