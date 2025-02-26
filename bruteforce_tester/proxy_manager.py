import requests
import logging
import time

logging.basicConfig(
    filename="logs/proxy_manager.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class ProxyManager:
    def __init__(self, proxy_list):
        self.proxy_list = proxy_list
        self.index = 0
        print(f"Loaded {len(self.proxy_list)} proxies: {self.proxy_list}")

    def get_next_proxy(self):
        if not self.proxy_list:
            logging.warning("Proxy list is empty, running without proxy.")
            return None

        for _ in range(len(self.proxy_list)):
            proxy = self.proxy_list[self.index]
            logging.info(f"Checking proxy: {proxy}")

            self.index = (self.index + 1) % len(self.proxy_list)
            if self.is_proxy_working(proxy):
                logging.info(f"Using valid proxy: {proxy}")
                return {"http": proxy, "https": proxy}

        logging.error("No working proxy found. Retrying in 10 seconds...")
        time.sleep(10)
        return self.get_next_proxy()

    def is_proxy_working(self, proxy):
        try:
            response = requests.get("https://www.google.com", proxies={"http": proxy, "https": proxy}, timeout=3)
            return response.status_code == 200
        except requests.RequestException:
            return False
