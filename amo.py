import time

import requests
import json
import hashlib
import hmac
from datetime import datetime
import random


def make_order(name, order):
    try:
        session = requests.Session()
        response = session.get('https://kevgenev8.amocrm.ru/')
        session_id = response.cookies.get('session_id')
        csrf_token = response.cookies.get('csrf_token')
        headers = {
            'Accept': 'application/json',
            'X-Requested-With': 'XMLHttpRequest',
            'Cookie': f'session_id={session_id}; '
                      f'csrf_token={csrf_token};'
                      f'last_login=kevgenev8@mail.ru',
            'Host': 'kevgenev8.amocrm.ru',
            'Origin': 'https://kevgenev8.amocrm.ru',
            'Referer': 'https://kevgenev8.amocrm.ru/',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
        }
        payload = {
            'csrf_token': csrf_token,
            'password': "Xh1wdBlk",
            'temporary_auth': "N",
            'username': "kevgenev8@mail.ru"}

        response = session.post('https://kevgenev8.amocrm.ru/oauth2/authorize', headers=headers, data=payload)
        access_token = response.cookies.get('access_token')
        refresh_token = response.cookies.get('refresh_token')
        headers['access_token'] = access_token
        headers['refresh_token'] = refresh_token
        url = 'https://kevgenev8.amocrm.ru/ajax/leads/multiple/add/'
        data = {
            'new_deal[0][name]': order,
            'new_deal[0][price]': '',
            'new_deal[0][contact_name]': name,
            'new_deal[0][company_name]': '',
            'new_deal[0][pipeline_id]': 6786474,
            'new_deal[0][create_contact]': 'true',
            'new_deal[0][create_company]': 'false',
            'pipeline': 'Y'
        }
        resp = session.post(url, data=data, headers=headers)
        print(resp.text)
    except:
        time.sleep(3)
        return make_order(name, order)


