import os

PROXY_LIST = [
    "38.180.27.230:2024", "161.97.74.176:32050",
    "103.127.223.126:1080", "98.191.0.37:4145"
]

URL = os.getenv("TARGET_URL", "https://staging-bo.agencerdas.id/login/")
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded"
}

REQUEST_TIMEOUT = 10  # Dalam detik
