from app_factory import create_app

# mysql支持
import pymysql

pymysql.install_as_MySQLdb()
# 创建app
app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
