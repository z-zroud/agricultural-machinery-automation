import requests
from config import settings
import os
from helper.response import assert_success_response, Response

def admin_login(username='admin', password='123456'):
    path = 'api/v1/login'
    data = {
        'name': username,
        'password': password
    }
    resp = requests.post(os.path.join(settings.server, path), json=data)
    assert_success_response(resp)
    settings.token = Response(resp).data


def user_login(username, password='123456'):
    path = 'api/v1/admin'
    data = {
        'name': username,
        'password': password,
        'displayName': username,
        "role": 'personal'
    }
    resp = requests.post(os.path.join(settings.server, path), json=data)
    assert_success_response(resp)
    settings.token = Response(resp).data