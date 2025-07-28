@echo off
chcp 65001 >nul
echo 🚀 启动集运管理系统 - 公网访问版本
echo ================================================

echo 📦 检查并安装依赖...
pip install pyngrok

echo 🚀 启动应用...
python deploy_ngrok.py

pause 