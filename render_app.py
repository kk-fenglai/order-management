# Render部署专用应用入口
# 这个文件专门用于Render平台部署

import os
from app import create_app

# 创建生产环境应用实例
app = create_app('production')

# 添加环境检查
@app.before_first_request
def check_environment():
    """检查环境变量配置"""
    print("🔍 检查Render环境变量...")
    print(f"MAIL_SERVER: {os.environ.get('MAIL_SERVER')}")
    print(f"MAIL_USERNAME: {os.environ.get('MAIL_USERNAME')}")
    print(f"BASE_URL: {os.environ.get('BASE_URL')}")

if __name__ == '__main__':
    app.run() 