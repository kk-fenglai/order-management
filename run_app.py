#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
集运管理系统启动脚本
适用于Anaconda环境
"""

import os

# 导入应用
from app import create_app

if __name__ == '__main__':
    print("🚀 启动集运管理系统...")
    
    # 检查是否为Render环境
    is_render = os.environ.get('RENDER', False)
    if is_render:
        print("🌐 运行在Render环境")
        print(f"📧 邮件配置: {os.environ.get('MAIL_USERNAME', '未设置')}")
    else:
        # 本地环境
        try:
            import config_local
            print(f"📧 邮件配置: {config_local.MAIL_USERNAME}")
        except ImportError:
            print("📧 邮件配置: 使用环境变量")
        print(f"🌐 访问地址: http://localhost:5000")
    
    print("=" * 50)
    
    # 创建应用
    app = create_app()
    
    # 创建数据库表
    with app.app_context():
        from models import db
        db.create_all()
        print("✅ 数据库初始化完成")
    
    # 运行应用 - 禁用自动重载以避免watchdog问题
    app.run(debug=True, host='0.0.0.0', port=5000, use_reloader=False) 