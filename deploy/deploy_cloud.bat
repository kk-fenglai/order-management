@echo off
chcp 65001 >nul
echo 🚀 集运管理系统 - 云端部署工具
echo ================================================
echo 此工具将帮助您将应用部署到云端
echo 部署后，任何人都可以通过链接访问您的系统
echo ================================================

echo 📦 检查并安装依赖...
echo.

echo 🔧 运行云端部署脚本...
python railway_deploy.py

echo.
echo ⏸️ 按任意键退出...
pause >nul 