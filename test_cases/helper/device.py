from email import header
import requests
from config import settings
from helper.response import assert_success_response, Response
import os

def add_device_type(device_type_id, name, desc, model_id, type_string, brand='', link=''):
    path = 'api/v1/device/type'
    data = {
        "deviceTypeId": device_type_id,
        "name": name,
        "description": desc,
        "modelId":model_id,
        "typeString": type_string,
        "brand": brand,
        "link": link
    }
    headers = {}
    headers["Authorization"] = settings.token
    resp = requests.post(os.path.join(settings.server, path), json=data, headers=headers)
    assert_success_response(resp)
    return Response(resp)