# dashboard.py

import requests
import json

# Example: Pull IPs from AbuseIPDB
def fetch_abuseipdb(api_key):
    url = "https://api.abuseipdb.com/api/v2/blacklist"
    headers = {'Key': api_key, 'Accept': 'application/json'}
    response = requests.get(url, headers=headers)
    return response.json()

if __name__ == "__main__":
    API_KEY = "f2f7f946c489a2131bf1a2b7292ec955b974591eda2a6da6ac042c0b9d6fb7aa0009c85965bf13fb"
    data = fetch_abuseipdb(API_KEY)
    print(json.dumps(data, indent=2))
