#!/usr/bin/env python3
"""
使用 ngrok 部署集运管理系统
让其他人可以通过公网链接访问您的应用
"""

import subprocess
import sys
import time
import requests
import os
from app import create_app

def install_ngrok():
    """安装 ngrok"""
    try:
        import pyngrok
        print("✅ ngrok 已安装")
        return True
    except ImportError:
        print("📦 正在安装 ngrok...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "pyngrok"])
            print("✅ ngrok 安装成功")
            return True
        except subprocess.CalledProcessError:
            print("❌ ngrok 安装失败")
            return False

def start_ngrok_tunnel(port=5000):
    """启动 ngrok 隧道"""
    try:
        from pyngrok import ngrok
        
        # 启动隧道
        print("🚀 正在启动 ngrok 隧道...")
        public_url = ngrok.connect(port)
        
        print("=" * 60)
        print("🌐 公网访问链接已创建！")
        print(f"📱 其他人可以通过以下链接访问：")
        print(f"🔗 {public_url}")
        print("=" * 60)
        print("💡 提示：")
        print("1. 这个链接可以让任何人访问您的应用")
        print("2. 链接会在您关闭程序后失效")
        print("3. 如果需要固定链接，请注册 ngrok 账号")
        print("=" * 60)
        
        return public_url
        
    except Exception as e:
        print(f"❌ 启动 ngrok 失败: {e}")
        return None

def main():
    """主函数"""
    print("🚀 集运管理系统 - ngrok 部署工具")
    print("=" * 50)
    
    # 安装 ngrok
    if not install_ngrok():
        return
    
    # 启动 Flask 应用
    print("🔧 正在启动 Flask 应用...")
    app = create_app()
    
    # 启动 ngrok 隧道
    public_url = start_ngrok_tunnel()
    if not public_url:
        return
    
    try:
        # 启动 Flask 应用
        print("🌐 启动 Flask 应用...")
        app.run(debug=False, host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        print("\n👋 正在关闭应用...")
    except Exception as e:
        print(f"❌ 应用启动失败: {e}")

if __name__ == '__main__':
    main() 