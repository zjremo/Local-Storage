from flask import current_app
from flask_restful import Resource
from models import Account
from controllers import RequestProcessor
from crypto import aes_decrypt
from . import api
import base64


# 添加数据记录api
class InsertdataApi(Resource):
    def post(self):
        # 加密password
        data_json = RequestProcessor.process_request_data()
        # 添加记录到Account表中
        return Account.CreateAccount(data_json)


# 更新数据记录api
class UpdatedataApi(Resource):
    def post(self):
        data_json = RequestProcessor.process_request_data()
        # 更新记录到Account表中
        return Account.UpdateAccount(data_json)


# 获取全部数据记录api
class GetdataApi(Resource):
    def get(self):
        return Account.GetAllAccount()


# 解密数据记录api
class DecryptdataApi(Resource):
    def post(self):
        data_json = RequestProcessor.process_request_data()
        if "encrypted_password" in data_json:
            preprocessdata = data_json["encrypted_password"].encode("utf-8")
            hex_key = current_app.config.get("CRYPTO_KEY", str)
            decrypted_password = aes_decrypt(preprocessdata, hex_key=hex_key).decode(
                "utf-8"
            )
            return {
                "status": "success",
                "message": "decrypted password success!",
                "decrypted_password": decrypted_password,
            }
        else:
            current_app.logger.error(
                "Failed to decrypt password, because no password has been provided!"
            )
            return {
                "status": "success",
                "message": "Failed to decrypt password, because no password has been provided!",
            }


# 删除数据记录api
class DeletedataApi(Resource):
    def post(self):
        data_json = RequestProcessor.process_request_data()
        return Account.DeleteAccount(data_json)


# 注册路由
api.add_resource(InsertdataApi, "/insert_data")
api.add_resource(UpdatedataApi, "/update_data")
api.add_resource(GetdataApi, "/get_data")
api.add_resource(DecryptdataApi, "/decrypt_data")
api.add_resource(DeletedataApi, "/delete_data")
