from helper.login import admin_login
from helper.device import add_device_type

def test_add_device_type():
    admin_login()
    add_device_type(device_type_id="at-devicetype", name="devicetype", desc="", type_string="typestring", model_id="pos")

