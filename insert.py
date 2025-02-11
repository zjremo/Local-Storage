from flask import Flask, request, jsonify,send_from_directory,render_template
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
import os
import re


app = Flask(__name__,
            template_folder='templates',
            static_folder='static')



load_dotenv(r'D:\桌面\.env')
password = os.getenv('MYSQL_PASSWORD')
key = os.getenv('AES_KEY')
# 连接数据库
def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password=password,
        database='local'
    )
    return connection

def aes_encrypt(data, key):

            cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC)

            padded_data = pad(data.encode('utf-8'), AES.block_size)

            encrypted = cipher.encrypt(padded_data)

            return base64.b64encode(cipher.iv + encrypted).decode('utf-8')


@app.route('/insert_data', methods=['POST'])
def insert_data():
     try:
        data = request.get_json()

        username = data.get('username')
        password = data.get('password')
        user_explain = data.get('user_explain')
        plugin = data.get('plugin')
        password = aes_encrypt(password,key)

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT id FROM account ORDER BY id DESC LIMIT 1;")
        last_id = cursor.fetchone()
        if last_id is None:
            number_id = 1
        else:
            last_id = last_id[0]
            number_id = last_id + 1
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



@app.route('/update_user', methods=['POST'])
def update_user():
    try:
        data = request.get_json()
        number_id = data.get('id')
        username = data.get('username')
        password = data.get('password')
        user_explain = data.get('user_explain')
        plugin = data.get('plugin')

        if not number_id:
            return jsonify({"message": "User ID must be provided!"}), 400

        password = aes_encrypt(password, key)

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM account;")

        check_id = cursor.fetchall()
        id_list = {row[0] for row in check_id}

        target_id = r"\b" + number_id +r"\b"
        if re.findall(target_id, str(id_list)):
            pass
        else:
            return jsonify({"message": "ID does not exist."}), 400


        query = '''
                UPDATE account
                SET username = %s,
                    password = %s,
                    user_explain = %s,
                    plugin = %s
                WHERE id = %s;
           '''
        cursor.execute(query, (username, password, user_explain, plugin,number_id))
        conn.commit()

        cursor.close()
        conn.close()
        return jsonify({"message": "Data update successful"}), 200
    except Error as e:
        print(f"Error: {e}")
        return jsonify({"message": "密码更新失败!", "error": str(e)}), 500


#查询所有数据
@app.route('/get-users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Unable to connect to the database"}), 500

    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT username, password, user_explain,plugin FROM account")
        users = cursor.fetchall()

        user_list = []
        for idx,all_data in enumerate(users, start=1):
            Completed=all_data['password'] = all_data['password'].decode('utf-8')
            all_data['id'] = idx
            user_list.append(all_data)

    except Error as e:
        return jsonify({"error": f"Error fetching data: {e}"}), 500
    finally:
        cursor.close()
        conn.close()

    return jsonify(user_list)


@app.route('/decrypt', methods=['POST'])
def decrypt_password():
    data = request.get_json()
    encrypted_password = data['encrypted_password']
    plugin = data['plugin']

    encrypted_data = base64.b64decode(encrypted_password)

    iv = encrypted_data[:AES.block_size]

    encrypted_text = encrypted_data[AES.block_size:]

    cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv)

    decrypted = unpad(cipher.decrypt(encrypted_text), AES.block_size)

    decrypted = decrypted.decode('utf-8')

    return jsonify({
        'success': True,
        'decrypted_password': decrypted
    })

@app.route('/')
def index():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8081)

