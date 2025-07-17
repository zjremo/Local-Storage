from flask import current_app, request
from crypto import aes_encrypt


# 对request进行预处理
class RequestProcessor:
    @classmethod
    def process_request_data(cls):
        # request里面提取表单信息
        data_json = request.get_json()
        password = data_json.get("password")
        hex_key = current_app.config.get("CRYPTO_KEY", str)
        password = aes_encrypt(password, hex_key)
        data_json["password"] = password
        return data_json
