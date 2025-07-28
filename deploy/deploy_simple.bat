@echo off
chcp 65001 >nul
echo 🚀 集运管理系统 - 简化云端部署工具
echo ================================================
echo 此工具将帮助您将应用部署到 Render 云端
echo 部署后，任何人都可以通过链接访问您的系统
echo ================================================

echo 📦 检查 Git 环境...
git --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Git 未安装，请先安装 Git
    echo 下载地址: https://git-scm.com/downloads
    pause
    exit /b 1
)
echo ✅ Git 已安装

echo.
echo 🔧 运行部署脚本...
python deploy_render.py

echo.
echo ⏸️ 按任意键退出...
pause >nul 