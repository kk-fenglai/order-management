#!/usr/bin/env python3
"""
检查 Nunalink.com 配置脚本
验证所有配置文件中的域名设置是否正确
"""

import os
import re

def check_file_for_domain(file_path, domain="nunalink.com"):
    """检查文件中是否包含正确的域名"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # 查找域名相关的配置
        patterns = [
            r'BASE_URL\s*=\s*["\']?https://([^"\'\s]+)["\']?',
            r'https://([^"\'\s]+)',
        ]
        
        found_domains = []
        for pattern in patterns:
            matches = re.findall(pattern, content)
            found_domains.extend(matches)
        
        # 过滤掉常见的无关域名
        filtered_domains = [d for d in found_domains if 'render.com' in d or domain in d]
        
        if filtered_domains:
            print(f"  📄 {file_path}:")
            for d in filtered_domains:
                if domain in d:
                    print(f"    ✅ 找到正确域名: {d}")
                else:
                    print(f"    ⚠️  找到其他域名: {d}")
        else:
            print(f"  📄 {file_path}: 未找到域名配置")
            
    except FileNotFoundError:
        print(f"  ❌ {file_path}: 文件不存在")
    except Exception as e:
        print(f"  ❌ {file_path}: 读取错误 - {e}")

def main():
    """主函数"""
    print("🔍 检查 Nunalink.com 配置")
    print("=" * 50)
    
    # 需要检查的文件列表
    files_to_check = [
        'render.yaml',
        'render_env_simple.txt',
        'config.py',
        'config_local.py.example'
    ]
    
    for file_path in files_to_check:
        check_file_for_domain(file_path)
    
    print("\n" + "=" * 50)
    print("📋 配置检查完成")
    print("\n下一步操作:")
    print("1. 如果所有配置都正确，运行: python deploy/deploy_nunalink.py")
    print("2. 或者双击运行: deploy_nunalink.bat")
    print("3. 按照提示完成部署到 Render")
    print("4. 配置 nunalink.com 域名")

if __name__ == '__main__':
    main() 