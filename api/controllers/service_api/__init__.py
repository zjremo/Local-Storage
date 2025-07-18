from flask_restful import Api
from flask import Blueprint

# 创建蓝图，添加前缀/v1
bp = Blueprint("api", __name__)

# 创建API实例
api = Api(bp)

from . import index
from . import service
