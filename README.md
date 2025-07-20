# Local Password Book

![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![Flask](https://img.shields.io/badge/Flask-3.0%2B-lightgrey)
![MySQL](https://img.shields.io/badge/MySQL-8.0%2B-orange)

本地化密码存储小工具，通过Web界面安全存储账号凭证到MySQL数据库

## ✨ 核心功能

- 🔐 AES-128加密存储敏感数据
- 🗃️ docker拉取MySQL数据库存储
- 🌐 Flask-restful API + Node.js 前后端分离
- 🔄 数据加密/解密 支持插入、更新和删除记录

## 🚀 快速部署

### 环境需求
- Python 3.11+
- Node.js 24.4.1
- Docker

## 使用方法
1.docker拉取MySQL并进行启动
```python
docker-compose up -d
```
2.安装所需依赖(利用uv解决依赖)
```python
conda create -n cydb python=3.11
conda activate cydb
cd api
uv pip sync uv.lock
```
3.启动后端服务
```python
uv run flask run --host=0.0.0.0 --port=5001 --debug
```
4.运行前端环境
```python
cd web
node service.js
```
5.在浏览器输入`localhost:3000`即可访问
![image](https://github.com/user-attachments/assets/2003c7ab-de33-49f7-baae-c045f9bfdeb7)



