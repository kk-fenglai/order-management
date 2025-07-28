# 本地配置文件 - 包含邮箱信息
# 注意：这个文件包含敏感信息，不要提交到版本控制系统

import os

# 应用配置
SECRET_KEY = 'dev-secret-key-change-in-production'
FLASK_DEBUG = True

# 数据库配置
DATABASE_URL = 'sqlite:///orders.db'

# 邮件配置 - Gmail (推荐用于Render部署)
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = 'dengfenglai1210@gmail.com'  # 替换为你的Gmail
MAIL_PASSWORD = 'fwpkjjgtfyqomqqa'     # Gmail应用专用密码

# 服务器配置 - 使用实际IP地址，让手机可以访问
BASE_URL = 'http://192.168.43.40:5000'

# 设置环境变量
os.environ['SECRET_KEY'] = SECRET_KEY
os.environ['FLASK_DEBUG'] = str(FLASK_DEBUG)
os.environ['DATABASE_URL'] = DATABASE_URL
os.environ['MAIL_SERVER'] = MAIL_SERVER
os.environ['MAIL_PORT'] = str(MAIL_PORT)
os.environ['MAIL_USE_TLS'] = str(MAIL_USE_TLS)
os.environ['MAIL_USE_SSL'] = str(MAIL_USE_SSL)
os.environ['MAIL_USERNAME'] = MAIL_USERNAME
os.environ['MAIL_PASSWORD'] = MAIL_PASSWORD
os.environ['BASE_URL'] = BASE_URL 