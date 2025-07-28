#!/usr/bin/env python3
"""
Render 云端部署工具
一键将集运管理系统部署到 Render 云端
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

def create_render_config():
    """创建 Render 配置文件"""
    print("⚙️ 创建 Render 配置文件...")
    
    # 确保 Procfile 存在
    if not os.path.exists('Procfile'):
        with open('Procfile', 'w', encoding='utf-8') as f:
            f.write('web: python run_app.py\n')
    
    # 确保 render.yaml 存在
    if not os.path.exists('render.yaml'):
        with open('render.yaml', 'w', encoding='utf-8') as f:
            f.write('''services:
  - type: web
    name: order-management-system
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: python run_app.py
    envVars:
      - key: PYTHON_VERSION
        value: 3.9.0
      - key: MAIL_SERVER
        value: smtp.163.com
      - key: MAIL_PORT
        value: 465
      - key: MAIL_USE_SSL
        value: True
      - key: MAIL_USERNAME
        value: alzy1210@163.com
      - key: MAIL_PASSWORD
        value: MAjQjkgenAqciFEW
      - key: SECRET_KEY
        value: your-secret-key-here-change-this
      - key: FLASK_ENV
        value: production
''')
    
    print("✅ Render 配置文件创建完成")

def create_github_repo():
    """创建 GitHub 仓库"""
    print("🌐 创建 GitHub 仓库...")
    print("请按照以下步骤操作：")
    print("1. 访问 https://github.com/new")
    print("2. 仓库名称输入: order-management-system")
    print("3. 选择 Public（公开）")
    print("4. 点击 'Create repository'")
    print("5. 复制仓库地址（类似: https://github.com/your-username/order-management-system.git）")
    
    repo_url = input("请输入您的 GitHub 仓库地址: ").strip()
    
    if not repo_url:
        print("❌ 未输入仓库地址，部署取消")
        return False
    
    try:
        # 添加远程仓库
        subprocess.run(['git', 'remote', 'add', 'origin', repo_url], check=True)
        
        # 推送到 GitHub
        print("📤 推送到 GitHub...")
        subprocess.run(['git', 'branch', '-M', 'main'], check=True)
        subprocess.run(['git', 'push', '-u', 'origin', 'main'], check=True)
        
        print("✅ 代码已推送到 GitHub")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ 推送到 GitHub 失败: {e}")
        return False

def deploy_to_render():
    """部署到 Render"""
    print("🚀 部署到 Render...")
    print("请按照以下步骤操作：")
    print("1. 访问 https://render.com/")
    print("2. 点击 'Sign Up' 注册账号（可以用 GitHub 账号登录）")
    print("3. 登录后点击 'New +' -> 'Web Service'")
    print("4. 选择 'Connect a repository'")
    print("5. 选择您刚创建的 order-management-system 仓库")
    print("6. 配置信息：")
    print("   - Name: order-management-system")
    print("   - Environment: Python")
    print("   - Build Command: pip install -r requirements.txt")
    print("   - Start Command: python run_app.py")
    print("7. 点击 'Create Web Service'")
    print("8. 等待部署完成（约 5-10 分钟）")
    
    input("部署完成后，请按回车键继续...")
    
    print("🎉 部署完成！")
    print("您的应用现在应该可以通过 Render 提供的链接访问了")
    return True

def main():
    """主函数"""
    print("🚀 集运管理系统 - Render 云端部署工具")
    print("=" * 50)
    print("此工具将帮助您将应用部署到 Render 云端")
    print("部署后，任何人都可以通过链接访问您的系统")
    print("=" * 50)
    
    # 检查依赖
    if not check_git():
        return
    
    # 初始化 Git 仓库
    init_git_repo()
    
    # 创建 Render 配置
    create_render_config()
    
    # 创建 GitHub 仓库
    if not create_github_repo():
        return
    
    # 部署到 Render
    if deploy_to_render():
        print("\n🎉 恭喜！您的集运管理系统已成功部署到云端！")
        print("\n现在您可以:")
        print("1. 在 Render 控制台查看您的应用链接")
        print("2. 分享这个链接给团队成员")
        print("3. 在任何设备上访问系统")
        print("4. 关闭您的电脑，系统依然在线")
        print("5. 享受24/7的云端服务")
    else:
        print("\n❌ 部署失败，请检查错误信息并重试")

if __name__ == '__main__':
    main() 