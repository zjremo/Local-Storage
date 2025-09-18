from flask import Flask, request, jsonify, session

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

@app.route('/login', methods=['POST'])
def login():
    """登录接口"""
    data = request.get_json()
    password = data.get('password')

    if password == 'hello':
        # 登录成功，设置session
        session['hello'] = 'hkjk'
        return jsonify({
            'success': True,
            'message': '登录成功'
        })
    else:
        return jsonify({
            'success': False,
            'message': '密码错误'
        }), 401


@app.route('/check-auth', methods=['GET'])
def check_auth():
    """检查登录状态"""
    if 'hello' in session and session['hello'] == 'hkjk':
        return jsonify({
            'authenticated': True,
            'message': '已登录',
            'session_data': session['hello']
        })
    else:
        return jsonify({
            'authenticated': False,
            'message': '未登录'
        }), 401


@app.route('/protected', methods=['GET'])
def protected():
    """需要认证的接口"""
    if 'hello' not in session or session['hello'] != 'hkjk':
        return jsonify({
            'success': False,
            'message': '请先登录'
        }), 401

    return jsonify({
        'success': True,
        'message': '这是受保护的数据',
        'data': '只有登录用户才能看到这个内容'
    })


@app.route('/logout', methods=['POST'])
def logout():
    """登出接口"""
    session.pop('hello', None)
    return jsonify({
        'success': True,
        'message': '已退出登录'
    })


if __name__ == '__main__':
    app.run(debug=True, port=5000)