from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

MYSQL_INDEXES_NAMING_CONVENTION = {
    # 数据库索引
    "ix": "ix_%(column_0_N_label)s",
    # 唯一约束
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    # 检查约束
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    # 外键约束
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    # 主键约束
    "pk": "pk_%(table_name)s",
}

metadata = MetaData(naming_convention=MYSQL_INDEXES_NAMING_CONVENTION)

db = SQLAlchemy(metadata=metadata)
