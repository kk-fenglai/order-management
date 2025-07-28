#!/usr/bin/env python3
"""
数据库迁移脚本：为现有包裹添加二维码字段
"""

import os
import sys
from datetime import datetime

# 添加项目根目录到Python路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import create_app
from models import db, Package

def migrate_add_qr_code():
    """为现有包裹添加二维码字段"""
    app = create_app()
    
    with app.app_context():
        print("开始数据库迁移：添加二维码字段...")
        
        # 获取所有没有二维码的包裹
        packages_without_qr = Package.query.filter_by(qr_code_image=None).all()
        
        if not packages_without_qr:
            print("所有包裹都已经有二维码了！")
            return
        
        print(f"找到 {len(packages_without_qr)} 个包裹需要生成二维码...")
        
        success_count = 0
        error_count = 0
        
        for package in packages_without_qr:
            try:
                # 生成二维码
                qr_code_image = Package.generate_qr_code(package.pickup_code, app.config.get('BASE_URL'))
                
                if qr_code_image:
                    package.qr_code_image = qr_code_image
                    package.updated_at = datetime.utcnow()
                    success_count += 1
                    print(f"✅ 成功为包裹 {package.id} ({package.customer_name}) 生成二维码")
                else:
                    error_count += 1
                    print(f"❌ 包裹 {package.id} ({package.customer_name}) 二维码生成失败")
                    
            except Exception as e:
                error_count += 1
                print(f"❌ 包裹 {package.id} ({package.customer_name}) 处理失败: {str(e)}")
        
        # 提交更改
        try:
            db.session.commit()
            print(f"\n迁移完成！")
            print(f"成功: {success_count} 个包裹")
            print(f"失败: {error_count} 个包裹")
        except Exception as e:
            db.session.rollback()
            print(f"❌ 提交更改失败: {str(e)}")

if __name__ == '__main__':
    migrate_add_qr_code() 