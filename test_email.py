#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
邮件功能测试脚本
测试163邮箱配置是否正确
"""

import config_local
from flask import Flask
from flask_mail import Mail, Message
from datetime import datetime

def test_email_config():
    """测试邮件配置"""
    print("🧪 开始测试邮件配置...")
    
    # 创建Flask应用
    app = Flask(__name__)
    
    # 配置邮件
    app.config['MAIL_SERVER'] = config_local.MAIL_SERVER
    app.config['MAIL_PORT'] = config_local.MAIL_PORT
    app.config['MAIL_USE_TLS'] = config_local.MAIL_USE_TLS
    app.config['MAIL_USE_SSL'] = config_local.MAIL_USE_SSL
    app.config['MAIL_USERNAME'] = config_local.MAIL_USERNAME
    app.config['MAIL_PASSWORD'] = config_local.MAIL_PASSWORD
    
    mail = Mail(app)
    
    with app.app_context():
        try:
            # 创建测试邮件
            msg = Message(
                subject='🧪 集运系统邮件测试',
                sender=config_local.MAIL_USERNAME,
                recipients=[config_local.MAIL_USERNAME]  # 发给自己测试
            )
            
            msg.html = f"""
            <html>
            <body>
                <h2>🎉 邮件测试成功！</h2>
                <p>您的163邮箱配置正确，可以正常发送邮件。</p>
                <p>测试时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
                <p>邮件服务器: {config_local.MAIL_SERVER}</p>
                <p>发送邮箱: {config_local.MAIL_USERNAME}</p>
                <hr>
                <p style="color: #666; font-size: 12px;">
                    此邮件由集运系统自动发送，用于测试邮件配置。
                </p>
            </body>
            </html>
            """
            
            # 发送邮件
            mail.send(msg)
            print("✅ 邮件发送成功！")
            print(f"📧 请检查邮箱: {config_local.MAIL_USERNAME}")
            print("📝 邮件主题: 🧪 集运系统邮件测试")
            
        except Exception as e:
            print("❌ 邮件发送失败！")
            print(f"错误信息: {e}")
            print("\n🔧 可能的解决方案:")
            print("1. 检查163邮箱是否开启了SMTP服务")
            print("2. 确认授权码是否正确")
            print("3. 检查网络连接")
            print("4. 确认邮箱没有被限制")

if __name__ == '__main__':
    test_email_config() 