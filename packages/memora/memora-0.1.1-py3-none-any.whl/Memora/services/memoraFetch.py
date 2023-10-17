import json
import requests
from Memora.config import config
from typing import Dict, Optional

def memoraFetch(token: str, path: str, method: str, body: Optional[Dict] = None):
    if not token:
        raise ValueError('You need to set your API key using memora.auth().')

    headers = {
        'X-Api-Key': token,
    }

    if body is not None:
        headers['Content-Type'] = 'application/json'
        body = json.dumps(body)

    url = f"{config['baseUrl']}{path}"
    response = requests.request(method, url, headers=headers, data=body)

    return response
