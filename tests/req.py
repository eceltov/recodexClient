# my_module.py
import urllib3
import json

http = urllib3.PoolManager()

def fetch_data(url):
    try:
        resp = http.request('GET', url)
        if resp.status == 200:
            return json.loads(resp.data.decode('utf-8'))
        else:
            return None
    except urllib3.exceptions.MaxRetryError as e:
        print(f"Max retries exceeded: {e}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def post_data(url, data):
    try:
        encoded_data = json.dumps(data).encode('utf-8')
        resp = http.request('POST', url, body=encoded_data, headers={'Content-Type': 'application/json'})
        if resp.status == 200:
            return json.loads(resp.data.decode('utf-8'))
        else:
            return None
    except Exception as e:
        print(f"An error occurred during POST: {e}")
        return None