#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Render环境变量检查脚本
用于验证Render上的环境变量配置是否正确
"""

import os

def check_render_environment():
    """检查Render环境变量配置"""
    
    print("🔍 检查Render环境变量配置...")
    print("=" * 50)
    
    # 检查基础配置
    secret_key = os.environ.get('SECRET_KEY')
    flask_debug = os.environ.get('FLASK_DEBUG')
    
    print(f"SECRET_KEY: {'✅ 已设置' if secret_key else '❌ 未设置'}")
    print(f"FLASK_DEBUG: {flask_debug}")
    
    # 检查邮件配置
    mail_server = os.environ.get('MAIL_SERVER')
    mail_port = os.environ.get('MAIL_PORT')
    mail_use_tls = os.environ.get('MAIL_USE_TLS')
    mail_use_ssl = os.environ.get('MAIL_USE_SSL')
    mail_username = os.environ.get('MAIL_USERNAME')
    mail_password = os.environ.get('MAIL_PASSWORD')
    
    print("\n📧 邮件配置检查:")
    print(f"MAIL_SERVER: {mail_server}")
    print(f"MAIL_PORT: {mail_port}")
    print(f"MAIL_USE_TLS: {mail_use_tls}")
    print(f"MAIL_USE_SSL: {mail_use_ssl}")
    print(f"MAIL_USERNAME: {mail_username}")
    print(f"MAIL_PASSWORD: {'✅ 已设置' if mail_password else '❌ 未设置'}")
    
    # 检查应用配置
    base_url = os.environ.get('BASE_URL')
    print(f"\n🌐 BASE_URL: {base_url}")
    
    # 检查数据库配置
    database_url = os.environ.get('DATABASE_URL')
    print(f"🗄️ DATABASE_URL: {'✅ 已设置' if database_url else '❌ 未设置'}")
    
    print("\n" + "=" * 50)
    
    # 验证邮件配置
    if all([mail_server, mail_port, mail_username, mail_password]):
        print("✅ 邮件配置完整")
        
        if mail_server == 'smtp.gmail.com' and mail_port == '587':
            print("✅ Gmail配置正确")
        else:
            print("⚠️ 建议使用Gmail配置")
            
    else:
        print("❌ 邮件配置不完整")
        print("请在Render控制台设置以下环境变量:")
        print("""
MAIL_SERVER = smtp.gmail.com
MAIL_PORT = 587
MAIL_USE_TLS = true
MAIL_USE_SSL = false
MAIL_USERNAME = dengfenglai1210@gmail.com
MAIL_PASSWORD = fwpkjjgtfyqomqqa
        """)

if __name__ == '__main__':
    check_render_environment() 