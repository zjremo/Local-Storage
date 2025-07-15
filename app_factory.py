import logging
import time

from configs import cydb_config
from cydb_app import CydbApp
import cydb_app

def create_flask_app_with_configs() -> CydbApp:
    """
    创建flask应用，配置使用.env文件
    """
    # 创建flask应用
    cydb_app = CydbApp(__name__)
    # 使用model_dump将配置转为词典，然后利用from_mapping映射到config
    cydb_app.config.from_mapping(cydb_config.model_dump())

    return cydb_app

def create_app() -> CydbApp:
    start_time = time.perf_counter()
    app = create_flask_app_with_configs()
    # 加载扩展，比如路由等
    initialize_extensions(app)
    end_time = time.perf_counter()
    if cydb_config.DEBUG:
        logging.info(f"Finished create_app ({round((end_time - start_time) * 1000, 2)} ms)")
    return app

def initialize_extensions(app: cydb_app):
    pass
