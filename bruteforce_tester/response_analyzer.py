from bs4 import BeautifulSoup

def analyze_response(response):
    if response.status_code == 200 and "dashboard" in response.text.lower():
        return True
    return False
