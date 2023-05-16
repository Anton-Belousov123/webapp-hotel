import requests
import json
import hashlib
import hmac
from datetime import datetime


def make_order(name, order):
    secret = 'c506ff3d57fca1998e50ea8076ef7afc27934f65'
    method = 'POST'
    contentType = 'application/json'
    date = datetime.now().strftime('%a, %d %b %Y %H:%M:%S %Z')
    path = '/v2/origin/custom/0de9c1dd-b5d8-4b38-bb7f-ef238bb3ca86_7eb31c63-e74d-41cd-86f7-34c6265386f9'

    url = "https://amojo.amocrm.ru" + path

    body = {
        'event_type': 'new_message',
        'payload': {
            'timestamp': int(datetime.now().timestamp()),
            'msec_timestamp': round(datetime.now().timestamp() * 1000),
            'msgid': '1',
            'conversation_id': '1',
            'sender': {
                'id': 'my_int-1376265f-86df-4c49-a0c3-a4816df41af8',
                'name': f'{name}'
            },
            'message': {
                'type': 'text',
                'text': order,
            },
            'silent': False,
        },
    }

    request_body = json.dumps(body)
    checksum = hashlib.md5(request_body.encode('utf-8')).hexdigest()
    signature = hmac.new(secret.encode('utf-8'), json.dumps(body).encode('UTF-8'), hashlib.sha1).hexdigest()
    data = request_body.encode('utf-8') + date.encode('utf-8')

    headers = {
        'Date': date,
        'Content-Type': 'application/json',
        'Content-MD5': checksum.lower(),
        'X-Signature': signature.lower(),
    }


    response = requests.post(url, headers=headers, data=request_body)
