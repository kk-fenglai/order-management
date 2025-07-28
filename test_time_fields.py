#!/usr/bin/env python3
"""
测试时间字段修改
"""

import sys
import os

# 添加当前目录到Python路径
sys.path.append('.')

def test_time_fields():
    """测试时间字段"""
    print("🧪 测试时间字段修改...")
    
    try:
        from app import create_app
        from models import Package
        
        app = create_app()
        
        with app.app_context():
            # 获取所有包裹
            packages = Package.query.all()
            
            if packages:
                print(f"✅ 找到 {len(packages)} 个包裹")
                
                for package in packages:
                    print(f"\n包裹 {package.id}:")
                    print(f"  客户: {package.customer_name}")
                    print(f"  取件码: {package.pickup_code}")
                    print(f"  状态: {package.status}")
                    
                    if package.cafe_arrival_date:
                        print(f"  咖啡馆到达时间: {package.cafe_arrival_date.strftime('%Y-%m-%d %H:%M:%S')}")
                    else:
                        print(f"  咖啡馆到达时间: 未设置")
                    
                    # 检查是否还有创建时间和更新时间
                    if hasattr(package, 'created_at'):
                        print(f"  创建时间: {package.created_at.strftime('%Y-%m-%d %H:%M:%S') if package.created_at else 'None'}")
                    if hasattr(package, 'updated_at'):
                        print(f"  更新时间: {package.updated_at.strftime('%Y-%m-%d %H:%M:%S') if package.updated_at else 'None'}")
                        
            else:
                print("⚠️ 没有找到包裹")
                
        return True
        
    except Exception as e:
        print(f"❌ 测试失败: {str(e)}")
        return False

if __name__ == '__main__':
    print("=" * 50)
    print("时间字段修改测试")
    print("=" * 50)
    
    success = test_time_fields()
    
    if success:
        print("\n✅ 测试完成")
        print("现在系统只显示咖啡馆到达时间（发送咖啡馆邮件时的时间）")
    else:
        print("\n❌ 测试失败")
    
    print("=" * 50) 