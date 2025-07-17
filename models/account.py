from flask import jsonify
from sqlalchemy import desc
from .base import Base
from .engine import db
import logging

logger = logging.Logger(__name__)


class Account(Base):
    __tablename__ = "account"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.LargeBinary(255), nullable=False)
    user_explain = db.Column(db.String(255), nullable=False)
    plugin = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<Account {self.username}>"

    def __str__(self):
        return f"<Account {self.username}>"

    @classmethod
    def CreateAccount(cls, account_data):
        """
        创建账号
        """
        try:
            account = cls(**account_data)
            db.session.add(account)
            db.session.commit()
            logger.info(f"Account created successfully {account}")
            return {
                "status": "success",
                "message": "Account created successfully",
            }, 200
        except Exception as e:
            db.session.rollback()
            logger.info(f"Failed to create account: {e}")
            return {
                "status": "error",
                "message": "Failed to create account",
                "error": str(e),
            }, 500

    @classmethod
    def update_record(cls, record, account_data):
        for key, value in account_data.items():
            setattr(record, key, value)

    @classmethod
    def UpdateAccount(cls, account_data):
        """
        更新账号
        """
        number_id = account_data.get("id")
        if not number_id:
            return jsonify({"message": "User ID must be provided!"}), 400
        try:
            record = db.session.query(cls).filter_by(id=number_id).first()
            if record:
                cls.update_record(record, account_data=account_data)
            else:
                return jsonify({"message": "ID does not exist."}), 400
        except Exception as e:
            db.session.rollback()
            logger.error(f"Failed to process account data. Details: {e}")
            return {
                "status": "error",
                "message": "Failed to update account",
                "error": str(e),
            }, 500

    @classmethod
    def GetAllAccount(cls):
        """
        获取所有账号
        """
        try:
            # 按照id从小到大排序
            records = db.session.query(cls).order_by(cls.id).all()
            if records:
                # 封装为字典列表
                account_list = [
                    {
                        "id": record.id,
                        "username": record.username,
                        "password": record.password,
                        "user_explain": record.user_explain,
                        "plugin": record.plugin,
                    }
                    for record in records
                ]
                return jsonify(account_list), 200
        except Exception as e:
            return jsonify({"error": f"Error fetching data: {e}"}), 500
