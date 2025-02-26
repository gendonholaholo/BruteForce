import requests

def send_request(url, username, password, headers):
    data = {"username": username, "password": password}
    response = requests.post(url, headers=headers, data=data, allow_redirects=False)
    return response
