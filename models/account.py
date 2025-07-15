from .base import Base
from .engine import db

class Account(Base):
    __tablename__ = 'account'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.LargeBinary(255), nullable=False)
    user_explain = db.Column(db.String(255), nullable=False)
    plugin = db.Column(db.String(255), nullable=False)
    
    def __repr__(self):
        return f'<Account {self.username}>'
    
    def __str__(self):
        return f'<Account {self.username}>'

    @classmethod
    def create(cls, username, password, user_explain, plugin):
        """
        创建账号
        """
        account = cls(
            username=username,
            password=password,
            user_explain=user_explain,
            plugin=plugin
        )
        db.session.add(account)
        db.session.commit()
        return account

    