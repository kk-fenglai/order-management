@echo off
chcp 65001 >nul
echo 🚀 集运管理系统 - 一键部署工具
echo ================================================
echo 正在打开部署工具包...
echo.

echo 📁 部署文件夹位置：
echo %cd%\deploy
echo.

echo 🎯 推荐部署方案：
echo 1. Render 云端部署（推荐）- 双击 deploy_simple.bat
echo 2. Railway 云端部署 - 双击 deploy_cloud.bat  
echo 3. ngrok 本地隧道 - 双击 start_public.bat
echo.

echo 📚 详细指南：
echo - 快速部署指南.md
echo - 云端部署指南.md
echo - 部署指南.md
echo.

echo 🔧 正在打开部署文件夹...
explorer deploy

echo.
echo ⏸️ 按任意键退出...
pause >nul 