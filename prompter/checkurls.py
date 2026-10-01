import sys
import requests
import re
import warnings
from datetime import datetime

def extract_urls(markdown_text):
    return re.findall(r"\[[^]]*\]\(([^)]*)\)", markdown_text)

def check_urls(markdown_text):
    urls = extract_urls(markdown_text)
    return [download_webpage(url) for url in urls]

def download_webpage(url):
    request_ts = datetime.now().isoformat()
    response = requests.get(url, timeout=30)
    response_ts = datetime.now().isoformat()

    return {"url": url, "request_ts": request_ts, "response_ts": response_ts, "status": f"{response.status_code} {response.reason}"}
