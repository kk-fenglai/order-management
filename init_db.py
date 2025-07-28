#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
数据库初始化脚本
删除旧数据库并创建新的数据库表
"""

import os
import config_local
from app import create_app
from models import db

def init_database():
    """初始化数据库"""
    print("🗄️ 开始初始化数据库...")
    
    # 创建应用
    app = create_app()
    
    with app.app_context():
        # 删除所有表
        print("🗑️ 删除现有数据库表...")
        db.drop_all()
        
        # 创建所有表
        print("🏗️ 创建新的数据库表...")
        db.create_all()
        
        print("✅ 数据库初始化完成！")
        print("📁 数据库文件位置: instance/orders.db")

if __name__ == '__main__':
    init_database() 