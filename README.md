# 集运管理系统

一个功能完整、安全可靠的集运包裹管理系统，支持自动邮件通知、二维码生成、状态跟踪等功能。

## 🚀 主要特性

### 安全性
- ✅ **环境变量配置**：敏感信息不再硬编码
- ✅ **输入验证**：完整的表单验证和邮箱格式检查
- ✅ **错误处理**：完善的异常处理和日志记录
- ✅ **SQL注入防护**：使用ORM防止SQL注入

### 代码结构
- ✅ **模块化设计**：代码分离到不同文件
- ✅ **配置管理**：独立的配置文件
- ✅ **应用工厂模式**：更好的应用初始化
- ✅ **工具函数**：可复用的工具函数

### 功能增强
- ✅ **分页功能**：支持大量数据的分页显示
- ✅ **搜索功能**：支持按姓名、邮箱、单号搜索
- ✅ **状态筛选**：按包裹状态筛选
- ✅ **统计信息**：数据统计和可视化
- ✅ **备注功能**：支持包裹备注
- ✅ **时间跟踪**：完整的创建和更新时间

### 用户体验
- ✅ **响应式设计**：支持移动端
- ✅ **错误页面**：友好的错误提示页面
- ✅ **表单验证**：实时表单验证
- ✅ **操作确认**：重要操作的确认提示

## 📋 功能特性

- 🔐 **安全可靠**：环境变量配置，输入验证
- 📧 **邮件通知**：自动发送到达和取件通知
- 📱 **二维码生成**：批量生成取件码二维码
- 📊 **状态管理**：完整的包裹状态跟踪
- 🔍 **搜索筛选**：多维度搜索和筛选
- 📈 **数据统计**：实时统计信息
- 📱 **移动友好**：响应式设计

## 🛠️ 技术栈

- **后端**: Flask 2.3.3, SQLAlchemy 3.0.5
- **前端**: Bootstrap 5, Font Awesome 6
- **数据库**: SQLite (可扩展至MySQL/PostgreSQL)
- **邮件**: Flask-Mail
- **二维码**: qrcode[pil]
- **验证**: email-validator

## 📦 快速开始

### 1. 安装依赖
```bash
pip install -r requirements.txt
```

### 2. 配置邮箱
编辑 `config_local.py` 文件，配置你的邮箱信息：
```python
MAIL_USERNAME = 'your-email@163.com'
MAIL_PASSWORD = 'your-authorization-code'
```

### 3. 启动系统
```bash
# 方式一：使用启动脚本
python run_app.py

# 方式二：使用批处理文件（Windows）
start_anaconda.bat

# 方式三：直接运行
python app.py
```

### 4. 访问系统
浏览器打开：`http://localhost:5000`

## 📁 项目结构

```
order-management-system/
├── app.py                    # 主应用文件
├── config.py                 # 配置文件
├── config_local.py           # 本地配置（包含邮箱信息）
├── models.py                 # 数据模型
├── utils.py                  # 工具函数
├── run_app.py                # 启动脚本
├── test_email.py             # 邮件测试脚本
├── start_anaconda.bat        # Anaconda启动脚本
├── requirements.txt          # Python依赖
├── README.md                 # 说明文档
├── templates/                # HTML模板
│   ├── base.html             # 基础模板
│   ├── index.html            # 主页
│   ├── package_detail.html   # 包裹详情
│   ├── new_package.html      # 新建包裹
│   ├── qr_codes.html         # 二维码页面
│   ├── stats.html            # 统计页面
│   ├── errors/               # 错误页面
│   │   ├── 404.html
│   │   └── 500.html
│   └── email/                # 邮件模板
│       ├── shenzhen_arrival.html
│       └── cafe_arrival.html
└── instance/                 # 实例文件夹
    └── orders.db             # SQLite数据库
```

## 📖 使用指南

### 创建包裹
1. 点击"新建包裹"按钮
2. 填写客户信息（姓名、邮箱）
3. 填写深圳快递单号
4. 可选填写备注信息
5. 系统自动生成取件码并发送通知邮件

### 管理包裹
- **查看列表**：支持搜索、筛选、分页
- **查看详情**：完整的包裹信息和操作面板
- **状态更新**：支持状态变更和时间记录
- **邮件重发**：可重新发送通知邮件

### 二维码功能
- 自动生成包含所有取件码的二维码
- 支持打印和分享
- 包含完整的取件信息

### 统计信息
- 实时显示包裹数量统计
- 今日新增数据
- 完成率可视化

## 🔧 邮件配置

### 163邮箱
```python
MAIL_SERVER = 'smtp.163.com'
MAIL_PORT = 25
MAIL_USE_TLS = False
MAIL_USE_SSL = False
MAIL_USERNAME = 'your-email@163.com'
MAIL_PASSWORD = 'your-authorization-code'
```

### Gmail
```python
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = 'your-email@gmail.com'
MAIL_PASSWORD = 'your-app-password'
```

### QQ邮箱
```python
MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = 'your-email@qq.com'
MAIL_PASSWORD = 'your-authorization-code'
```

## 🧪 测试

### 测试邮件功能
```bash
python test_email.py
```

### 测试API接口
访问：`http://localhost:5000/api/packages`

## 🔒 安全特性

- **环境变量**：敏感信息通过环境变量管理
- **输入验证**：完整的表单验证和SQL注入防护
- **错误处理**：友好的错误提示，不暴露系统信息
- **日志记录**：完整的操作日志记录

## 🚀 部署建议

### 开发环境
```bash
python run_app.py
```

### 生产环境
```bash
# 使用 Gunicorn
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app

# 或使用 uWSGI
pip install uwsgi
uwsgi --http 0.0.0.0:5000 --module app:app
```

## 🆘 故障排除

### 邮件发送失败
1. 检查邮箱配置是否正确
2. 确认授权码/应用密码
3. 检查网络连接
4. 查看日志信息

### 数据库问题
- 删除 `instance/orders.db` 重新创建
- 确保有写入权限
- 检查数据库连接配置

### 端口被占用
修改端口号：
```python
app.run(debug=True, host='0.0.0.0', port=5001)
```

## 📄 许可证

MIT License

## 📞 支持

如有问题或建议，请提交 Issue 或联系开发者。 