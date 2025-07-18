from flask import current_app
from flask_restful import Resource
from models import Account
from controllers import RequestProcessor
from . import api


# 服务介绍api
class Service(Resource):
    def get(self):
        return {
            "status": "success",
            "message": "Welcome to the Service API",
            "APPName": current_app.config["APPNAME"],
        }


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


# 注册路由
api.add_resource(Service, "/introduction")
api.add_resource(InsertdataApi, "/insert_data")
api.add_resource(UpdatedataApi, "/update_user")
api.add_resource(GetdataApi, "/get-users")
