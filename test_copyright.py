#!/usr/bin/env python3
"""
测试版权信息更新
"""

import os

def test_copyright_update():
    """测试版权信息更新"""
    print("🧪 测试版权信息更新...")
    
    # 需要检查的文件列表
    files_to_check = [
        'templates/base.html',
        'templates/email/shenzhen_arrival.html',
        'templates/email/cafe_arrival.html',
        'templates/email/package_notification.html',
        'templates/email/order_confirmation.html'
    ]
    
    old_copyright = "2024"
    new_copyright = "2025 NÜNA LINKS 集运中心"
    
    all_updated = True
    
    for file_path in files_to_check:
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                if old_copyright in content:
                    print(f"❌ {file_path}: 仍包含旧版权信息")
                    all_updated = False
                elif new_copyright in content:
                    print(f"✅ {file_path}: 版权信息已更新")
                else:
                    print(f"⚠️ {file_path}: 未找到版权信息")
                    
            except Exception as e:
                print(f"❌ {file_path}: 读取失败 - {str(e)}")
                all_updated = False
        else:
            print(f"❌ {file_path}: 文件不存在")
            all_updated = False
    
    return all_updated

def show_copyright_info():
    """显示版权信息"""
    print("\n📋 版权信息概览:")
    print("=" * 50)
    
    files_to_check = [
        'templates/base.html',
        'templates/email/shenzhen_arrival.html',
        'templates/email/cafe_arrival.html',
        'templates/email/package_notification.html',
        'templates/email/order_confirmation.html'
    ]
    
    for file_path in files_to_check:
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # 查找版权信息
                lines = content.split('\n')
                for i, line in enumerate(lines):
                    if 'NÜNA LINKS' in line and '2025' in line and '保留所有权利' in line:
                        print(f"{file_path}:")
                        print(f"  第{i+1}行: {line.strip()}")
                        print()
                        break
                        
            except Exception as e:
                print(f"❌ {file_path}: 读取失败 - {str(e)}")

if __name__ == '__main__':
    print("=" * 50)
    print("版权信息更新测试")
    print("=" * 50)
    
    # 测试版权信息更新
    success = test_copyright_update()
    
    if success:
        print("\n✅ 所有版权信息已成功更新！")
    else:
        print("\n❌ 部分版权信息更新失败")
    
    # 显示版权信息概览
    show_copyright_info()
    
    print("=" * 50) 