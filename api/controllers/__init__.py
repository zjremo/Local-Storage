from flask import current_app, request


# 对request进行预处理
class RequestProcessor:
    @classmethod
    def process_request_data(cls):
        # request里面提取表单信息
        data_json = request.get_json()
        if "password" in data_json:
            password = data_json.get("password")
            hex_key = current_app.config.get("CRYPTO_KEY", str)
            from crypto import aes_encrypt

            password = aes_encrypt(password, hex_key)
            data_json["password"] = password
        return data_json
