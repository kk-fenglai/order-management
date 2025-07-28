# Render部署指南

## 🚀 在Render上部署集运管理系统

### 1. 准备工作

#### 1.1 创建Gmail应用专用密码
1. 登录你的Gmail账户
2. 进入"安全性"设置
3. 开启"两步验证"
4. 生成"应用专用密码"
5. 保存这个密码（16位字符）

#### 1.2 准备代码
确保你的代码已经推送到GitHub仓库。

### 2. 在Render上创建应用

#### 2.1 创建Web Service
1. 登录Render控制台
2. 点击"New +" → "Web Service"
3. 连接你的GitHub仓库
4. 选择仓库：`order-management-system`

#### 2.2 配置应用设置
```
Name: order-management-system (或你喜欢的名称)
Environment: Python 3
Build Command: pip install -r requirements.txt
Start Command: gunicorn app:app
```

### 3. 环境变量配置

在Render控制台的"Environment"标签页中添加以下环境变量：

#### 3.1 基础配置
```
SECRET_KEY = your-random-secret-key-here
FLASK_DEBUG = false
```

#### 3.2 邮件配置（Gmail）
```
MAIL_SERVER = smtp.gmail.com
MAIL_PORT = 587
MAIL_USE_TLS = true
MAIL_USE_SSL = false
MAIL_USERNAME = your-gmail@gmail.com
MAIL_PASSWORD = your-16-digit-app-password
```

#### 3.3 应用配置
```
BASE_URL = https://your-app-name.onrender.com
```

### 4. 创建requirements.txt

确保你的`requirements.txt`包含以下内容：

```txt
Flask==2.3.3
Flask-SQLAlchemy==3.0.5
Flask-Mail==0.9.1
Werkzeug==2.3.7
pandas==2.1.1
openpyxl==3.1.2
qrcode[pil]==7.4.2
pytz==2023.3
Pillow==10.0.1
python-dotenv==1.0.0
gunicorn==21.2.0
```

### 5. 修改应用入口

创建`render_app.py`文件：

```python
from app import create_app

app = create_app('production')

if __name__ == '__main__':
    app.run()
```

### 6. 数据库配置

#### 6.1 使用Render PostgreSQL（推荐）
1. 在Render上创建PostgreSQL数据库
2. 获取连接字符串
3. 设置环境变量：
```
DATABASE_URL = postgresql://username:password@host:port/database
```

#### 6.2 使用SQLite（简单但有限制）
```
DATABASE_URL = sqlite:///orders.db
```

### 7. 常见问题解决

#### 7.1 邮件发送失败
**问题**：邮件无法发送
**解决方案**：
- 确保使用Gmail应用专用密码
- 检查环境变量配置
- 使用587端口而不是25端口

#### 7.2 数据库连接失败
**问题**：无法连接数据库
**解决方案**：
- 检查DATABASE_URL环境变量
- 确保数据库服务已启动
- 检查网络连接

#### 7.3 应用启动失败
**问题**：应用无法启动
**解决方案**：
- 检查requirements.txt
- 确保所有依赖都已安装
- 查看Render日志

### 8. 测试部署

#### 8.1 检查应用状态
1. 访问你的Render应用URL
2. 检查是否正常加载
3. 测试基本功能

#### 8.2 测试邮件功能
1. 创建一个测试包裹
2. 尝试发送邮件
3. 检查邮件是否收到

### 9. 监控和维护

#### 9.1 查看日志
- 在Render控制台查看应用日志
- 监控错误和警告信息

#### 9.2 性能优化
- 使用Render的付费计划获得更好性能
- 定期清理数据库
- 监控资源使用情况

### 10. 安全注意事项

#### 10.1 环境变量
- 不要在代码中硬编码敏感信息
- 使用环境变量存储密码和密钥
- 定期更新密钥

#### 10.2 数据库安全
- 使用强密码
- 定期备份数据
- 限制数据库访问

## 📞 获取帮助

如果遇到问题：
1. 查看Render文档
2. 检查应用日志
3. 提交GitHub Issue
4. 联系技术支持

---

**注意**：Render免费计划有一些限制，如果遇到性能问题，考虑升级到付费计划。 