# Render部署专用应用入口
# 这个文件专门用于Render平台部署

from app import create_app

# 创建生产环境应用实例
app = create_app('production')

if __name__ == '__main__':
    app.run() 