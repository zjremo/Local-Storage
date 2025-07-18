from cydb_app import CydbApp
from models import db


# 用app中的配置来初始化db
def init_app(app: CydbApp) -> None:
    db.init_app(app)
