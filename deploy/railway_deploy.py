#!/usr/bin/env python3
"""
Railway 云部署工具
一键将集运管理系统部署到云端，让任何人都可以访问
"""

import os
import subprocess
import sys
import json
import time

def check_git():
    """检查 Git 是否安装"""
    try:
        subprocess.run(['git', '--version'], check=True, capture_output=True)
        print("✅ Git 已安装")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ Git 未安装，请先安装 Git")
        print("下载地址: https://git-scm.com/downloads")
        return False

def check_node():
    """检查 Node.js 是否安装"""
    try:
        subprocess.run(['node', '--version'], check=True, capture_output=True)
        print("✅ Node.js 已安装")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ Node.js 未安装，请先安装 Node.js")
        print("下载地址: https://nodejs.org/")
        return False

def init_git_repo():
    """初始化 Git 仓库"""
    if not os.path.exists('.git'):
        print("📦 初始化 Git 仓库...")
        subprocess.run(['git', 'init'], check=True)
        subprocess.run(['git', 'add', '.'], check=True)
        subprocess.run(['git', 'commit', '-m', 'Initial commit'], check=True)
        print("✅ Git 仓库初始化完成")
    else:
        print("✅ Git 仓库已存在")

def create_railway_config():
    """创建 Railway 配置文件"""
    print("⚙️ 创建 Railway 配置文件...")
    
    # 确保 Procfile 存在
    if not os.path.exists('Procfile'):
        with open('Procfile', 'w', encoding='utf-8') as f:
            f.write('web: python run_app.py\n')
    
    # 确保 railway.json 存在
    if not os.path.exists('railway.json'):
        with open('railway.json', 'w', encoding='utf-8') as f:
            json.dump({
                "$schema": "https://railway.app/railway.schema.json",
                "build": {
                    "builder": "NIXPACKS"
                },
                "deploy": {
                    "startCommand": "python run_app.py",
                    "healthcheckPath": "/",
                    "healthcheckTimeout": 100,
                    "restartPolicyType": "ON_FAILURE",
                    "restartPolicyMaxRetries": 10
                }
            }, f, indent=2, ensure_ascii=False)
    
    print("✅ Railway 配置文件创建完成")

def install_railway_cli():
    """安装 Railway CLI"""
    try:
        print("📦 检查 Railway CLI...")
        subprocess.run(['railway', '--version'], check=True, capture_output=True)
        print("✅ Railway CLI 已安装")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("📦 安装 Railway CLI...")
        try:
            subprocess.run(['npm', 'install', '-g', '@railway/cli'], check=True)
            print("✅ Railway CLI 安装成功")
            return True
        except subprocess.CalledProcessError:
            print("❌ Railway CLI 安装失败")
            return False

def deploy_to_railway():
    """部署到 Railway"""
    print("🚀 开始部署到 Railway...")
    
    try:
        # 登录 Railway
        print("🔐 请在弹出的浏览器窗口中登录 Railway...")
        subprocess.run(['railway', 'login'], check=True)
        
        # 创建新项目
        print("📁 创建 Railway 项目...")
        subprocess.run(['railway', 'init'], check=True)
        
        # 部署项目
        print("🚀 部署项目...")
        subprocess.run(['railway', 'up'], check=True)
        
        # 获取域名
        print("🌐 获取访问域名...")
        result = subprocess.run(['railway', 'domain'], check=True, capture_output=True, text=True)
        domain = result.stdout.strip()
        
        print("=" * 60)
        print("🎉 部署成功！")
        print(f"🌐 您的应用地址: {domain}")
        print("=" * 60)
        print("💡 使用说明:")
        print("1. 这个链接可以分享给任何人")
        print("2. 系统24/7在线，无需您的电脑运行")
        print("3. 数据会自动保存到云端")
        print("4. 如需修改，请重新运行此脚本")
        print("=" * 60)
        
        return domain
        
    except subprocess.CalledProcessError as e:
        print(f"❌ 部署失败: {e}")
        return None

def main():
    """主函数"""
    print("🚀 集运管理系统 - Railway 云部署工具")
    print("=" * 50)
    print("此工具将帮助您将应用部署到云端")
    print("部署后，任何人都可以通过链接访问您的系统")
    print("=" * 50)
    
    # 检查依赖
    if not check_git():
        return
    
    if not check_node():
        return
    
    # 初始化 Git 仓库
    init_git_repo()
    
    # 创建 Railway 配置
    create_railway_config()
    
    # 安装 Railway CLI
    if not install_railway_cli():
        return
    
    # 部署到 Railway
    domain = deploy_to_railway()
    
    if domain:
        print(f"\n🎉 恭喜！您的集运管理系统已成功部署到云端！")
        print(f"🌐 访问地址: {domain}")
        print("\n现在您可以:")
        print("1. 分享这个链接给团队成员")
        print("2. 在任何设备上访问系统")
        print("3. 关闭您的电脑，系统依然在线")
        print("4. 享受24/7的云端服务")
    else:
        print("\n❌ 部署失败，请检查错误信息并重试")

if __name__ == '__main__':
    main() 