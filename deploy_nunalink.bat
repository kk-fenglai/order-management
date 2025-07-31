@echo off
chcp 65001 >nul
echo.
echo ========================================
echo 集运管理系统 - Nunalink.com 部署工具
echo ========================================
echo.
echo 正在启动部署脚本...
echo.

cd /d "%~dp0"
python deploy/deploy_nunalink.py

echo.
echo 部署脚本执行完成！
echo 按任意键退出...
pause >nul 