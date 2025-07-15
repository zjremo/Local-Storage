# 此文件负责导入和设置日志格式
import logging

def init_app(app: CydbApp) -> None:
    """
    初始化日志格式, asctime: 时间, name: 日志名, levelname: 日志等级, message: 日志内容
    """
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
