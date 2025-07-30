#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Render环境数据库初始化脚本
用于在Render部署时创建数据库表
"""

import os
import sys
from datetime import datetime

# 添加项目路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def init_database():
    """初始化数据库"""
    try:
        from app import create_app
        from models import db, Package
        
        print("🚀 初始化Render数据库...")
        
        # 创建应用
        app = create_app()
        
        with app.app_context():
            # 创建所有表
            db.create_all()
            print("✅ 数据库表创建成功")
            
            # 检查是否有数据
            package_count = Package.query.count()
            print(f"📊 当前包裹数量: {package_count}")
            
            if package_count == 0:
                print("📝 数据库为空，可以开始添加数据")
            else:
                print("📝 数据库中已有数据")
            
            print("🎉 数据库初始化完成！")
            
    except Exception as e:
        print(f"❌ 数据库初始化失败: {str(e)}")
        import traceback
        traceback.print_exc()
        return False
    
    return True

if __name__ == '__main__':
    init_database() 