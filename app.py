# from dotenv import load_dotenv
# from flask import Flask

# # 创建flask app
# app = Flask(__name__, template_folder='templates', static_folder='static')

# # 全局配置加载
# load_dotenv('.env', override=True)
# passward = os.getenv('MYSQL_PASSWORD')
# hex_key = os.getenv('AES_KEY')

# # 使用flask sqlachemy连接数据库
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/local'
# db = SQLAlchemy(app)
from app_factory import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0" , port=5001)   



