# 此文件负责导入和设置日志格式
import logging
from cydb_app import CydbApp


def init_app(app: CydbApp) -> None:
    """
    初始化日志格式, asctime: 时间, name: 日志名, levelname: 日志等级, message: 日志内容
    """
    formatter = logging.Formatter(
        "[%(asctime)s] %(levelname)s in %(module)s: %(message)s"
    )

    # 控制台处理器
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    # 移除flask默认的处理器
    app.logger.handlers.clear()

    # 禁用 Flask 的默认日志行为
    app.logger.propagate = False

    # 添加自定义处理器
    app.logger.addHandler(stream_handler)
    app.logger.setLevel(logging.INFO)
