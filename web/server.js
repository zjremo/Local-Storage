const express = require('express');
const path = require('path');
const axios = require('axios');
const { error } = require('console');
const app = express();
// 使用 body-parser 处理 POST 请求中的 JSON 数据
app.use(express.json());

// 提供静态文件（HTML、CSS、JS）
app.use('/static', express.static(path.join(__dirname, 'public/static')));

// 主页
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// 插入记录
app.post('/insert_data', (req, res) => {
    // 处理数据插入逻辑（调用Flask后端接口）
    const { username, password, user_explain, plugin } = req.body
    axios.post('http://localhost:5001/insert_data', {
        username,
        password,
        user_explain,
        plugin
    }).then(response => {
        res.json({ message: '数据插入成功!', data: response.data })
    }).catch(error => {
        console.error('调用后端服务失败:', error);
        // 打印错误信息
        res.status(500).json({ message: '插入数据失败，调用后端服务失败', error: error.message });
    })
});

// 更新记录信息
app.post('/update_data', (req, res) => {
    // 处理用户更新逻辑 (调用Flask后端接口)
    const {id, username, password, user_explain, plugin} = req.body
    axios.post('http://localhost:5001/update_data', {
        id,
        username,
        password,
        user_explain,
        plugin
    }).then(response => {
        res.json({message: '数据更新成功!', data: response.data})
    }).catch(error => {
        console.error('调用后端服务失败:', error);
        // 打印错误信息
        res.status(500).json({message: '更新数据失败，调用后端服务失败', error: error.message})
    })
});

app.post('/decrypt_data', (req, res) => {
    const {encrypted_password, plugin} = req.body
    axios.post('http://localhost:5001/decrypt_data', {
        encrypted_password,
        plugin
    }).then(response => {
        res.json({message:'数据解密成功!', data: response.data})
    }).catch(error => {
        console.error('调用后端服务失败:', error);
        res.status(500).json({message: '解密数据失败，调用后端服务失败', error: error.message})
    })
});

app.get('/get_data', async (req, res) => {
    try {
        // 向后端 Flask API 请求真实数据
        const response = await axios.get('http://localhost:5001/get_data');
        // 将后端返回的数据返回给前端
        res.json(response.data);
    } catch (error) {
        console.error('获取数据失败:', error.message);
        res.status(500).json({ message: '从后端获取数据失败', error: error.message });
    }
});

// 删除记录
app.post('/delete_data', (req, res) => {
    const { id } = req.body;
    axios.post('http://localhost:5001/delete_data', {
        id
    }).then(response => {
        res.json({ message: '数据删除成功!', data: response.data });
    }).catch(error => {
        console.error('调用后端服务失败:', error);
        res.status(500).json({ message: '删除数据失败', error: error.message });
    });
});

// 启动服务器
const PORT = 3000;
app.listen(PORT, () => {
    console.log(`服务器正在运行于 http://localhost:${PORT}`);
});
