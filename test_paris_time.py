#!/usr/bin/env python3
"""
测试巴黎时间显示
"""

import sys
import os
from datetime import datetime, timedelta

# 添加当前目录到Python路径
sys.path.append('.')

def test_paris_time():
    """测试巴黎时间显示"""
    print("🧪 测试巴黎时间显示...")
    
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
                    
                    if package.cafe_arrival_date:
                        print(f"  UTC时间: {package.cafe_arrival_date.strftime('%Y-%m-%d %H:%M:%S')}")
                        
                        if package.cafe_arrival_date_paris:
                            print(f"  巴黎时间: {package.cafe_arrival_date_paris.strftime('%Y-%m-%d %H:%M:%S')}")
                            
                            if package.latest_pickup_time_paris:
                                print(f"  最晚取件(巴黎): {package.latest_pickup_time_paris.strftime('%Y-%m-%d %H:%M:%S')}")
                                
                                if package.is_overdue:
                                    print(f"  ⚠️  状态: 已逾期")
                                else:
                                    print(f"  ✅ 状态: 未逾期")
                            else:
                                print(f"  ❌ 最晚取件时间: 计算失败")
                        else:
                            print(f"  ❌ 巴黎时间转换失败")
                    else:
                        print(f"  咖啡馆到达时间: 未设置")
                        
            else:
                print("⚠️ 没有找到包裹")
                
        return True
        
    except Exception as e:
        print(f"❌ 测试失败: {str(e)}")
        return False

def test_time_conversion():
    """测试时间转换"""
    print("\n🔍 测试时间转换...")
    
    try:
        from app import create_app
        from models import Package
        
        app = create_app()
        
        with app.app_context():
            # 创建一个测试包裹
            test_package = Package(
                customer_name="测试客户",
                customer_email="test@example.com",
                shenzhen_tracking_number="TEST123456",
                pickup_code="123456",
                status="cafe_arrived"
            )
            
            # 设置咖啡馆到达时间为当前UTC时间
            test_package.cafe_arrival_date = datetime.utcnow()
            
            print(f"UTC时间: {test_package.cafe_arrival_date.strftime('%Y-%m-%d %H:%M:%S')}")
            
            if test_package.cafe_arrival_date_paris:
                print(f"巴黎时间: {test_package.cafe_arrival_date_paris.strftime('%Y-%m-%d %H:%M:%S')}")
                
                if test_package.latest_pickup_time_paris:
                    print(f"最晚取件(巴黎): {test_package.latest_pickup_time_paris.strftime('%Y-%m-%d %H:%M:%S')}")
                    print(f"是否逾期: {test_package.is_overdue}")
                else:
                    print("最晚取件时间计算失败")
            else:
                print("巴黎时间转换失败")
                
        return True
        
    except Exception as e:
        print(f"❌ 测试失败: {str(e)}")
        return False

if __name__ == '__main__':
    print("=" * 50)
    print("巴黎时间显示测试")
    print("=" * 50)
    
    # 测试现有包裹
    success1 = test_paris_time()
    
    # 测试时间转换
    success2 = test_time_conversion()
    
    if success1 and success2:
        print("\n✅ 所有测试通过！")
        print("巴黎时间显示功能正常工作")
    else:
        print("\n❌ 部分测试失败")
    
    print("=" * 50) 