from flask import Flask, request, jsonify,send_from_directory
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
import os

app = Flask(__name__)

load_dotenv(r'/系统脚本/.env')
password = os.getenv('MYSQL_PASSWORD')
# 连接数据库
def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',       # 数据库主机
        user='root',            # 数据库用户名
        password=password,  # 数据库密码
        database='local'   # 数据库名称
    )
    return connection

#插入数据
@app.route('/insert_data', methods=['POST'])
def insert_data():
     try:
        data = request.get_json()

        username = data.get('username')
        password = data.get('password')
        user_explain = data.get('user_explain')
        plugin = data.get('plugin')
        key = '0e03759119cf0310c14f9f06a2699413'

        def aes_encrypt(data, key):
            cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC)

            padded_data = pad(data.encode('utf-8'), AES.block_size)

            encrypted = cipher.encrypt(padded_data)

            return base64.b64encode(cipher.iv + encrypted).decode('utf-8')

        password = aes_encrypt(password,key)

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT id FROM account ORDER BY id DESC LIMIT 1;")
        last_id = cursor.fetchone()[0]
        number_id = last_id + 1
        # SQL 插入语句
        query = '''
            INSERT INTO account (id,username, `password`, user_explain, `plugin`)
            VALUES (%s,%s, %s, %s, %s)
        '''
        cursor.execute(query, (number_id,username, password, user_explain, plugin))
        conn.commit()

        cursor.close()
        conn.close()

        return jsonify({"message": "Data inserted successfully"}), 200

     except Error as e:
        print(f"Error: {e}")
        return jsonify({"message": "Failed to insert data", "error": str(e)}), 500


#查询数据库最后一行数据
@app.route('/get_last_row', methods=['GET'])
def get_last_row():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM account ORDER BY id DESC LIMIT 1")
    last_row = cursor.fetchone()
    last_row['password'] = last_row['password'].decode('utf-8')

    cursor.close()
    connection.close()

    if last_row:
        return jsonify({'success': True, 'last_row': last_row})
    else:
        return jsonify({'success': False, 'message': 'No data found.'})


@app.route('/')
def index():
    return send_from_directory('templates', 'index.html')



if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8081)

