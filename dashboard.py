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
    API_KEY = "your_api_key_here"
    data = fetch_abuseipdb(API_KEY)
    print(json.dumps(data, indent=2))
