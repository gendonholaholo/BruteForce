from bruteforce_tester.config import URL, HEADERS
from bruteforce_tester.brute_force import BruteForceTester
from bruteforce_tester.config import PROXY_LIST

if __name__ == "__main__":
    use_proxy = False
    proxies = PROXY_LIST if use_proxy else []
    tester = BruteForceTester(URL, HEADERS, proxies=proxies, max_threads=10)
    tester.start()  # Menjalankan brute force
