@echo off
echo ========================================
echo 集运管理系统 - Anaconda启动脚本
echo ========================================
echo.

REM 检查是否在Anaconda环境中
python -c "import sys; print('Anaconda环境:', 'anaconda' in sys.executable.lower() or 'conda' in sys.executable.lower())"

echo.
echo 正在启动系统...
echo 邮件配置: alzy1210@163.com
echo 访问地址: http://localhost:5000
echo.
echo 按 Ctrl+C 停止服务
echo ========================================

REM 运行Python应用
python run_app.py

pause 