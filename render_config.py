# Render部署专用配置文件
# 这个文件专门用于Render平台部署

import os

class RenderConfig:
    """Render平台配置"""
    
    # 基础配置
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key-here')
    DEBUG = False
    
    # 数据库配置 - Render会自动提供DATABASE_URL
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///orders.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # 邮件配置 - 使用环境变量
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '587'))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() == 'true'
    MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL', 'false').lower() == 'true'
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    
    # 应用配置
    ITEMS_PER_PAGE = 20
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB
    
    # Render会自动提供应用URL
    BASE_URL = os.environ.get('BASE_URL', 'https://your-app-name.onrender.com')

# 导出配置
config = {
    'development': RenderConfig,
    'production': RenderConfig,
    'testing': RenderConfig,
    'default': RenderConfig
} 