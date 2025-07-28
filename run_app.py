#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
集运管理系统启动脚本
适用于Anaconda环境
"""

# 导入本地配置
import config_local

# 导入应用
from app import create_app

if __name__ == '__main__':
    print("🚀 启动集运管理系统...")
    print(f"📧 邮件配置: {config_local.MAIL_USERNAME}")
    print(f"🌐 访问地址: http://localhost:5000")
    print("=" * 50)
    
    # 创建应用
    app = create_app()
    
    # 创建数据库表
    with app.app_context():
        from models import db
        db.create_all()
        print("✅ 数据库初始化完成")
    
    # 运行应用
    app.run(debug=True, host='0.0.0.0', port=5000) 