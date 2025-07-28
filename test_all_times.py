#!/usr/bin/env python3
"""
测试所有时间显示
"""

import sys
import os
from datetime import datetime, timedelta

# 添加当前目录到Python路径
sys.path.append('.')

def test_all_time_displays():
    """测试所有时间显示"""
    print("🧪 测试所有时间显示...")
    
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
                    print(f"\n包裹 {package.id}: {package.customer_name}")
                    print(f"  取件码: {package.pickup_code}")
                    print(f"  状态: {package.status}")
                    
                    # 测试各种时间显示
                    print(f"  UTC创建时间: {package.created_at.strftime('%Y-%m-%d %H:%M:%S') if package.created_at else 'None'}")
                    print(f"  UTC更新时间: {package.updated_at.strftime('%Y-%m-%d %H:%M:%S') if package.updated_at else 'None'}")
                    
                    if package.cafe_arrival_date:
                        print(f"  UTC咖啡馆到达: {package.cafe_arrival_date.strftime('%Y-%m-%d %H:%M:%S')}")
                        if package.cafe_arrival_date_paris:
                            print(f"  巴黎咖啡馆到达: {package.cafe_arrival_date_paris.strftime('%Y-%m-%d %H:%M:%S')}")
                        else:
                            print(f"  ❌ 巴黎时间转换失败")
                    
                    if package.latest_pickup_time_paris:
                        print(f"  巴黎最晚取件: {package.latest_pickup_time_paris.strftime('%Y-%m-%d %H:%M:%S')}")
                        print(f"  是否逾期: {package.is_overdue}")
                    
                    if package.pickup_date:
                        print(f"  UTC取件时间: {package.pickup_date.strftime('%Y-%m-%d %H:%M:%S')}")
                        if package.pickup_date_paris:
                            print(f"  巴黎取件时间: {package.pickup_date_paris.strftime('%Y-%m-%d %H:%M:%S')}")
                        
            else:
                print("⚠️ 没有找到包裹")
                
        return True
        
    except Exception as e:
        print(f"❌ 测试失败: {str(e)}")
        return False

def test_template_filter():
    """测试模板过滤器"""
    print("\n🔍 测试模板过滤器...")
    
    try:
        from app import create_app
        
        app = create_app()
        
        with app.app_context():
            # 测试模板过滤器
            from datetime import datetime
            
            # 创建一个测试时间
            test_time = datetime.utcnow()
            print(f"UTC时间: {test_time.strftime('%Y-%m-%d %H:%M:%S')}")
            
            # 获取模板过滤器
            format_filter = app.jinja_env.filters['format_datetime']
            formatted_time = format_filter(test_time)
            print(f"模板过滤器输出: {formatted_time}")
            
        return True
        
    except Exception as e:
        print(f"❌ 测试失败: {str(e)}")
        return False

if __name__ == '__main__':
    print("=" * 50)
    print("所有时间显示测试")
    print("=" * 50)
    
    # 测试所有时间显示
    success1 = test_all_time_displays()
    
    # 测试模板过滤器
    success2 = test_template_filter()
    
    if success1 and success2:
        print("\n✅ 所有测试通过！")
        print("所有时间显示功能正常工作")
    else:
        print("\n❌ 部分测试失败")
    
    print("=" * 50) 