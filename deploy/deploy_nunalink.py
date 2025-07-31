#!/usr/bin/env python3
"""
Nunalink.com 域名部署工具
一键将集运管理系统部署到 Render 云端，并使用 nunalink.com 域名
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
        subprocess.run(['git', 'commit', '-m', 'Initial commit for nunalink.com deployment'], check=True)
        print("✅ Git 仓库初始化完成")
    else:
        print("✅ Git 仓库已存在")
        # 提交当前更改
        try:
            subprocess.run(['git', 'add', '.'], check=True)
            subprocess.run(['git', 'commit', '-m', 'Update configuration for nunalink.com'], check=True)
            print("✅ 配置更改已提交")
        except subprocess.CalledProcessError:
            print("ℹ️ 没有新的更改需要提交")

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
        # 检查是否已有远程仓库
        result = subprocess.run(['git', 'remote', '-v'], capture_output=True, text=True)
        if 'origin' in result.stdout:
            print("🔄 更新远程仓库地址...")
            subprocess.run(['git', 'remote', 'set-url', 'origin', repo_url], check=True)
        else:
            print("➕ 添加远程仓库...")
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
    return True

def setup_custom_domain():
    """设置自定义域名"""
    print("🌐 设置自定义域名 nunalink.com...")
    print("请按照以下步骤操作：")
    print("1. 在 Render 控制台找到您的 Web Service")
    print("2. 点击 'Settings' 标签")
    print("3. 找到 'Custom Domains' 部分")
    print("4. 点击 'Add Domain'")
    print("5. 输入: nunalink.com")
    print("6. 点击 'Add'")
    print("7. Render 会提供 DNS 记录，请按照以下步骤配置：")
    print("")
    print("DNS 配置步骤：")
    print("1. 登录您的域名注册商（如 GoDaddy、Namecheap 等）")
    print("2. 找到 nunalink.com 的 DNS 管理")
    print("3. 添加以下 DNS 记录：")
    print("   - 类型: CNAME")
    print("   - 名称: @ 或留空")
    print("   - 值: [Render 提供的 CNAME 值]")
    print("4. 保存 DNS 设置")
    print("5. 等待 DNS 传播（通常需要几分钟到几小时）")
    
    input("DNS 配置完成后，请按回车键继续...")
    
    print("✅ 自定义域名配置完成！")
    return True

def verify_deployment():
    """验证部署"""
    print("🔍 验证部署...")
    print("请访问以下链接验证部署是否成功：")
    print("1. Render 提供的链接: https://order-management-system.onrender.com")
    print("2. 自定义域名: https://nunalink.com")
    print("")
    print("如果遇到问题，请检查：")
    print("- Render 控制台中的构建日志")
    print("- 环境变量是否正确设置")
    print("- DNS 是否已正确配置")
    
    return True

def main():
    """主函数"""
    print("🚀 集运管理系统 - Nunalink.com 域名部署工具")
    print("=" * 60)
    print("此工具将帮助您将应用部署到 Render 云端")
    print("并使用 nunalink.com 作为自定义域名")
    print("=" * 60)
    
    # 检查依赖
    if not check_git():
        return
    
    # 初始化 Git 仓库
    init_git_repo()
    
    # 创建 GitHub 仓库
    if not create_github_repo():
        return
    
    # 部署到 Render
    if not deploy_to_render():
        return
    
    # 设置自定义域名
    if not setup_custom_domain():
        return
    
    # 验证部署
    verify_deployment()
    
    print("\n🎉 恭喜！您的集运管理系统已成功部署到云端！")
    print("\n现在您可以:")
    print("1. 通过 https://nunalink.com 访问您的系统")
    print("2. 分享这个链接给团队成员")
    print("3. 在任何设备上访问系统")
    print("4. 关闭您的电脑，系统依然在线")
    print("5. 享受24/7的云端服务")
    print("\n技术支持:")
    print("- 如果遇到问题，请检查 Render 控制台的日志")
    print("- 确保所有环境变量都已正确设置")
    print("- DNS 传播可能需要一些时间")

if __name__ == '__main__':
    main() 