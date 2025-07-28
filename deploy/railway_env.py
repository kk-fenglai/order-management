#!/usr/bin/env python3
"""
Railway 环境变量配置
用于在 Railway 云端设置邮件配置等环境变量
"""

import subprocess
import os

def set_railway_env():
    """设置 Railway 环境变量"""
    print("⚙️ 设置 Railway 环境变量...")
    
    # 邮件配置
    env_vars = {
        'MAIL_SERVER': 'smtp.163.com',
        'MAIL_PORT': '465',
        'MAIL_USE_SSL': 'True',
        'MAIL_USERNAME': 'alzy1210@163.com',
        'MAIL_PASSWORD': 'MAjQjkgenAqciFEW',
        'SECRET_KEY': 'your-secret-key-here-change-this',
        'FLASK_ENV': 'production',
        'DATABASE_URL': 'sqlite:///orders.db'
    }
    
    try:
        for key, value in env_vars.items():
            print(f"设置 {key}...")
            subprocess.run(['railway', 'variables', 'set', f'{key}={value}'], check=True)
        
        print("✅ 环境变量设置完成")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ 环境变量设置失败: {e}")
        return False

def main():
    """主函数"""
    print("⚙️ Railway 环境变量配置工具")
    print("=" * 40)
    
    if set_railway_env():
        print("\n🎉 环境变量配置成功！")
        print("现在您的应用已经配置好邮件发送功能")
    else:
        print("\n❌ 环境变量配置失败")
        print("请确保已经登录 Railway 并创建了项目")

if __name__ == '__main__':
    main() 